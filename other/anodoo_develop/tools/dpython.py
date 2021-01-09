if isinstance(route, list):

if isinstance(response, (bytes, str)):
if isinstance(response, werkzeug.wrappers.BaseResponse):

request.env.ref('base.public_user').id

    if pathname is None:
        pathname = os.path.join(module, filename)
    ext = os.path.splitext(filename)[1].lower()   获取文件后缀

#res_mode and res_id
if attachment.res_model and attachment.res_id:
                record = self.env[attachment.res_model].browse(attachment.res_id)

self.env.user.has_group('crm.group_use_lead')
type = fields.Selection([('lead', 'Lead'), ('opportunity', 'Opportunity')], index=True, required=True, tracking=15,
        default=lambda self: 'lead' if self.env['res.users'].has_group('crm.group_use_lead') else 'opportunity',
        help="Type is used to separate Leads and Opportunities")