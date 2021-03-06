__author__ = 'ironeagle'

import os

from django.views.generic.base import TemplateView
from django.conf.urls import url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_HTML_PATH = os.path.join(BASE_DIR, "aetos_material/templates/core/docs/")

file_names = []
for (os_dir_path, os_dir_names, os_file_names) in os.walk(DOCS_HTML_PATH):
    file_names.extend(os_file_names)
    break

material_design_docs = [
    url(r'^docs/%s$' % file_name, TemplateView.as_view(template_name='core/docs/%s' % file_name),
        name="core-docs-%s" % file_name.split('.')[0])
    for file_name in file_names
]

urlpatterns = [
    url(r'^docs/$', TemplateView.as_view(template_name='core/docs/index.html'), name="core-docs-home"),
] + material_design_docs