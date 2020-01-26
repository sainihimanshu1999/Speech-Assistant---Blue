from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHFetchResult(TestCase):
        @min_os_level("10.13")
        def testMethods(self):
            self.assertResultIsBOOL(Photos.PHFetchResult.containsObject_)
            self.assertArgIsBlock(
                Photos.PHFetchResult.enumerateObjectsUsingBlock_,
                0,
                b"v@" + objc._C_NSUInteger + b"o^Z",
            )
            self.assertArgIsBlock(
                Photos.PHFetchResult.enumerateObjectsWithOptions_usingBlock_,
                1,
                b"v@" + objc._C_NSUInteger + b"o^Z",
            )
            self.assertArgIsBlock(
                Photos.PHFetchResult.enumerateObjectsAtIndexes_options_usingBlock_,
                2,
                b"v@" + objc._C_NSUInteger + b"o^Z",
            )


if __name__ == "__main__":
    main()
