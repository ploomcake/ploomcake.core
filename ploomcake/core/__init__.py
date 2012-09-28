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

from Products.LinguaPlone.browser.controlpanel import MultiLanguageControlPanelAdapter
from zope.component import getMultiAdapter
from zope.i18n import MessageFactory
from ploomcake.core.config import PROJECTNAME

_ = MessageFactory(PROJECTNAME)

#monkeypatch
def set_available_languages(self, value):
    site = getMultiAdapter((self.context, self.context.REQUEST), name=u"plone_portal_state").portal()
    languages = [str(l) for l in value]
    self.context.supported_langs = languages
    view = site.restrictedTraverse('@@language-setup-folders')
    view(forceOneLanguage=True)

MultiLanguageControlPanelAdapter.set_available_languages = set_available_languages

MultiLanguageControlPanelAdapter.available_languages = property(MultiLanguageControlPanelAdapter.get_available_languages,
                                                                MultiLanguageControlPanelAdapter.set_available_languages)



