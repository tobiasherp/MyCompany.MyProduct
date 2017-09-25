# -*- coding: utf-8 -*-
# Organisatorisches:
__author__ = """Tobias Herp <tobias.herp@stein.de>"""
__docformat__ = 'plaintext'
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

# Sonstiges (Plone):
from Products.CMFCore.utils import getToolByName

from .config import PROJECTNAME

# Logging:
import logging
# ------------------------------------------------------ [ Daten ... [
# UNITRACC_PORTAL_TYPES_1000 = UNITRACC_PORTAL_TYPES[:17]

PROFILE_ID = PROJECTNAME + ':default'
LOGGER_LABEL = PROJECTNAME + ': setuphandlers'
# ------------------------------------------------------ ] ... Daten ]

logger = logging.getLogger(LOGGER_LABEL)


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'MyCompany.MyProduct:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


# ------------------------ [  Upgrade steps, ./profiles.zcml ... [
def update_site_structure_1001(context, logger=logger):
    """
    New groups, roles and pages
    """
    if logger is None:
        logger = logging.getLogger(LOGGER_LABEL)
    try:
        site = context.getSite()
    except AttributeError:
        site = getToolByName(context, 'portal_url')
    # ... functionality deleted.
# ------------------------ ] ...  Upgrade steps, ./profiles.zcml ]
