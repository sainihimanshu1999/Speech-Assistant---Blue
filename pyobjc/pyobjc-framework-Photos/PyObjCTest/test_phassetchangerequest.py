from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHAssetChangeRequest(TestCase):
        @min_os_level("10.15")
        def testMethods(self):
            self.assertResultIsBOOL(Photos.PHAssetChangeRequest.isFavorite)
            self.assertArgIsBOOL(Photos.PHAssetChangeRequest.setFavorite_, 0)

            self.assertResultIsBOOL(Photos.PHAssetChangeRequest.isHidden)
            self.assertArgIsBOOL(Photos.PHAssetChangeRequest.setHidden_, 0)

            self.assertResultIsBOOL(
                Photos.PHContentEditingInputRequestOptions.isNetworkAccessAllowed
            )
            self.assertArgIsBOOL(
                Photos.PHContentEditingInputRequestOptions.setNetworkAccessAllowed_, 0
            )

            self.assertResultIsBlock(
                Photos.PHContentEditingInputRequestOptions.progressHandler, b"vdo^Z"
            )
            self.assertArgIsBlock(
                Photos.PHContentEditingInputRequestOptions.setProgressHandler_,
                0,
                b"vdo^Z",
            )

            self.assertArgIsBlock(
                Photos.PHAsset.requestContentEditingInputWithOptions_completionHandler_,
                1,
                b"v@@",
            )

        @min_os_level("10.15")
        def test_constants(self):
            self.assertIsInstance(
                Photos.PHContentEditingInputResultIsInCloudKey, unicode
            )
            self.assertIsInstance(Photos.PHContentEditingInputCancelledKey, unicode)
            self.assertIsInstance(Photos.PHContentEditingInputErrorKey, unicode)


if __name__ == "__main__":
    main()
