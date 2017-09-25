# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
Berechtigungen
"""

__author__ = "Tobias Herp <tobias.herp@stein.de>"
VERSION = (0,
           4,  # Excerpt for github version
           )
__version__ = '.'.join(map(str, VERSION))

# 'Access contents information':
from Products.Sessions.SessionPermissions import ACCESS_CONTENTS_PERM as Access_contents_information

# BetonQuali:
AddMyType = 'MyCompany.MyProduct: Add MyType'
