import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from pprint import pprint
import unittest
from Testing import ZopeTestCase
import CPSNewsLettersTestCase
from Products.CMFCore.utils import getToolByName

class TestGlobalInstall(CPSNewsLettersTestCase.CPSNewsLettersTestCase):
    def afterSetUp(self):
        self.login('root')

    def beforeTearDown(self):
        self.logout()

    def testInstallerScript(self):
        # Check installation script
        from Products.ExternalMethod.ExternalMethod import ExternalMethod
        installer = ExternalMethod('installer',
            'CPS NewsLetters INSTALLER', 'CPSNewsLetters.install',
            'install')
        self.portal._setObject('installer', installer)
        self.portal.installer()

    def testNewsLetterTypeFixtures(self):
        # Test if the NewsLetter portal_type is well installed
        ttool = self.portal.portal_types
        self.assertEqual('NewsLetter' in ttool.objectIds(), 1)

    def testSubscriptionsToolFixtures(self):
        # Test if CPSNewsLetters has register all the compulsory parameters
        # within portal_subscriptions
        # If portal_subscriptions is not installed then we juste skip the tests
        # since it's possible to use the CPSNewsLetters without this component

        subscriptions_tool = getToolByName(self.portal, 'portal_subscriptions')

        if subscriptions_tool is not None:
            self.assertEqual('NewsLetter' in subscriptions_tool.getRenderedPortalTypes(), 1)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGlobalInstall))
    return suite
