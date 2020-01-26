import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKLocalSearchRequest(TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKLocalSearchRequest, objc.objc_class)

        def test_constants(self):
            self.assertEqual(MapKit.MKLocalSearchResultTypeAddress, 1 << 0)
            self.assertEqual(MapKit.MKLocalSearchResultTypePointOfInterest, 1 << 1)


if __name__ == "__main__":
    main()
