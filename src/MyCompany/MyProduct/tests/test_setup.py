# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from MyCompany.MyProduct.testing import MYCOMPANY_MYPRODUCT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that MyCompany.MyProduct is properly installed."""

    layer = MYCOMPANY_MYPRODUCT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if MyCompany.MyProduct is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'MyCompany.MyProduct'))

    def test_browserlayer(self):
        """Test that IMycompanyMyproductLayer is registered."""
        from MyCompany.MyProduct.interfaces import (
            IMycompanyMyproductLayer)
        from plone.browserlayer import utils
        self.assertIn(IMycompanyMyproductLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MYCOMPANY_MYPRODUCT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['MyCompany.MyProduct'])

    def test_product_uninstalled(self):
        """Test if MyCompany.MyProduct is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'MyCompany.MyProduct'))

    def test_browserlayer_removed(self):
        """Test that IMycompanyMyproductLayer is removed."""
        from MyCompany.MyProduct.interfaces import \
            IMycompanyMyproductLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMycompanyMyproductLayer, utils.registered_layers())
