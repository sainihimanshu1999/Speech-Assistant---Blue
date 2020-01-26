from PyObjCTools.TestSupport import *

import StoreKit


class TestSKArcadeService(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            StoreKit.SKArcadeService.registerArcadeAppWithRandomFromLib_randomFromLibLength_resultHandler_,
            2,
            b"v@I@I@",
        )

    @min_os_level("10.15")
    @expectedFailure
    def test_methods10_15_missing(self):
        self.assertArgIsBlock(
            StoreKit.SKArcadeService.arcadeSubscriptionStatusWithNonce_resultHandler_,
            2,
            b"v@I@I@",
        )


if __name__ == "__main__":
    main()
