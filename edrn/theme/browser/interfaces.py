# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme
from zope.viewlet.interfaces import IViewletManager

class IThemeSpecific(IClassicTheme):
    '''Marker interface that defines a Zope 3 browser layer.'''
    

class INCITopmostManager(IViewletManager):
    '''A viewlet manager that enables NCI to display their bright red long-stretching banner.'''
    
