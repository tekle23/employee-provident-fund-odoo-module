
{
    'name': "Ethiopian provident Fund",
    'version': "16.0.0.1",
    'summary': """ Ethiopian employee provident fund""",
    'description': """Depost from bEthiopian employee provident fund""",
    'author': "Tekle YItayew",
    'company': "Odoo Ethiopia",
    'category': 'Human resource',
    'depends': ['base_setup','hr','om_hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'security/users_grups.xml',
        'data/mail_template_data.xml',
        'data/activity.xml',
        'report/provident_fund.xml',
        'views/res_config/res_config_settings_view.xml',
        'views/provident_fund/provident_fund.xml',
        'views/provident_fund/balance.xml',
        'views/provident_fund/deposits.xml',
        'views/pad_custom_header_layout.xml'
        
    ],

    'license': "AGPL-3",
    'installable': True,
    'application': True,
    'images': ['static/description/banner.jpg'],
}
