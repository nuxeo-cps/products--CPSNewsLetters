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

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGlobalInstall))
    return suite
