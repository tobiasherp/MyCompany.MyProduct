# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import MyCompany.MyProduct


class MycompanyMyproductLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=MyCompany.MyProduct)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'MyCompany.MyProduct:default')


MYCOMPANY_MYPRODUCT_FIXTURE = MycompanyMyproductLayer()


MYCOMPANY_MYPRODUCT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MYCOMPANY_MYPRODUCT_FIXTURE,),
    name='MycompanyMyproductLayer:IntegrationTesting'
)


MYCOMPANY_MYPRODUCT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MYCOMPANY_MYPRODUCT_FIXTURE,),
    name='MycompanyMyproductLayer:FunctionalTesting'
)


MYCOMPANY_MYPRODUCT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MYCOMPANY_MYPRODUCT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MycompanyMyproductLayer:AcceptanceTesting'
)
