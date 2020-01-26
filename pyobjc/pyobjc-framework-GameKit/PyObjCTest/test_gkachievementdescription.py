from PyObjCTools.TestSupport import *

import GameKit


class TestGKAchievementDescriptionHelper(GameKit.GKAchievementDescription):
    def isHidden(self):
        return 1

    def isReplayable(self):
        return 1


class TestGKAchievementDescription(TestCase):
    def testMethods(self):
        self.assertArgIsBlock(
            GameKit.GKAchievementDescription.loadAchievementDescriptionsWithCompletionHandler_,
            0,
            b"v@@",
        )

        self.assertResultIsBOOL(TestGKAchievementDescriptionHelper.isHidden)
        self.assertResultIsBOOL(TestGKAchievementDescriptionHelper.isReplayable)

        self.assertArgIsBlock(
            GameKit.GKAchievementDescription.loadImageWithCompletionHandler_, 0, b"v@@"
        )


if __name__ == "__main__":
    main()
