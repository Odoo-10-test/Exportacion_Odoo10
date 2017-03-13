# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    $Id: account.py 1005 2005-07-25 08:41:42Z nicoe $
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
from datetime import datetime, date, time, timedelta
from odoo import api, fields, models
import base64
import csv
import StringIO
from odoo import http
import unicodedata
try:
    import xlwt
except ImportError:
    xlwt = None
import re
from cStringIO import StringIO

class wizard_receipt_txt(models.TransientModel):
    _name = 'wizard.file.generate'
    _description = 'Wizard that generate file.'

    date = fields.Date(string='Start')
    date_from = fields.Date(string='Desde')
    date_to = fields.Date(string='Hasta')
    


    def generate_file(self):
        #wzd_values = self.read(cr,uid,ids,context=context)[0]
        path = '/tmp/file_%s.csv'% (datetime.today())
        export_objs = self.env['economical.activities'].search([])
        
        fp = StringIO()
        with open(path, 'w') as csvfile:
            fieldnames = ['code', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        
            for line in export_objs:
                print line
                writer.writerow({'code':str(line.code), 'name': str(line.name.encode('utf-8').strip())})
        
        fp.close()
        csvfile.close()
        arch = open(path, 'r').read()
        data = base64.encodestring(arch)
        attach_vals = {
                 'name':'File%s.csv' % (datetime.today().strftime("%d-%m-%Y")),
                 'datas':data,
                 'datas_fname':'File#_%s.csv' % (datetime.today().strftime("%d-%m-%Y")),
                 }
        doc_id = self.env['ir.attachment'].create(attach_vals)
        return {
                    'type' : "ir.actions.act_url",
                    'url': "web/content/?model=ir.attachment&id="+str(doc_id.id)+"&filename_field=datas_fname&field=datas&download=true&filename="+str(doc_id.name),
                    'target': "self",
                    }


            
 #~ def from_data(self, fields, rows):
        #~ fp = StringIO()
        #~ writer = csv.writer(fp, quoting=csv.QUOTE_ALL)

        #~ writer.writerow([name.encode('utf-8') for name in fields])

        #~ for data in rows:
            #~ row = []
            #~ for d in data:
                #~ if isinstance(d, basestring):
                    #~ d = d.replace('\n',' ').replace('\t',' ')
                    #~ try:
                        #~ d = d.encode('utf-8')
                    #~ except UnicodeError:
                        #~ pass
                #~ if d is False: d = None
                #~ row.append(d)
            #~ writer.writerow(row)

        #~ fp.seek(0)
        #~ data = fp.read()
        #~ fp.close()
        #~ return data


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
