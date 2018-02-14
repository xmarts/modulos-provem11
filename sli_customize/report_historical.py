from odoo import api, fields, models
from odoo.tools.sql import drop_view_if_exists


class ReportStockLinesDate(models.Model):
    _name = "sli.historical.employee"
    _description = "Reporte de Historial de empleados"
    _auto = False

    id = fields.Integer('Id', readonly=True)
    nombre = fields.Char('Nombre', readonly=True)
    fechaingreso = fields.Date('Fecha de ingreso', readonly=True)
    fechabaja = fields.Date('fecha de baja', readonly=True)
    motivo = fields.Char('Motivo de baja', readonly=True)
    finiquito = fields.Boolean('Finiquito', readonly=True)
    recontratado = fields.Boolean('Recontratado', readonly=True)

    @api.model_cr
    def init(self):
        drop_view_if_exists(self._cr, 'sli_historical_employee')
        self._cr.execute("""
            create or replace view  sli_historical_employee as(
            select he.id as id,name_related as nombre, ah.admissiondate as fechaingreso,ah.dischargedate as fechabaja,
            ah.reason as motivo, ah.settlement as finiquito, ah.retracted as recontratado
            from hr_employee he
            left join applicant_historical ah on ah.employee_id = he.id
        )""")