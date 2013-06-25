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

from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import applyProfile

from ploomcake.core.config import PROJECTNAME

class CoreLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import ploomcake.core
        import Products.LinguaPlone
        import Products.PloneFormGen
        import redomino.contentwellportlets
        import collective.quickupload
        import plone.formwidget.captcha
        import redomino.cache
        import redomino.css3theme
        import redomino.tinymceplugins.snippet
        import plone.app.caching

        self.loadZCML(package=Products.LinguaPlone)
        self.loadZCML(package=plone.app.caching)
        self.loadZCML(package=Products.PloneFormGen)
        self.loadZCML(package=redomino.contentwellportlets)
        self.loadZCML(package=collective.quickupload)
        self.loadZCML(package=plone.formwidget.captcha)
        self.loadZCML(package=redomino.cache)
        self.loadZCML(package=redomino.css3theme)
        self.loadZCML(package=redomino.tinymceplugins.snippet)
        self.loadZCML(package=ploomcake.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploomcake.core:default')


CORE_FIXTURE = CoreLayer()

# Note: the layer name must be unique
CORE_INTEGRATION_TESTING = IntegrationTesting(bases=(CORE_FIXTURE,), name='%s:Integration' % PROJECTNAME)
CORE_FUNCTIONAL_TESTING = FunctionalTesting(bases=(CORE_FIXTURE,), name='%s:Functional' % PROJECTNAME)

def browser_login(portal, browser, username=None, password=None):
    """ An utility method to perform login in functional tests """
    handleErrors = browser.handleErrors
    try:
        browser.handleErrors = False
        browser.open(portal.absolute_url() + '/login_form')
        if username is None:
            username = TEST_USER_NAME
        if password is None:
            password = TEST_USER_PASSWORD
        browser.getControl(name='__ac_name').value = username
        browser.getControl(name='__ac_password').value = password
        browser.getControl(name='submit').click()
    finally:
        browser.handleErrors = handleErrors
