from odoo import models, fields , api



class doctors(models.Model):

   _name = "o2clinic.doctors"
   # _inherit = 'hr.employee'
   
   name = fields.Char(string="Doctor name", required=True )
   emp_id = fields.Many2one('res.partner', string='Employee  Name')
   en_name = fields.Char(string="Doctor En name" )
   birthday = fields.Date(string="birthday")
   address = fields.Char(string="address")
   phone = fields.Char(string="phone")
   mobile = fields.Char(string="mobile")
   email = fields.Char(string="email")
   specialist_id = fields.Many2one('o2clinic.specialists' , string="specialist")
   specialist_for = fields.Text(string="specialist_for")
   certificates = fields.Text(string="certificates")
   clinic_id = fields.Many2one('o2clinic.clinics' , string="Clinic Name")
   
   image = fields.Binary()
   gender = fields.Selection(selection=[('male', 'Male'),('female', 'Female')])
   workdays = fields.Many2many("o2clinic.workdays","doctor_workdays_rel", "doctor_id", "day_id",string="workdays")
   available = fields.Boolean(default=True)
   waiting_time = fields.Integer()
   active = fields.Boolean(default=True)
   count_book = fields.Integer(compute='calculate_pending_book');
   next_book = fields.Integer(compute='calculate_next_book')
   next_book_num = fields.Integer(compute='calculate_next_book_num')
   photo = fields.Binary()
   middle=fields.Char(required=True)
   last =fields.Char(required=True)
   nationality = fields.Many2one('o2clinic.nationality', string="nationality")
   ID_Number = fields.Char(string="ID Number")
   street = fields.Char(string="street")  
   city = fields.Char(string="city")
   country_id=fields.Char(string="country")
   date_of_birth=fields.Date()
   age=fields.Char(string="age")
   mother_tongue= fields.Selection(selection=[('arbic', 'arabic'), ('english', 'english')])
   hiring_date=fields.Date()
   maritual_status=fields.Selection(selection=[('single', 'single'), ('married', 'married')])
   contact_phone1=fields.Char(string="phone1")
   contact_mobile1=fields.Char(string="mobile1")
   university=fields.Char(string="university")
   graduation_date=fields.Date()
   dgree=fields.Selection(selection=[('A', 'A'), ('B', 'B')])

 

   @api.depends()
   def calculate_next_book(self):
       
      for data in self:
         if data.waiting_time or data.count_book:
            next_book =  (data.count_book * data.waiting_time)
            data.next_book = next_book





   @api.depends()
   def calculate_pending_book(self):
       
      for data in self:
         if data.id:
          pending_book = self.env['o2clinic.appoinements'].search_count([['state', '=', 'confirmed'], ['doctor_id', '=', data.id]])
        
          data.count_book = pending_book



   @api.depends()
   def calculate_next_book_num(self):
       
      for data in self:
         if data.id:
          pending_book = self.env['o2clinic.appoinements'].search([['state', '=', 'confirmed'], ['doctor_id', '=', data.id]], limit=1).id
         
          data.next_book_num = pending_book



   @api.multi         
   def make_appoinement(self):

    doctor_id = self.id
    doctor_name = self.name

    return {
        'name': ('Make New Appoinement | Dr .', doctor_name),
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'o2clinic.appoinements',
        'view_id': False,
        'type': 'ir.actions.act_window',
        'target':'new',
        'context': {'doctor_id': doctor_id,'patient_gender':'male'}
    } 

