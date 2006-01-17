import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

import unittest
import CPSNewsLettersTestCase

from Products.CMFCore.utils import getToolByName

class TestGlobalInstall(CPSNewsLettersTestCase.CPSNewsLettersTestCase):

    def testNewsLetterTypeFixtures(self):
        # Test if the NewsLetter portal_type is well installed
        ttool = self.portal.portal_types
        self.assert_('NewsLetter' in ttool.objectIds())

    # XXX disabled, as it seems the subscriptions tool doesn't read
    # any XML config anyway...
    def XXXtestSubscriptionsToolFixtures(self):
        # Test if CPSNewsLetters has register all the compulsory parameters
        # within portal_subscriptions
        # If portal_subscriptions is not installed then we juste skip the tests
        # since it's possible to use the CPSNewsLetters without this component

        subscriptions_tool = getToolByName(self.portal, 'portal_subscriptions')

        if subscriptions_tool is not None:
            self.assertEqual('workflow_newsletter_sendmail' in subscriptions_tool.getRenderedEvents(), 1)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGlobalInstall))
    return suite
