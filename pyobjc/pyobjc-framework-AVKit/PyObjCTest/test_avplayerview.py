import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import AVKit

    class TestAVPlayerViewHelper(AVKit.NSObject):
        def playerView_restoreUserInterfaceForPictureInPictureStopWithCompletionHandler_(
            self, a, b
        ):
            pass

        def playerViewShouldAutomaticallyDismissAtPictureInPictureStart_(self, a):
            return 1

    class TestAVPlayerView(TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(AVKit.AVPlayerView, objc.objc_class)

        @min_os_level("10.9")
        def testMethods10_9(self):
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsFrameSteppingButtons_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsFrameSteppingButtons)
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsSharingServiceButton_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsSharingServiceButton)
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsFullScreenToggleButton_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsFullScreenToggleButton)
            self.assertResultIsBOOL(AVKit.AVPlayerView.canBeginTrimming)

            self.assertArgIsBlock(
                AVKit.AVPlayerView.beginTrimmingWithCompletionHandler_,
                0,
                b"v" + objc._C_NSInteger,
            )

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertResultIsBOOL(AVKit.AVPlayerView.isReadyForDisplay)

        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertArgIsBOOL(AVKit.AVPlayerView.setUpdatesNowPlayingInfoCenter_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.updatesNowPlayingInfoCenter)

        @min_os_level("10.15")
        def testMethods10_15(self):
            self.assertArgIsBOOL(AVKit.AVPlayerView.setShowsTimecodes_, 0)
            self.assertResultIsBOOL(AVKit.AVPlayerView.showsTimecodes)

            self.assertResultIsBOOL(AVKit.AVPlayerView.allowsPictureInPicturePlayback)
            self.assertArgIsBOOL(
                AVKit.AVPlayerView.setAllowsPictureInPicturePlayback_, 0
            )

            self.assertArgIsBlock(
                TestAVPlayerViewHelper.playerView_restoreUserInterfaceForPictureInPictureStopWithCompletionHandler_,
                1,
                b"vZ",
            )
            self.assertResultIsBOOL(
                TestAVPlayerViewHelper.playerViewShouldAutomaticallyDismissAtPictureInPictureStart_
            )

        @min_os_level("10.9")
        def test_constants(self):
            self.assertEqual(AVKit.AVPlayerViewControlsStyleNone, 0)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleInline, 1)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleFloating, 2)
            self.assertEqual(AVKit.AVPlayerViewControlsStyleMinimal, 3)
            self.assertEqual(
                AVKit.AVPlayerViewControlsStyleDefault,
                AVKit.AVPlayerViewControlsStyleInline,
                4,
            )

            self.assertEqual(AVKit.AVPlayerViewTrimOKButton, 0)
            self.assertEqual(AVKit.AVPlayerViewTrimCancelButton, 1)

        @min_sdk_level("10.15")
        def test_protocols(self):
            objc.protocolNamed("AVPlayerViewPictureInPictureDelegate")


if __name__ == "__main__":
    main()
