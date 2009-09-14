# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase, LogoViewlet, SiteActionsViewlet, SearchBoxViewlet
from zope.component import getMultiAdapter

class NCIBar(ViewletBase):
    '''Red NCI bar viewlet.'''
    index = ViewPageTemplateFile('nci-bar.pt')
    

class EDRNSiteActions(SiteActionsViewlet):
    '''Site actions specific to EDRN.'''
    index = ViewPageTemplateFile('edrn-site-actions.pt')
    def update(self):
        super(EDRNSiteActions, self).update()
        contextState = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        self.siteActions = contextState.actions().get('edrn-actions', None)
    

class EDRNLogo(LogoViewlet):
    '''EDRN logo viewlet.'''
    index = ViewPageTemplateFile('edrn-logo.pt')

class EDRNSkinLogo(LogoViewlet):
    '''EDRN Skin logo viewlet.'''
    index = ViewPageTemplateFile('edrn-skin-logo.pt')
    
    
class EDRNFooter(ViewletBase):
    '''EDRN footer items viewlet.'''
    index = ViewPageTemplateFile('edrn-footer.pt')
    def update(self):
        super(EDRNFooter, self).update()
        contextState = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        self.siteActions = contextState.actions().get('site_actions', None)
    
class EDRNDefaultSiteSearchBox(SearchBoxViewlet):
    '''EDRN Default Site Search Box --upper right hand corner'''
    index = ViewPageTemplateFile('defaultSiteSearchBox.pt');
