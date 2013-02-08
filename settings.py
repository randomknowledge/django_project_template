# coding=utf-8
from {{ project_name }}.conf.dev import *

try:
    from settings_local import *
except ImportError:
    pass
