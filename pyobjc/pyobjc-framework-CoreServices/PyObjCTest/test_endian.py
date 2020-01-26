from PyObjCTools.TestSupport import *

import CoreServices


class TestAIFF(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("Endian16_Swap")
        self.assert_not_wrapped("Endian32_Swap")
        self.assert_not_wrapped("Endian64_Swap")
        self.assert_not_wrapped("EndianS16_NtoB")
        self.assert_not_wrapped("EndianU16_BtoN")
        self.assert_not_wrapped("EndianU16_NtoB")
        self.assert_not_wrapped("EndianS32_BtoN")
        self.assert_not_wrapped("EndianS32_NtoB")
        self.assert_not_wrapped("EndianU32_BtoN")
        self.assert_not_wrapped("EndianU32_NtoB")
        self.assert_not_wrapped("EndianS64_BtoN")
        self.assert_not_wrapped("EndianS64_NtoB")
        self.assert_not_wrapped("EndianU64_BtoN")
        self.assert_not_wrapped("EndianS16_LtoN")
        self.assert_not_wrapped("EndianS16_NtoL")
        self.assert_not_wrapped("EndianU16_LtoN")
        self.assert_not_wrapped("EndianU16_NtoL")
        self.assert_not_wrapped("EndianS32_LtoN")
        self.assert_not_wrapped("EndianS32_NtoL")
        self.assert_not_wrapped("EndianU32_LtoN")
        self.assert_not_wrapped("EndianU32_NtoL")
        self.assert_not_wrapped("EndianS64_LtoN")
        self.assert_not_wrapped("EndianS64_NtoL")
        self.assert_not_wrapped("EndianU64_LtoN")
        self.assert_not_wrapped("EndianU64_NtoL")
        self.assert_not_wrapped("EndianS16_LtoB")
        self.assert_not_wrapped("EndianS16_BtoL")
        self.assert_not_wrapped("EndianU16_LtoB")
        self.assert_not_wrapped("EndianU16_BtoL")
        self.assert_not_wrapped("EndianS32_LtoB")
        self.assert_not_wrapped("EndianS32_BtoL")
        self.assert_not_wrapped("EndianU32_LtoB")
        self.assert_not_wrapped("EndianU32_BtoL")
        self.assert_not_wrapped("EndianS64_LtoB")
        self.assert_not_wrapped("EndianS64_BtoL")
        self.assert_not_wrapped("EndianU64_LtoB")
        self.assert_not_wrapped("EndianU64_BtoL")
        self.assert_not_wrapped("BigEndianUInt32")
        self.assert_not_wrapped("BigEndianLong")
        self.assert_not_wrapped("BigEndianUnsignedLong")
        self.assert_not_wrapped("BigEndianShort")
        self.assert_not_wrapped("BigEndianUnsignedShort")
        self.assert_not_wrapped("BigEndianFixed")
        self.assert_not_wrapped("BigEndianUnsignedFixed")
        self.assert_not_wrapped("BigEndianOSType")
        self.assert_not_wrapped("kCoreEndianResourceManagerDomain")
        self.assert_not_wrapped("kCoreEndianAppleEventManagerDomain")
        self.assert_not_wrapped("CoreEndianInstallFlipper")
        self.assert_not_wrapped("CoreEndianGetFlipper")
        self.assert_not_wrapped("CoreEndianFlipData")


if __name__ == "__main__":
    main()