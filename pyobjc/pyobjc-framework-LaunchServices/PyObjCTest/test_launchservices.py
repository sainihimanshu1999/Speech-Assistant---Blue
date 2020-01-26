"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices


class TestLaunchServices(TestCase):
    def testValues(self):
        # Use this to test for a number of enum and #define values
        self.assertHasAttr(LaunchServices, "kLSRequestAllInfo")
        self.assertIsInstance(LaunchServices.kLSRequestAllInfo, (int, long))
        # Note: the header file seems to indicate otherwise but the value
        # really is a signed integer!
        self.assertEqual(LaunchServices.kLSRequestAllInfo, 0xFFFFFFFF)

        self.assertHasAttr(LaunchServices, "kLSLaunchInProgressErr")
        self.assertIsInstance(LaunchServices.kLSLaunchInProgressErr, (int, long))
        self.assertEqual(LaunchServices.kLSLaunchInProgressErr, -10818)

        self.assertHasAttr(LaunchServices, "kLSInvalidExtensionIndex")
        self.assertIsInstance(LaunchServices.kLSInvalidExtensionIndex, (int, long))

    def testVariables(self):
        self.assertHasAttr(LaunchServices, "kUTTypeItem")
        self.assertIsInstance(LaunchServices.kUTTypeItem, unicode)

        self.assertHasAttr(LaunchServices, "kUTTypeApplication")
        self.assertIsInstance(LaunchServices.kUTTypeApplication, unicode)

        self.assertHasAttr(LaunchServices, "kUTExportedTypeDeclarationsKey")
        self.assertIsInstance(LaunchServices.kUTExportedTypeDeclarationsKey, unicode)

    def testFunctions(self):
        self.assertHasAttr(LaunchServices, "UTTypeEqual")
        self.assertIsInstance(LaunchServices.UTTypeEqual, objc.function)

        self.assertHasAttr(LaunchServices, "UTCreateStringForOSType")
        self.assertIsInstance(LaunchServices.UTCreateStringForOSType, objc.function)

        self.assertHasAttr(LaunchServices, "LSSetDefaultHandlerForURLScheme")
        self.assertIsInstance(
            LaunchServices.LSSetDefaultHandlerForURLScheme, objc.function
        )

        self.assertHasAttr(LaunchServices, "_LSCopyAllApplicationURLs")
        self.assertIsInstance(LaunchServices._LSCopyAllApplicationURLs, objc.function)

        arr = LaunchServices._LSCopyAllApplicationURLs(None)
        self.assertIsInstance(arr, objc.lookUpClass("NSArray"))
        for a in arr:
            if str(a) == "file://localhost/Applications/Calculator.app/":
                break
            elif str(a) == "file:///Applications/Calculator.app/":
                break
            elif str(a) == "file:///System/Applications/Calculator.app/":
                break
        else:
            self.fail("No Calculator.app?")

        fn = LaunchServices.LSGetExtensionInfo
        self.assertEqual(fn(10, b"hello.text".decode("latin1"), None), (0, 6))
        self.assertEqual(fn(10, "hello.text", None), (0, 6))


if __name__ == "__main__":
    main()
