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
from zope.interface import Interface, implements
from ploomcake.core import _

class IPloomCakeCake(Interface):
    """... """
    def getProfile():
        """profile name"""
    def getTitle():
        """profile title"""
    def getDescription():
        """profile description"""


class PloomCakeWebsiteCake(object):
    implements(IPloomCakeCake)

    def getProfile(self):
        return u"ploomcake.core:website"
    def getTitle(self):
        return "PloomCake Website"
    def getDescription(self):
        return _("ploomcake_website_desc",default="Install this for public facing websites")

class PloomCakeCollabPortalCake(object):
    implements(IPloomCakeCake)

    def getProfile(self):
        return u"ploomcake.core:collaboration portal"
    def getTitle(self):
        return u"PloomCake Collaboration Portal"
    def getDescription(self):
        return _("ploomcake_collab_desc", default="Install this for mixed intranet/internet websites")


