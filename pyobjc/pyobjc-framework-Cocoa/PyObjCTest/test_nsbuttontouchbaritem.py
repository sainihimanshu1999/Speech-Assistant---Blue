from PyObjCTools.TestSupport import *
import AppKit


class TestNSButtonTouchBarItem(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsSEL(
            AppKit.NSButtonTouchBarItem.buttonTouchBarItemWithIdentifier_title_target_action_,
            3,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSButtonTouchBarItem.buttonTouchBarItemWithIdentifier_image_target_action_,
            3,
            b"v@:@",
        )
        self.assertArgIsSEL(
            AppKit.NSButtonTouchBarItem.buttonTouchBarItemWithIdentifier_title_image_target_action_,
            4,
            b"v@:@",
        )


if __name__ == "__main__":
    main()
