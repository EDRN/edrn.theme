# encoding: utf-8
# Copyright 2010 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

PROFILE_ID = 'profile-edrn.theme:default'

def nullUpgradeStep(setupTool):
    '''A null step for when a profile upgrade requires no custom activity.'''

def upgrade4to5(setupTool):
    '''Upgrade 4 to 5 by updating skins and viewlets'''
    setupTool.runImportStepFromProfile(PROFILE_ID, 'skins')
    setupTool.runImportStepFromProfile(PROFILE_ID, 'viewlets')
