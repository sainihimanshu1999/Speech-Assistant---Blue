from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLRequest(TestCase):
    def testConstants(self):
        self.assertEqual(NSURLRequestUseProtocolCachePolicy, 0)
        self.assertEqual(NSURLRequestReloadIgnoringLocalCacheData, 1)
        self.assertEqual(NSURLRequestReloadIgnoringLocalAndRemoteCacheData, 4)
        self.assertEqual(
            NSURLRequestReloadIgnoringCacheData,
            NSURLRequestReloadIgnoringLocalCacheData,
        )
        self.assertEqual(NSURLRequestReturnCacheDataElseLoad, 2)
        self.assertEqual(NSURLRequestReturnCacheDataDontLoad, 3)
        self.assertEqual(NSURLRequestReloadRevalidatingCacheData, 5)

        self.assertEqual(NSURLNetworkServiceTypeDefault, 0)
        self.assertEqual(NSURLNetworkServiceTypeVoIP, 1)
        self.assertEqual(NSURLNetworkServiceTypeVideo, 2)
        self.assertEqual(NSURLNetworkServiceTypeBackground, 3)
        self.assertEqual(NSURLNetworkServiceTypeVoice, 4)
        self.assertEqual(NSURLNetworkServiceTypeResponsiveData, 6)
        self.assertEqual(NSURLNetworkServiceTypeAVStreaming, 8)
        self.assertEqual(NSURLNetworkServiceTypeResponsiveAV, 9)
        self.assertEqual(NSURLNetworkServiceTypeCallSignaling, 11)

    def testMethods(self):
        self.assertResultIsBOOL(NSURLRequest.HTTPShouldHandleCookies)
        self.assertArgIsBOOL(NSMutableURLRequest.setHTTPShouldHandleCookies_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSURLRequest.HTTPShouldUsePipelining)
        self.assertArgIsBOOL(NSMutableURLRequest.setHTTPShouldUsePipelining_, 0)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSURLRequest.allowsCellularAccess)
        self.assertArgIsBOOL(NSMutableURLRequest.setAllowsCellularAccess_, 0)

        self.assertResultIsBOOL(NSURLRequest.supportsSecureCoding)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(NSURLRequest.allowsExpensiveNetworkAccess)
        self.assertArgIsBOOL(NSMutableURLRequest.setAllowsExpensiveNetworkAccess_, 0)
        self.assertResultIsBOOL(NSURLRequest.allowsConstrainedNetworkAccess)
        self.assertArgIsBOOL(NSMutableURLRequest.setAllowsConstrainedNetworkAccess_, 0)

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("NSURLSessionWebSocketDelegate")


if __name__ == "__main__":
    main()
