from PyObjCTools.TestSupport import *
from CoreData import *


class TestNSAttributeDescription(TestCase):
    def testConstants(self):
        self.assertEqual(NSUndefinedAttributeType, 0)
        self.assertEqual(NSInteger16AttributeType, 100)
        self.assertEqual(NSInteger32AttributeType, 200)
        self.assertEqual(NSInteger64AttributeType, 300)
        self.assertEqual(NSDecimalAttributeType, 400)
        self.assertEqual(NSDoubleAttributeType, 500)
        self.assertEqual(NSFloatAttributeType, 600)
        self.assertEqual(NSStringAttributeType, 700)
        self.assertEqual(NSBooleanAttributeType, 800)
        self.assertEqual(NSDateAttributeType, 900)
        self.assertEqual(NSBinaryDataAttributeType, 1000)
        self.assertEqual(NSUUIDAttributeType, 1100)
        self.assertEqual(NSURIAttributeType, 1200)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(NSTransformableAttributeType, 1800)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(NSObjectIDAttributeType, 2000)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSAttributeDescription.allowsExternalBinaryDataStorage)
        self.assertArgIsBOOL(
            NSAttributeDescription.setAllowsExternalBinaryDataStorage_, 0
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            NSAttributeDescription.preservesValueInHistoryOnDeletion
        )
        self.assertArgIsBOOL(
            NSAttributeDescription.setPreservesValueInHistoryOnDeletion_, 0
        )


if __name__ == "__main__":
    main()
