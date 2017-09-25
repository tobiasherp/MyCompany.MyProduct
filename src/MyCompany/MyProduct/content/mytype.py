# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from ..interfaces import IMyType

from ..config import PROJECTNAME

##code-section module-header #fill in your manual code here
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.base import registerATCT as registerType
# from Products.Archetypes.interfaces import ISchema

# from Products.Archetypes.atapi import AnnotationStorage
# from Products.validation import V_REQUIRED
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MyType_schema = (
    ATContentTypeSchema.copy()
    # + schema.copy()
    )


basecls = (# MyBase,   # (add later, after solution for factory problem)
           ATCTContent,
           )
class MyType(*basecls):
    """
    My content type which appears in the types tool,
    but currently can't be added
    """
    security = ClassSecurityInfo()

    implements(IMyType)

    meta_type = 'MyType'
    _at_rename_after_creation = True

    schema = MyType_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

# set_trace()
registerType(MyType, PROJECTNAME)
# end of class UnitraccFile

##code-section module-footer #fill in your manual code here
##/code-section module-footer
