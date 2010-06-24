# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Test the set up of the EDRN Theme.
'''

import unittest
from edrn.theme.tests.base import EDRNThemeTestCase
from zope.component import getUtility
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.viewlet.interfaces import IViewlet
from Products.CMFCore.utils import getToolByName

_themeName = u'EDRN Theme'

class TestSetup(EDRNThemeTestCase):
    '''Unit tests for the setup of the EDRN theme.'''
    
    def afterSetUp(self):
        self.storage = getUtility(IViewletSettingsStorage)

    def testActions(self):
        actions = getToolByName(self.portal, 'portal_actions')
        for name in ('home', 'sitemap', 'contact'):
            self.failUnless(name in actions.edrnActions)
        for name in ('home', 'contact', 'policies', 'accessibility', 'viewing', 'foia', 'sitemap', 'ncihome'):
            self.failUnless(name in actions.site_actions)
    
    def testCustomPortalTop(self):
        viewlets = list(self.storage.getOrder(u'plone.portaltop', _themeName))
        self.assertEquals(u'plone.header', viewlets[0], 'Plone header is not first in portaltop.')
        self.assertEquals(u'plone.personal_bar', viewlets[1], 'Plone personal bar is not second in portaltop.')
        self.assertEquals(u'plone.app.i18n.locales.languageselector', viewlets[2], 'Language selector is not third in portaltop.')
        hidden = self.storage.getHidden(u'plone.portaltop', _themeName)
        self.failUnless(u'plone.path_bar' in hidden, 'Plone path bar is not hidden in portaltop.')
    
    def testNCITopmostViewlet(self):
        viewlets = list(self.storage.getOrder(u'edrn.nci_topmost', _themeName))
        self.assertEquals(u'edrn.skip_links', viewlets[0], 'EDRN-derived skip links not first in NCI topmost viewlet.')
        self.assertEquals(u'edrn.nci_bar', viewlets[1], 'NCI bar not second in NCI topmost viewlet.')
    
    # Disable due to last-minute theme revamp; and this might all go away once we migrate to Deliverance (kelly/2010.6.24)
    # def testCustomPortalHeader(self):
    #     viewlets = list(self.storage.getOrder(u'plone.portalheader', _themeName))
    #     self.assertEquals(u'plone.searchbox', viewlets[0], 'Plone searchbox not first in portal header.')
    #     self.assertEquals(u'edrn.edrn_actions', viewlets[1], 'EDRN special actions not second in portal header.')
    #     self.assertEquals(u'edrn.logo', viewlets[2], 'EDRN logo not third in portal header.')
    #     self.assertEquals(u'plone.global_sections', viewlets[4], 'Plone global sections not fifth in portal header.')
    #     hidden = self.storage.getHidden(u'plone.portalheader', _themeName)
    #     self.failUnless(u'plone.site_actions' in hidden, 'Site actions are not hidden in the portal header.')
    #     self.failUnless(u'plone.logo' in hidden, 'The Plone logo is not hidden in the portal header.')
    
    def testCustomContentViews(self):
        viewlets = list(self.storage.getOrder(u'plone.contentviews', _themeName))
        self.assertEquals(u'edrn.path_bar', viewlets[0], 'EDRN-derived path bar not first in content views.')
        self.assertEquals(u'plone.contentviews', viewlets[1], 'Plone content views not second in content views.')
        self.assertEquals(u'plone.contentactions', viewlets[2], 'Plone content actions not third in content views.')

    def testCustomPortalFooter(self):
        viewlets = list(self.storage.getOrder(u'plone.portalfooter', _themeName))
        self.assertEquals(u'edrn.nci_footer', viewlets[0], 'EDRN footer not first in footer.')
        hidden = self.storage.getOrder(u'plone.portalfooter', _themeName)
        self.failUnless(u'plone.footer', 'Plone footer not hidden in footer viewlet.')
    
    def testViewletAvailability(self):
        from edrn.theme.browser.viewlets import NCIBar, EDRNSiteActions, EDRNLogo, EDRNFooter
        self.failUnless(IViewlet.implementedBy(NCIBar))
        self.failUnless(IViewlet.implementedBy(EDRNSiteActions))
        self.failUnless(IViewlet.implementedBy(EDRNLogo))
        self.failUnless(IViewlet.implementedBy(EDRNFooter))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
    
