{
    'name': 'Evaluación de Desempeño',
    'version': '1.0',
    'summary': 'Módulo para gestionar evaluaciones de desempeño de empleados',
    'category': 'Productivity',
    'author': 'Alejandro Lorenzo',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'icon': '/evaluacion_desempeno/static/description/icon53.png',
    'data': [
        'views/evaluacion_desempeno_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/evaluacion_desempeno/static/src/css/styles.css',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """
        Módulo de Odoo para la gestión de evaluaciones de desempeño de empleados,
        incluyendo vistas Kanban y formulario detallado.
    """,
}