from odoo import models, fields


class open_reservations(models.Model):
	"""docstring for open_reservations"""

	_name = "o2clinic.open.reservations"
	doctor_id = fields.Many2one('o2clinic.doctors' , string="Doctor Name")
	start_time = fields.Float(string='Start Time')
	end_time =  fields.Float(string='End Time')

    
class nationality(models.Model):
	"""docstring for nationality"""

	_name = "o2clinic.nationality"
	name = fields.Char(string="name", required=True)

class workdays(models.Model):
	"""docstring for workdays"""

	_name = "o2clinic.workdays"
	name = fields.Char(string="name", required=True)







