odoo.define('anodoo_website.form', function (require) {
'use strict';

var FormEditorRegistry = require('website_form.form_editor_registry');

FormEditorRegistry.add('create_website_form', {
    defaultTemplateName: 'anodoo_website.default_website_form',
    defaultTemplatePath: '/anodoo_website/static/src/xml/website_form.xml',
    fields: [{
        name: 'type',
        type: 'char',
        required: true,
        string: '业务类型',
    }],
});

});
