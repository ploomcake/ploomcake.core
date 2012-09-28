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
from Products.CMFPlone.browser.navigation import CatalogNavigationTabs as BaseNavigation
from Products.CMFPlone import utils
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.root import getNavigationRoot


class CatalogNavigationTabs(BaseNavigation):

    def _getNavQuery(self):
        context = self.context
        navtree_properties = self.navtree_properties

        customQuery = getattr(context, 'getCustomNavQuery', False)
        if customQuery is not None and utils.safe_callable(customQuery):
            query = customQuery()
        else:
            query = {}

        portal = context.portal_url.getPortalObject()
        ltool = getToolByName(portal, 'portal_languages')
        lang = ltool.getPreferredLanguage()
        rootPath = lang in portal.objectIds() and "/".join(portal[lang].getPhysicalPath()) or getNavigationRoot(context)
        query['path'] = {'query': rootPath, 'depth': 1}

        blacklist = navtree_properties.getProperty('metaTypesNotToList', ()) 
        all_types = self.portal_catalog.uniqueValuesFor('portal_type')
        query['portal_type'] = [t for t in all_types if t not in blacklist]

        sortAttribute = navtree_properties.getProperty('sortAttribute', None)
        if sortAttribute is not None:
            query['sort_on'] = sortAttribute
            sortOrder = navtree_properties.getProperty('sortOrder', None)
            if sortOrder is not None:
                query['sort_order'] = sortOrder

        if navtree_properties.getProperty('enable_wf_state_filtering', False):
            query['review_state'] = navtree_properties.getProperty(
                                                    'wf_states_to_show', []) 

        query['is_default_page'] = False

        if self.site_properties.getProperty('disable_nonfolderish_sections',
                                            False):
            query['is_folderish'] = True

        return query
