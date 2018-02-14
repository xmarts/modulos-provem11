# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'HR Recruitment/Employee - Extended',
    'version' : '1.0',
    'price' : 20.0,
    'currency': 'EUR',
    'category': 'Human Resources',
    'license': 'Other proprietary',
    'description': """

HR Applicant and Employee with Education/Medical/Employment/Family Details.

Tags:
Applicant Education details
Applicant Family details
Applicant Employeement details
Applicant Medical Tests
Applicant Institutes
Applicant Organization
employee Education details
employee Employeement details
employee Employeement History
employee Medical Checkups
employee Institutes 
employeement History
employee Organization
employee Relations
employee university
applicant degree
employee degree
medical tests
medical examination
family data
employment details
past employment details
employee employment
mother father names
hr_applicant_recruitment
hr recruitment information
create employee recruitment
college study information
education
medical
family
company data

            """,
    'summary' : 'HR Applicant and Employee with Education/Medical/Employment/Family Details.',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
    'depends' : ['hr_recruitment'],
    'data' : [
              'data/applicant_relation_data.xml',
              'security/ir.model.access.csv',
              'views/applicant_recruitment_configuration.xml',
              'views/hr_recruitment_view.xml',
              'views/hr_views.xml',
              ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
