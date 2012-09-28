import doctest

import unittest2 as unittest

from plone.testing import layered
from plone.app import testing
from ploomcake.core.testing import CORE_FUNCTIONAL_TESTING

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
normal_testfiles = [
    'viewlet.txt',
]



def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     ),
                layer=CORE_FUNCTIONAL_TESTING)
        for test in normal_testfiles])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
