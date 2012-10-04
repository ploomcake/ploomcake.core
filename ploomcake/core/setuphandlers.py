#!/usr/bin/env python
# Authors: Andrea D'Este <andrea.deste@ploomcake.com> and contributors (see docs/CONTRIBUTORS.txt)
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from Products.CMFPlone.interfaces import INonInstallable as INonInstallableProfile
from zope.interface import implements

class HiddenProducts(object):
    implements(INonInstallable)

    def getNonInstallableProducts(self):
        return ['ploomcake.core']

class HiddenProfiles(object):
    implements(INonInstallableProfile)

    def getNonInstallableProfiles(self):
        return ['ploomcake.core:default','ploomcake.core:website','ploomcake.core:collaboration portal']

import transaction
from Products.CMFCore.utils import getToolByName

from ZODB.POSException import ConflictError


def setupWebsite(context):
    if context.readDataFile('ploomcake.core.website_various.txt') is None:
        return
    site = context.getSite()
    # create the language folders
    view = site.restrictedTraverse('@@language-setup-folders')
    transaction.savepoint()
    try:
        view(forceOneLanguage=True)
    except ConflictError:
        raise
    except Exception, e:
        transaction.rollback()


def setupCollaboration_portal(context):
    if context.readDataFile('ploomcake.core.collaboration_portal_various.txt') is None:
        return

def setupIntranet(context):
    if context.readDataFile('ploomcake.core.intranet_various.txt') is None:
        return


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    # create the language folders

    if context.readDataFile('ploomcake.core.default_various.txt') is None:
        return
    # Add additional setup code here
    site = context.getSite()
    #fixing the purgepolicy issue:
    #http://stackoverflow.com/questions/9683466/purging-all-old-cmfeditions-versions/9684696#9684696)
    site.portal_purgepolicy.maxNumberOfVersionsToKeep = 4

    css_to_release = ['++resource++quickupload_static/uploadify.css',
                      '++resource++quickupload_static/fileuploader.css']
    ctool = getToolByName(site, 'portal_css')
    resources_to_release = [ctool.getResource(css) for css in css_to_release if css in ctool.getResourceIds()]
    for resource in resources_to_release:
        resource.setAuthenticated(False)

    js_to_release = ['++resource++quickupload_static/swfobject.js',
                     '++resource++quickupload_static/jquery.uploadify.js',
                     '++resource++quickupload_static/fileuploader.js',
                     '++resource++quickupload_static/helpers.js']
    jtool = getToolByName(site, 'portal_javascripts')
    resources_to_release = [jtool.getResource(js) for js in js_to_release if js in jtool.getResourceIds()]
    for resource in resources_to_release:
        resource.setAuthenticated(False)

    
