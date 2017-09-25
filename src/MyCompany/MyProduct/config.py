# -*- coding: utf-8 -*-

# ACHTUNG
# ~~~~~~~
# Die Permission-Rollen-Zuordnungen hier sind nur wirksam für die
# Rollen, die auch im Zope-Root-Verzeichnis existieren, also für die
# Zope-Standardrollen Manager und Owner.  Ansonsten 'leben' die
# Zuordnungen in der ZODB und müssen daselbst geändert werden!
# Die Zuweisung einer Permission hier *nur* an die Rolle 'Manager'
# bedeutet also *nicht* (!), daß sie nur für Manager gedacht ist;
# letztlich soll so wenig wie nur irgend möglich an der Rolle Manager
# bzw. entsprechenden Universalpermissions hängen.

# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
from os import sep

from .permissions import (AddMyType,
        )

PROJECTNAME = "MyCompany.MyProduct"
PRODUCT_HOME = sep.join(__file__.split(sep)[:-1])

MANAGERS_ONLY = ('Manager',)
MANAGERS_AND_OWNER = ('Manager', 'Owner')

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, MANAGERS_AND_OWNER)
ADD_CONTENT_PERMISSIONS = {
    'MyType': AddMyType,
}
for perm in ADD_CONTENT_PERMISSIONS.values():
    setDefaultRoles(perm, MANAGERS_ONLY)
