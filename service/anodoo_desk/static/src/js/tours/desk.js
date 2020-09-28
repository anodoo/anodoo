odoo.define('desk.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register('desk_tour', {
    url: "/web",
}, [{
    trigger: '.o_app[data-menu-xmlid="desk_menu_root_anodoo"]',
    content: _t('Want to <b>boost your customer satisfaction</b>?<br/><i>Click Desk to start.</i>'),
    position: 'bottom',
}, {
    trigger: '.oe_kanban_action_button',
    extra_trigger: '.o_kanban_primary_left',
    content: _t('Click here to view this team\'s tickets.'),
    position: 'bottom',
    width: 200,
}, {
    trigger: '.o-kanban-button-new',
    extra_trigger: '.o_kanban_desk_ticket',
    content: _t('Let\'s create your first ticket.'),
    position: 'bottom',
    width: 200,
}, {
    trigger: 'input.field_name',
    extra_trigger: '.o_form_editable',
    content: _t('Enter a subject or title for this ticket.<br/><i>(e.g. Problem with installation, Wrong order, Can\'t understand bill, etc.)</i>'),
    position: 'right',
}, {
    trigger: '.o_field_widget.field_partner_id',
    extra_trigger: '.o_form_editable',
    content: _t('Enter the customer. Feel free to create it on the fly.'),
    position: 'top',
}, {
    trigger: '.o_field_widget.field_user_id',
    extra_trigger: '.o_form_editable',
    content: _t('Assign the ticket to someone.'),
    position: 'right',
}, {
    trigger: '.o_form_button_save',
    content: _t('Save this ticket and the modifications you\'ve made to it.'),
    position: 'bottom',
}, {
    trigger: '.o_back_button',
    extra_trigger: '.o_form_view.o_form_readonly',
    content: _t('Use the breadcrumbs to go back to the Kanban view.'),
    position: 'bottom',
}, {
    trigger: '.o_kanban_record',
    content: _t('Click these cards to open their form view, or <b>drag &amp; drop</b> them through the different stages of this team.'),
    position: 'right',
    run: "drag_and_drop .o_kanban_group:eq(2) ",
}, {
    trigger: '.o_priority',
    extra_trigger: '.o_kanban_record',
    content: _t('<b>Stars</b> mark the <b>ticket priority</b>. You can change it directly from here!'),
    position: 'bottom',
    run: "drag_and_drop .o_kanban_group:eq(2) ",
}, {
    trigger: ".o_column_quick_create .o_quick_create_folded",
    content: _t('Add columns to configure <b>stages for your tickets</b>.<br/><i>e.g. Awaiting Customer Feedback, Customer Followup, ...</i>'),
    position: 'right',
}
// TODO: Restore this step
// , {
//     trigger: '.dropdown-toggle[data-menu-xmlid="desk_menu_config"]',
//     content: _t('Click here and select "Desk Teams" for further configuration.'),
//     position: 'bottom',
// }
]);

});
