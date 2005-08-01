import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

import unittest
import CPSNewsLettersTestCase

from Products.CMFCore.utils import getToolByName

class TestNewsLetters(CPSNewsLettersTestCase.CPSNewsLettersTestCase):
    # Test object creation and publication workflow

    def afterSetUp(self):
        self.login('manager')
        self.wftool = getToolByName(self.portal, 'portal_workflow')

    def beforeTearDown(self):
        self.logout()

    # Test the renamming of a published object
    # Trac(#793)
    def testSubmitAndRename(self):
        type_name = 'NewsLetter'
        id_file = 'file'
        ws = self.portal.workspaces
        
        # Create a new File
        self.wftool.invokeFactoryFor(ws, type_name, id_file)
        proxy = getattr(ws, id_file)

        # Publish it
        proxy.content_status_modify(
            submit=['sections',],
            workflow_action='copy_submit')

        # Renamme
        sc = self.portal.sections
        new_id = 'id2'
        sc.manage_renameObjects([id_file], [new_id])

        # Check this
        self.assert_(new_id in sc.objectIds())
        self.assert_(id_file not in sc.objectIds())

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNewsLetters))
    return suite

if __name__ == '__main__':
    framework(descriptions=1, verbosity=2)

