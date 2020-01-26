import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKOverlayPathRenderer(TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKOverlayPathRenderer, objc.objc_class)

        @min_os_level("10.15")
        def test_methods(self):
            self.assertResultIsBOOL(MapKit.MKOverlayPathRenderer.shouldRasterize)
            self.assertArgIsBOOL(MapKit.MKOverlayPathRenderer.setShouldRasterize_, 0)


if __name__ == "__main__":
    main()
