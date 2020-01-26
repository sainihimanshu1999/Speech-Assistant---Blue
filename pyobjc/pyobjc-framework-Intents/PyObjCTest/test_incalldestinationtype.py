import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINCallDestinationType(TestCase):
        @min_os_level("10.12")
        def testConstants(self):
            self.assertEqual(Intents.INCallDestinationTypeUnknown, 0)
            self.assertEqual(Intents.INCallDestinationTypeNormalDestination, 1)
            self.assertEqual(Intents.INCallDestinationTypeEmergencyDestination, 2)
            self.assertEqual(Intents.INCallDestinationTypeVoicemailDestination, 3)
            self.assertEqual(Intents.INCallDestinationTypeRedialDestination, 4)

            self.assertEqual(Intents.INCallDestinationTypeNormal, 1)
            self.assertEqual(Intents.INCallDestinationTypeEmergency, 2)
            self.assertEqual(Intents.INCallDestinationTypeVoicemail, 3)
            self.assertEqual(Intents.INCallDestinationTypeRedial, 4)


if __name__ == "__main__":
    main()
