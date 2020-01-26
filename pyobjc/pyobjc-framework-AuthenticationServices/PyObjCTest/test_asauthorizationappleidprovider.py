from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASAuthorizationAppleIDProvider(TestCase):
    def test_constants(self):
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDProviderCredentialRevoked, 0
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDProviderCredentialAuthorized, 1
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDProviderCredentialNotFound, 2
        )
        self.assertEqual(
            AuthenticationServices.ASAuthorizationAppleIDProviderCredentialTransferred,
            3,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationAppleIDProvider.getCredentialStateForUserID_completion_,
            1,
            b"v" + objc._C_NSInteger + b"@",
        )
