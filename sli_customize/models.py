## -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, date, time,timedelta
from . import amount_to_text

import logging
_logger = logging.getLogger(__name__)

class xmartshremployee(models.Model):
	_inherit ='hr.employee'

	applicant_credit_ids = fields.One2many('applicant.credit','employee_id')
	applicant_historical_ids = fields.One2many('applicant.historical','employee_id')
	x_licencia_id = fields.Text(string='Número de licencia')
	tipo_licencia = fields.Text(string='Tipo de licencia')
	edad = fields.Integer(string="Edad", compute="_compute_days")

	_sql_constraints = [
		('barcode_uniq', 'unique(barcode)', 'El valor de "ID credencial" ya existe.'),
		('imss_uniq', 'unique(x_nss)', 'El numero del imss ya existe.'),
	]

	@api.model
	def create(self, vals):
		valor = self.env['ir.sequence'].next_by_code('sequence.employee')
		vals['barcode'] = valor
		return super(xmartshremployee,self).create(vals)

	@api.onchange('address_home_id')
	def orderwizardall_onchange(self):
		if self.address_home_id is not None:
			self.x_rfc_id = self.address_home_id.vat

	@api.one
	def _compute_days(self):
		if str(self.birthday) != 'False':
			# _logger.info(_("entrooooooooooo  \n\n \n%s") % (str(self.validity_date)))
			fecha = str(self.birthday) + ' 00:00:00'
			cumple = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S').date()
			_logger.info(_("cumple: \n\n \n%s") % (cumple))
			i = datetime.now()
			hoy = (str(i.year) + '-' + str(i.month, ) + '-' + str(i.day) + ' 00:00:00')
			fecha_hoy = datetime.strptime(hoy, '%Y-%m-%d %H:%M:%S').date()
			_logger.info(_("fecha hoy: \n\n \n%s") % (fecha_hoy))
			total = fecha_hoy - cumple
			years = str(int(total.days / 365))
			_logger.info(_("Edad: \n\n \n%s") % (years))
			self.edad = years

class hrcontract(models.Model):
    _inherit ='hr.contract'


    @api.one
    @api.depends('wage')
    def _get_amount_to_text(self):
        _logger.info(_("ENNTRO a monto texto "))
        self.amount_to_text = amount_to_text.get_amount_to_text(self, self.wage,'MXN')
    amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
                                 help='Amount of the invoice in letter')


class hrcontract_salary(models.Model):
	_inherit = 'hr.contract'

	@api.one
	def _compute_salary(self):
		self.salarioquin = self.wage * 15

	salarioquin = fields.Float(string='Salario quincenal', compute="_compute_salary")

	@api.one
	@api.depends('salarioquin')
	def _get_amount_to_text_salary(self):
		self.amount_to_text_salary = amount_to_text.get_amount_to_text(self, self.salarioquin, 'MXN')

	amount_to_text_salary = fields.Char(compute='_get_amount_to_text_salary', string="Salario quincenal en texto")

	sueldo_a_pagar = fields.Float(string='Sueldo integro a pagar')

	@api.one
	@api.depends('sueldo_a_pagar')
	def _get_amount_to_text_sueldo(self):
		self.amount_to_text_sueldo = amount_to_text.get_amount_to_text(self, self.sueldo_a_pagar, 'MXN')

	amount_to_text_sueldo = fields.Char(compute='_get_amount_to_text_sueldo', string="Sueldo a pagar en texto")

class newfieldhremployee(models.Model):
	_inherit = 'applicant.family'

	fechanacimiento = fields.Date(string='Fecha nacimiento')

class newfieldmedical(models.Model):
	_inherit = 'applicant.medical'

	fechaexamen = fields.Date(string='Fecha examen')


class newtabcredit(models.Model):
	_name = 'applicant.credit'
	_description = 'Applicant credit'

	referencecredit = fields.Char('Referencia de crédito')
	typecredit = fields.Selection([('infonavit', 'Infonavit'),('fonacot', 'Fonacot'),('escolar', 'Escolar')], string = 'Tipo de crédito')
	numbercredit = fields.Char('Folio de crédito')
	importinit = fields.Float('Importe inicial')
	state = fields.Selection([('abierto', 'Abierto'),('suspendido', 'Suspendido'),('cerrado', 'Cerrado')], string = 'Estado')
	employee_id = fields.Many2one(
		'hr.employee',
		string='Employee'
	)

class newtabhistorical(models.Model):
	_name = 'applicant.historical'
	_description = 'Applicant historical'

	organization_id = fields.Many2one(
		'res.company',
		string='Organizacion',
		required=True,
	)
	admissiondate = fields.Date('Fecha ingreso')
	dischargedate = fields.Date('Fecha de baja')
	settlement = fields.Boolean('Finiquito')
	employee_id = fields.Many2one(
		'hr.employee',
		string='Employee'
	)