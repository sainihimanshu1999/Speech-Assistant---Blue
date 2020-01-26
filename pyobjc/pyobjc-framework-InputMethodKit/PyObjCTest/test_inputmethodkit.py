"""
Some simple tests to check that the framework is properly wrapped.
"""
from PyObjCTools.TestSupport import *
import objc
import InputMethodKit


class TestInputMethodKit(TestCase):
    def testClasses(self):

        self.assertHasAttr(InputMethodKit, "IMKInputController")
        self.assertIsInstance(InputMethodKit.IMKInputController, objc.objc_class)

        # 10.5
        self.assertHasAttr(InputMethodKit, "IMKCandidates")
        self.assertIsInstance(InputMethodKit.IMKCandidates, objc.objc_class)

    def testValues(self):
        self.assertHasAttr(InputMethodKit, "kIMKScrollingGridCandidatePanel")
        self.assertIsInstance(
            InputMethodKit.kIMKScrollingGridCandidatePanel, (int, long)
        )
        self.assertEqual(InputMethodKit.kIMKScrollingGridCandidatePanel, 2)

    def testVariables(self):
        self.assertHasAttr(InputMethodKit, "IMKCandidatesOpacityAttributeName")
        self.assertIsInstance(InputMethodKit.IMKCandidatesOpacityAttributeName, unicode)

    def testProtocols2(self):
        objc.protocolNamed("IMKMouseHandling")
        objc.protocolNamed("IMKStateSetting")


if __name__ == "__main__":
    main()
