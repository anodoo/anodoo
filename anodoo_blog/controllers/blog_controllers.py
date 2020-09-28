# -*- coding: utf-8 -*-

from odoo import http
import werkzeug

from odoo.http import request
from odoo import http, fields
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.addons.website.controllers.main import QueryURL


class AnodooBlog(WebsiteBlog):
    
    #override
    @http.route()
    def blog(self, blog=None, tag=None, page=1, **opt):
        tags = tag
        active_tag_ids = tags and [unslug(tag)[1] for tag in tags.split(',')] or []
        if active_tag_ids:
            fixed_tag_slug = ",".join(slug(t) for t in request.env['blog.tag'].browse(active_tag_ids))
            if fixed_tag_slug != tags:
                return request.redirect(request.httprequest.full_path.replace("/tag/%s/" % tags, "/tag/%s/" % fixed_tag_slug, 1), 301)
            
        ConfigParameter = request.env['ir.config_parameter'].sudo()
        is_blog_website_mana2many = ConfigParameter.get_param('anodoo_blog.is_blog_website_mana2many')
        
        #return super(AnodooBlog, self).blog(blog=blog, tag=tag, page=page, **opt)
        #override
        Blog = request.env['blog.blog']
        if blog and not blog.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()

        blogs_domain = request.website.website_domain() + [('is_public', '=', True)]
        blogs = Blog.search(blogs_domain)

        if not blog and len(blogs) == 1:
            return werkzeug.utils.redirect('/blog/%s' % slug(blogs[0]), code=302)

        series, date_begin, date_end, state = opt.get('series'), opt.get('date_begin'), opt.get('date_end'), opt.get('state')

        values = self._prepare_blog_values(blogs=blogs, blog=blog, date_begin=date_begin, date_end=date_end, tags=tag, series=series, state=state, page=page)

        
        if blog:
            values['main_object'] = blog
            values['edit_in_backend'] = True
            values['blog_url'] = QueryURL('', ['blog', 'tag'], blog=blog, tag=tag, series=series, date_begin=date_begin, date_end=date_end)
        else:
            values['blog_url'] = QueryURL('/blog', ['tag'], series=series, date_begin=date_begin, date_end=date_end)

        #是否显示footer
        values['no_footer'] = ConfigParameter.get_param('anodoo_blog.is_hide_footer')
        
        return request.render("website_blog.blog_post_short", values)
        
    
    #override 增加:文章属于多个栏目
    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, series=False, state=False, page=False):
        """ Prepare all values to display the blogs index page or one specific blog"""
        BlogPost = request.env['blog.post']
        
        ConfigParameter = request.env['ir.config_parameter'].sudo()
        is_post_blog_mana2many = ConfigParameter.get_param('anodoo_blog.is_post_blog_mana2many')
            

        # prepare domain
        if not is_post_blog_mana2many:
            domain = request.website.website_domain()
        else:
            domain = ['|'] + request.website.website_domain() + [('multi_website_ids', 'in', [request.website.id])]
        
        #is_public 支持有些文章不在列表显示,但可以单独链接浏览
        domain += [('is_public', '=', True)]

        if blog:
            
            if is_post_blog_mana2many:
                domain += ['|', ('blog_id', '=', blog.id), ('multi_blog_ids', 'in', [blog.id])]
            else:
                domain += [('blog_id', '=', blog.id)]

        if date_begin and date_end:
            domain += [("post_date", ">=", date_begin), ("post_date", "<=", date_end)]

        active_tag_ids = tags and [unslug(tag)[1] for tag in tags.split(',')] or []
        if active_tag_ids:
            fixed_tag_slug = ",".join(slug(t) for t in request.env['blog.tag'].browse(active_tag_ids))
            if fixed_tag_slug != tags:
                return request.redirect(request.httprequest.full_path.replace("/tag/%s/" % tags, "/tag/%s/" % fixed_tag_slug, 1), 301)

            domain += [('tag_ids', 'in', active_tag_ids)]
            
        series_id = False
        if series:
            series_id = unslug(series)[1]
            domain += [('series_id', '=', series_id)]
        

        if request.env.user.has_group('website.group_website_designer'):
            count_domain = domain + [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())]
            published_count = BlogPost.search_count(count_domain)
            unpublished_count = BlogPost.search_count(domain) - published_count

            if state == "published":
                domain += [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())]
            elif state == "unpublished":
                domain += ['|', ("website_published", "=", False), ("post_date", ">", fields.Datetime.now())]
        else:
            domain += [("post_date", "<=", fields.Datetime.now())]

        use_cover = request.website.viewref('website_blog.opt_blog_cover_post').active
        fullwidth_cover = request.website.viewref('website_blog.opt_blog_cover_post_fullwidth_design').active

        # if blog, we show blog title, if use_cover and not fullwidth_cover we need pager + latest always
        offset = (page - 1) * self._blog_post_per_page
        first_post = BlogPost
        if not blog:
            first_post = BlogPost.search(domain + [('website_published', '=', True)], order="post_date desc, id asc", limit=1)
            if use_cover and not fullwidth_cover:
                offset += 1

        posts = BlogPost.search(domain, offset=offset, limit=self._blog_post_per_page, order="is_published desc, post_date desc, id asc")
        total = BlogPost.search_count(domain)

        pager = request.website.pager(
            url=request.httprequest.path.partition('/page/')[0],
            total=total,
            page=page,
            step=self._blog_post_per_page,
        )

        all_tags = blog and blogs.all_tags()[blog.id] or blogs.all_tags(join=True)
        tag_category = sorted(all_tags.mapped('category_id'), key=lambda category: category.name.upper())
        other_tags = sorted(all_tags.filtered(lambda x: not x.category_id), key=lambda tag: tag.name.upper())

        # for performance prefetch the first post with the others
        post_ids = (first_post | posts).ids
        
        PostSeries = request.env['anodoo.blog.post.series'].sudo()
        all_series = PostSeries.search(request.website.website_domain(), limit=10)
        series = PostSeries.browse(series_id)

        return {
            'date_begin': date_begin,
            'date_end': date_end,
            'first_post': first_post.with_prefetch(post_ids),
            'other_tags': other_tags,
            'tag_category': tag_category,
            'nav_list': self.nav_list(),
            'tags_list': self.tags_list,
            'pager': pager,
            'posts': posts.with_prefetch(post_ids),
            'tag': tags,
            'active_tag_ids': active_tag_ids,
            'domain': domain,
            'state_info': state and {"state": state, "published": published_count, "unpublished": unpublished_count},
            'blogs': blogs,
            'blog': blog,
            
            'series': series,
            'all_series': all_series
        }
        
    #Override: 增加系列,所有系列,相关文章#
    @http.route()
    def blog_post(self, blog, blog_post, tag_id=None, page=1, enable_editor=None, **post):
        """ Prepare all values to display the blog.

        :return dict values: values for the templates, containing

         - 'blog_post': browse of the current post
         - 'blog': browse of the current blog
         - 'blogs': list of browse records of blogs
         - 'tag': current tag, if tag_id in parameters
         - 'tags': all tags, for tag-based navigation
         - 'pager': a pager on the comments
         - 'nav_list': a dict [year][month] for archives navigation
         - 'next_post': next blog post, to direct the user towards the next interesting post
        """
        if not blog.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()

        BlogPost = request.env['blog.post']
        date_begin, date_end = post.get('date_begin'), post.get('date_end')

        pager_url = "/blogpost/%s" % blog_post.id

        pager = request.website.pager(
            url=pager_url,
            total=len(blog_post.website_message_ids),
            page=page,
            step=self._post_comment_per_page,
            scope=7
        )
        pager_begin = (page - 1) * self._post_comment_per_page
        pager_end = page * self._post_comment_per_page
        comments = blog_post.website_message_ids[pager_begin:pager_end]

        domain = request.website.website_domain() + [('is_public', '=', True)]
        blogs = blog.search(domain)

        tag = None
        if tag_id:
            tag = request.env['blog.tag'].browse(int(tag_id))
        blog_url = QueryURL('', ['blog', 'tag'], blog=blog_post.blog_id, tag=tag, date_begin=date_begin, date_end=date_end)

        if not blog_post.blog_id.id == blog.id:
            return request.redirect("/blog/%s/post/%s" % (slug(blog_post.blog_id), slug(blog_post)), code=301)

        tags = request.env['blog.tag'].search([])

        # Find next Post
        blog_post_domain = [('blog_id', '=', blog.id)]
        if not request.env.user.has_group('website.group_website_designer'):
            blog_post_domain += [('post_date', '<=', fields.Datetime.now())]

        all_post = BlogPost.search(blog_post_domain)

        if blog_post not in all_post:
            return request.redirect("/blog/%s" % (slug(blog_post.blog_id)))

        # should always return at least the current post
        all_post_ids = all_post.ids
        current_blog_post_index = all_post_ids.index(blog_post.id)
        nb_posts = len(all_post_ids)
        next_post_id = all_post_ids[(current_blog_post_index + 1) % nb_posts] if nb_posts > 1 else None
        next_post = next_post_id and BlogPost.browse(next_post_id) or False

        #begin:增加系列,所有系列,相关文章
        blog_post_series = blog_post.series_id
        
        PostSeries = request.env['anodoo.blog.post.series'].sudo()
        all_series = PostSeries.search(request.website.website_domain(), limit=10)

        relative_posts = blog_post.relative_post_ids
        #end:
        
        
        values = {
            'tags': tags,
            'tag': tag,
            'blog': blog,
            'blog_post': blog_post,
            'blogs': blogs,
            'main_object': blog_post,
            'nav_list': self.nav_list(blog),
            'enable_editor': enable_editor,
            'next_post': next_post,
            'date': date_begin,
            'blog_url': blog_url,
            'pager': pager,
            'comments': comments,
            
            #增加
            'blog_post_series': blog_post_series,
            'all_series':all_series,
            'relative_posts':relative_posts,
        }
        
        #是否显示footer
        ConfigParameter = request.env['ir.config_parameter'].sudo()
        values['no_footer'] = ConfigParameter.get_param('anodoo_blog.is_hide_footer')
        
        response = request.render("website_blog.blog_post_complete", values)

        request.session[request.session.sid] = request.session.get(request.session.sid, [])
        if not (blog_post.id in request.session[request.session.sid]):
            request.session[request.session.sid].append(blog_post.id)
            # Increase counter
            blog_post.sudo().write({
                'visits': blog_post.visits + 1,
            })
        return response
    
#     @http.route([
#         '/blog/series/<string:series>',
#         '/blog/series/<string:series>/page/<int:page>',
#     ], type='http', auth="public", website=True)
#     def blog_post_series(self, series=None, page=1, **opt):
#         Blog = request.env['blog.blog']
#         
# 
#         blogs_domain = request.website.website_domain() + [('is_public', '=', True)]
#         blogs = Blog.search(blogs_domain)
# 
#         date_begin, date_end, state = opt.get('date_begin'), opt.get('date_end'), opt.get('state')
# 
#         values = self._prepare_blog_values(blogs=blogs, blog=None, date_begin=date_begin, date_end=date_end, tags=None, series=series, state=state, page=page)
#         values['blog_url'] = QueryURL('/blog', ['tag'], date_begin=date_begin, date_end=date_end)
# 
#         
#         return request.render("website_blog.blog_post_short", values)
    
    