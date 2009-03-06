# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from plone.theme.interfaces import IDefaultPloneLayer
from zope.viewlet.interfaces import IViewletManager

class IThemeSpecific(IDefaultPloneLayer):
    '''Marker interface that defines a Zope 3 browser layer.'''
    

class INCITopmostManager(IViewletManager):
    '''A viewlet manager that enables NCI to display their bright red long-stretching banner.'''
    
