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
from setuptools import setup, find_packages
import os

version = '1.6'

setup(name='ploomcake.core',
      version=version,
      description="Ploomcake policy product",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author="Andrea D'Este",
      author_email='andrea.deste@redomino.com',
      url='https://github.com/ploomcake/ploomcake.core',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploomcake'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.PloneFormGen',
          'Products.ContentWellPortlets',
          'Products.LinguaPlone',
          'collective.quickupload',
          'plone.formwidget.captcha',
          'redomino.cache',
          'collective.portlet.embed',
          'ploomcake.theme',
          'redomino.seosupport',
          'redomino.tokenrole',
          'redomino.protectdelete'
      ],
      extras_require={
          'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
#      paster_plugins=[],
      )
