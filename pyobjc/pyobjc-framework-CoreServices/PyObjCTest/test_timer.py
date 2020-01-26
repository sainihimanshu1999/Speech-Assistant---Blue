from PyObjCTools.TestSupport import *

import CoreServices


class TestTimer(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("Microseconds")
        self.assert_not_wrapped("kTMTaskActive")
        self.assert_not_wrapped("TMTask")
        self.assert_not_wrapped("InsTime")
        self.assert_not_wrapped("InsXTime")
        self.assert_not_wrapped("PrimeTime")
        self.assert_not_wrapped("RmvTime")
        self.assert_not_wrapped("InstallTimeTask")
        self.assert_not_wrapped("InstallXTimeTask")
        self.assert_not_wrapped("PrimeTimeTask")
        self.assert_not_wrapped("RemoveTimeTask")
        self.assert_not_wrapped("NewTimerUPP")
        self.assert_not_wrapped("DisposeTimerUPP")
        self.assert_not_wrapped("InvokeTimerUPP(")


if __name__ == "__main__":
    main()
