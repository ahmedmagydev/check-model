from odoo import fields, models,api
from datetime import datetime



class Checkcustomer(models.Model):
    _name = 'check.customer'
    _description='Check Customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name=fields.Many2one("res.partner" ,string="Customer" ,required=True)
    start_date=fields.Date(required=True)
    end_date=fields.Datetime(required=True)
    check=fields.Selection([("check_in","CheckIn"),("check_out","CheckOut")])
    state=fields.Selection([("draft","Draft"),("finish","Finish")], default='draft')
    description=fields.Html()
    
        
        #    button
    def action_draft(self):
        
        
        self.state="draft"
        self.check="check_in"
        
    # def action_finish(self):
        
        
    #     self.state="finish"
    #     self.check="check_out"
            
        # elif self.check=="check_out":
        #     self.state="finish"
        
        
        
    @api.onchange("check")
    def onchange_check(self):
        if self.check=='check_out':
            self.state="finish"
    
    
    @api.onchange("end_date")
    def onchange_end_date(self):
        if self.end_date and datetime.now() > fields.Datetime.from_string(self.end_date):
            self.check = "check_out"
            self.state = "finish"