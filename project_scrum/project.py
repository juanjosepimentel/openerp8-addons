# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _

class projectProjectInehrit(osv.osv):
    _inherit = 'project.project'
    _columns = {
	'pb_stage_ids': fields.many2many('project.scrum.pb.stage', 'project_scrum_backlog_stage_rel', 'project_id', 'stage_id', 'Backlog Stages', states={'close':[('readonly',True)], 'cancelled':[('readonly',True)]}),
        'is_scrum': fields.boolean("Is it a Scrum Project ?"),
        'scrum_master_id': fields.many2one('res.users', 'Scrum Master', help="The person who is maintains the processes for the product"),
        'product_owner_id': fields.many2one('res.users', "Product Owner"),
        'goal' : fields.text("Goal", help="The document that includes the project, jointly between the team and the customer"),
    }

    def _get_stage_common(self, cr, uid, context):
        ids = self.pool.get('project.scrum.pb.stage').search(cr, uid, [('case_default','=',1)], context=context)
        return ids

    _defaults = {
        'is_scrum': True,
	'pb_stage_ids': _get_stage_common 
    }
