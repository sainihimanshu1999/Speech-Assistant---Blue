from PyObjCTools.TestSupport import *

from ImageCaptureCore import *


class TestICScannerFunctionalUnits(TestCase):
    def testConstants(self):
        self.assertEqual(ICScannerFunctionalUnitTypeFlatbed, 0)
        self.assertEqual(ICScannerFunctionalUnitTypePositiveTransparency, 1)
        self.assertEqual(ICScannerFunctionalUnitTypeNegativeTransparency, 2)
        self.assertEqual(ICScannerFunctionalUnitTypeDocumentFeeder, 3)

        self.assertEqual(ICScannerMeasurementUnitInches, 0)
        self.assertEqual(ICScannerMeasurementUnitCentimeters, 1)
        self.assertEqual(ICScannerMeasurementUnitPicas, 2)
        self.assertEqual(ICScannerMeasurementUnitPoints, 3)
        self.assertEqual(ICScannerMeasurementUnitTwips, 4)
        self.assertEqual(ICScannerMeasurementUnitPixels, 5)

        self.assertEqual(ICScannerBitDepth1Bit, 1)
        self.assertEqual(ICScannerBitDepth8Bits, 8)
        self.assertEqual(ICScannerBitDepth16Bits, 16)

        self.assertEqual(ICScannerColorDataFormatTypeChunky, 0)
        self.assertEqual(ICScannerColorDataFormatTypePlanar, 1)

        self.assertEqual(ICScannerPixelDataTypeBW, 0)
        self.assertEqual(ICScannerPixelDataTypeGray, 1)
        self.assertEqual(ICScannerPixelDataTypeRGB, 2)
        self.assertEqual(ICScannerPixelDataTypePalette, 3)
        self.assertEqual(ICScannerPixelDataTypeCMY, 4)
        self.assertEqual(ICScannerPixelDataTypeCMYK, 5)
        self.assertEqual(ICScannerPixelDataTypeYUV, 6)
        self.assertEqual(ICScannerPixelDataTypeYUVK, 7)
        self.assertEqual(ICScannerPixelDataTypeCIEXYZ, 8)

        self.assertEqual(ICScannerDocumentTypeDefault, 0)
        self.assertEqual(ICScannerDocumentTypeA4, 1)
        self.assertEqual(ICScannerDocumentTypeB5, 2)
        self.assertEqual(ICScannerDocumentTypeUSLetter, 3)
        self.assertEqual(ICScannerDocumentTypeUSLegal, 4)
        self.assertEqual(ICScannerDocumentTypeA5, 5)
        self.assertEqual(ICScannerDocumentTypeISOB4, 6)
        self.assertEqual(ICScannerDocumentTypeISOB6, 7)
        self.assertEqual(ICScannerDocumentTypeUSLedger, 9)
        self.assertEqual(ICScannerDocumentTypeUSExecutive, 10)
        self.assertEqual(ICScannerDocumentTypeA3, 11)
        self.assertEqual(ICScannerDocumentTypeISOB3, 12)
        self.assertEqual(ICScannerDocumentTypeA6, 13)
        self.assertEqual(ICScannerDocumentTypeC4, 14)
        self.assertEqual(ICScannerDocumentTypeC5, 15)
        self.assertEqual(ICScannerDocumentTypeC6, 16)
        self.assertEqual(ICScannerDocumentType4A0, 17)
        self.assertEqual(ICScannerDocumentType2A0, 18)
        self.assertEqual(ICScannerDocumentTypeA0, 19)
        self.assertEqual(ICScannerDocumentTypeA1, 20)
        self.assertEqual(ICScannerDocumentTypeA2, 21)
        self.assertEqual(ICScannerDocumentTypeA7, 22)
        self.assertEqual(ICScannerDocumentTypeA8, 23)
        self.assertEqual(ICScannerDocumentTypeA9, 24)
        self.assertEqual(ICScannerDocumentType10, 25)
        self.assertEqual(ICScannerDocumentTypeISOB0, 26)
        self.assertEqual(ICScannerDocumentTypeISOB1, 27)
        self.assertEqual(ICScannerDocumentTypeISOB2, 28)
        self.assertEqual(ICScannerDocumentTypeISOB5, 29)
        self.assertEqual(ICScannerDocumentTypeISOB7, 30)
        self.assertEqual(ICScannerDocumentTypeISOB8, 31)
        self.assertEqual(ICScannerDocumentTypeISOB9, 32)
        self.assertEqual(ICScannerDocumentTypeISOB10, 33)
        self.assertEqual(ICScannerDocumentTypeJISB0, 34)
        self.assertEqual(ICScannerDocumentTypeJISB1, 35)
        self.assertEqual(ICScannerDocumentTypeJISB2, 36)
        self.assertEqual(ICScannerDocumentTypeJISB3, 37)
        self.assertEqual(ICScannerDocumentTypeJISB4, 38)
        self.assertEqual(ICScannerDocumentTypeJISB6, 39)
        self.assertEqual(ICScannerDocumentTypeJISB7, 40)
        self.assertEqual(ICScannerDocumentTypeJISB8, 41)
        self.assertEqual(ICScannerDocumentTypeJISB9, 42)
        self.assertEqual(ICScannerDocumentTypeJISB10, 43)
        self.assertEqual(ICScannerDocumentTypeC0, 44)
        self.assertEqual(ICScannerDocumentTypeC1, 45)
        self.assertEqual(ICScannerDocumentTypeC2, 46)
        self.assertEqual(ICScannerDocumentTypeC3, 47)
        self.assertEqual(ICScannerDocumentTypeC7, 48)
        self.assertEqual(ICScannerDocumentTypeC8, 49)
        self.assertEqual(ICScannerDocumentTypeC9, 50)
        self.assertEqual(ICScannerDocumentTypeC10, 51)
        self.assertEqual(ICScannerDocumentTypeUSStatement, 52)
        self.assertEqual(ICScannerDocumentTypeBusinessCard, 53)
        self.assertEqual(ICScannerDocumentTypeE, 60)
        self.assertEqual(ICScannerDocumentType3R, 61)
        self.assertEqual(ICScannerDocumentType4R, 62)
        self.assertEqual(ICScannerDocumentType5R, 63)
        self.assertEqual(ICScannerDocumentType6R, 64)
        self.assertEqual(ICScannerDocumentType8R, 65)
        self.assertEqual(ICScannerDocumentTypeS8R, 66)
        self.assertEqual(ICScannerDocumentType10R, 67)
        self.assertEqual(ICScannerDocumentTypeS10R, 68)
        self.assertEqual(ICScannerDocumentType11R, 69)
        self.assertEqual(ICScannerDocumentType12R, 70)
        self.assertEqual(ICScannerDocumentTypeS12R, 71)
        self.assertEqual(ICScannerDocumentType110, 72)
        self.assertEqual(ICScannerDocumentTypeAPSH, 73)
        self.assertEqual(ICScannerDocumentTypeAPSC, 74)
        self.assertEqual(ICScannerDocumentTypeAPSP, 75)
        self.assertEqual(ICScannerDocumentType135, 76)
        self.assertEqual(ICScannerDocumentTypeMF, 77)
        self.assertEqual(ICScannerDocumentTypeLF, 78)

        self.assertEqual(ICScannerFunctionalUnitStateReady, 1 << 0)
        self.assertEqual(ICScannerFunctionalUnitStateScanInProgress, 1 << 1)
        self.assertEqual(ICScannerFunctionalUnitStateOverviewScanInProgress, 1 << 2)

        self.assertEqual(ICScannerFeatureTypeEnumeration, 0)
        self.assertEqual(ICScannerFeatureTypeRange, 1)
        self.assertEqual(ICScannerFeatureTypeBoolean, 2)
        self.assertEqual(ICScannerFeatureTypeTemplate, 3)

    def testMethods(self):
        self.assertResultIsBOOL(ICScannerFeatureBoolean.value)
        self.assertArgIsBOOL(ICScannerFeatureBoolean.setValue_, 0)

        self.assertResultIsBOOL(
            ICScannerFunctionalUnit.acceptsThresholdForBlackAndWhiteScanning
        )
        self.assertResultIsBOOL(
            ICScannerFunctionalUnit.usesThresholdForBlackAndWhiteScanning
        )
        self.assertArgIsBOOL(
            ICScannerFunctionalUnit.setUsesThresholdForBlackAndWhiteScanning_, 0
        )
        self.assertResultIsBOOL(ICScannerFunctionalUnit.scanInProgress)
        self.assertResultIsBOOL(ICScannerFunctionalUnit.canPerformOverviewScan)
        self.assertResultIsBOOL(ICScannerFunctionalUnit.overviewScanInProgress)
        self.assertResultIsBOOL(
            ICScannerFunctionalUnitDocumentFeeder.supportsDuplexScanning
        )
        self.assertResultIsBOOL(
            ICScannerFunctionalUnitDocumentFeeder.duplexScanningEnabled
        )
        self.assertArgIsBOOL(
            ICScannerFunctionalUnitDocumentFeeder.setDuplexScanningEnabled_, 0
        )
        self.assertResultIsBOOL(ICScannerFunctionalUnitDocumentFeeder.documentLoaded)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            ICScannerFunctionalUnitDocumentFeeder.reverseFeederPageOrder
        )


if __name__ == "__main__":
    main()
