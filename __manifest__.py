# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernandez
#    (<http://www.falconsolutions.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Export MFH',
    'version': '10.0.0.1.0',
    'author': "Falcón Solutions, Marlon Falcón, Alexander Rodriguez",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Settings',
    'summary': 'Reportes Personalizados Localización Chilena',
    'depends': ['l10n_cl_base'],
    'description': """
Reportes 
=====================================================

        """,
    'data': [
        'wizard/export_file_view.xml',
    ],
    'qweb': [''],
    'external_dependencies': {
        'python': [],
     },
    'installable': True,
    'auto_install': False,
    'demo': [],
    'test': [],
}
