from PyObjCTools.TestSupport import *

import OSLog


class TestEntrySignpost(TestCase):
    def test_constants(self):
        self.assertEqual(OSLog.OSLogEntrySignpostTypeUndefined, 0)
        self.assertEqual(OSLog.OSLogEntrySignpostTypeIntervalBegin, 1)
        self.assertEqual(OSLog.OSLogEntrySignpostTypeIntervalEnd, 2)
        self.assertEqual(OSLog.OSLogEntrySignpostTypeEvent, 3)
