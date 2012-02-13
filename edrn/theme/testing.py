# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting, PLONE_FIXTURE
from plone.testing import z2

class EDRNTheme(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import edrn.theme
        self.loadZCML(package=edrn.theme)
        z2.installProduct(app, 'edrn.theme')
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'edrn.theme:default')
    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'edrn.theme')
        
EDRN_THEME = EDRNTheme()
EDRN_THEME_INTEGRATION_TESTING = IntegrationTesting(bases=(EDRN_THEME,), name='EDRNTheme:Integration')
EDRN_THEME_FUNCTIONAL_TESTING = FunctionalTesting(bases=(EDRN_THEME,), name='EDRNTheme:Functional')
