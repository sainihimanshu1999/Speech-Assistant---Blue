from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKGameModelHelper(GameplayKit.NSObject):
        def value(self):
            return 1

        def setValue_(self, v):
            pass

        def playerId(self):
            return 1

        def setPlayerId_(self, v):
            pass

        def scoreForPlayer_(self, p):
            return 1

        def isWinForPlayer_(self, p):
            return 1

        def isLossForPlayer_(self, p):
            return 1

    class TestGKGameModel(TestCase):
        def testConstants(self):
            self.assertEqual(GameplayKit.GKGameModelMaxScore, 1 << 24)
            self.assertEqual(GameplayKit.GKGameModelMinScore, -(1 << 24))

        def testMethods(self):
            self.assertResultHasType(TestGKGameModelHelper.value, objc._C_NSInteger)
            self.assertArgHasType(TestGKGameModelHelper.setValue_, 0, objc._C_NSInteger)

            self.assertResultHasType(TestGKGameModelHelper.playerId, objc._C_NSInteger)
            self.assertArgHasType(
                TestGKGameModelHelper.setPlayerId_, 0, objc._C_NSInteger
            )

            self.assertResultHasType(
                TestGKGameModelHelper.scoreForPlayer_, objc._C_NSInteger
            )
            self.assertResultIsBOOL(TestGKGameModelHelper.isWinForPlayer_)
            self.assertResultIsBOOL(TestGKGameModelHelper.isLossForPlayer_)

        def testProtocols(self):
            objc.protocolNamed("GKGameModelUpdate")
            objc.protocolNamed("GKGameModelPlayer")
            objc.protocolNamed("GKGameModel")


if __name__ == "__main__":
    main()
