from Testing import ZopeTestCase
from Products.ExternalMethod.ExternalMethod import ExternalMethod

from Products.CPSDefault.tests import CPSTestCase

ZopeTestCase.installProduct('CPSNewsLetters')

CPSNewsLettersTestCase = CPSTestCase.CPSTestCase

class CPSNewsLettersInstaller(CPSTestCase.CPSInstaller):
    def addPortal(self, id):
        """Override the Default addPortal method installing
        a Default CPS Site.

        Will launch the external method for CPSNewsLetters too.
        """

        # CPS Default Site
        factory = self.app.manage_addProduct['CPSDefault']
        factory.manage_addCPSDefaultSite(id,
                                         root_password1="passwd",
                                         root_password2="passwd",
                                         langs_list=['fr', 'en'])

        portal = getattr(self.app, id)

        # Install the CPSNewsLetters product
        cpsnewsletters_installer = ExternalMethod('cpnewsletters_installer',
                                                    '',
                                                    'CPSNewsLetters.install',
                                                    'install')
        portal._setObject('cpsnewsletters_installer', cpsnewsletters_installer)
        portal.cpsnewsletters_installer()

CPSTestCase.setupPortal(PortalInstaller=CPSNewsLettersInstaller)
