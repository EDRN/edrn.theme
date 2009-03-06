# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EDRN Theme: test harness base classes.'''

from Globals import package_home
from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Testing import ZopeTestCase as ztc
from zope.component import provideUtility
from zope.interface import implements

PACKAGE_HOME = package_home(globals())

# Traditional Products we have to load manually for test cases:
# (none at this time)

@onsetup
def setupEDRNTheme():
    '''Set up additional products required for EDRN Theme.'''
    fiveconfigure.debug_mode = True
    import edrn.theme
    zcml.load_config('configure.zcml', edrn.theme)
    fiveconfigure.debug_mode = False
    ztc.installPackage('edrn.theme')

setupEDRNTheme()
ptc.setupPloneSite(products=['edrn.theme'])

class EDRNThemeTestCase(ptc.PloneTestCase):
    '''Base for unit tests in this package.'''
    pass
    

class EDRNThemeFunctionalTestCase(ptc.FunctionalTestCase):
    '''Base class for functional (doc-)tests.'''
    pass
    


