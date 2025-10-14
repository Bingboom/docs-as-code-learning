
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'AT Command Manual'
author = 'Your Name'
release = '1.0'

extensions = ['sphinx_idf_theme']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_idf_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

pdf_file = None
pdf_filename = None
pdf_url = None
idf_target_title_dict = {}
languages = ['zh_CN']

def setup(app):
    app.add_config_value('pdf_file', None, 'env')
    app.add_config_value('pdf_filename', None, 'env')
    app.add_config_value('pdf_url', None, 'env')
    app.add_config_value('idf_target_title_dict', {}, 'env')
#   app.add_config_value('languages', ['zh_CN'], 'env')
    app.add_css_file('custom.css')
