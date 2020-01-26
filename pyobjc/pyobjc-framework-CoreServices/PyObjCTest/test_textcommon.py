from PyObjCTools.TestSupport import *

import CoreServices


class TestTextCommon(TestCase):
    def test_constants(self):
        self.assertEqual(CoreServices.kTextFlushDefault, 0)
        self.assertEqual(CoreServices.kTextCenter, 1)
        self.assertEqual(CoreServices.kTextFlushRight, -1)
        self.assertEqual(CoreServices.kTextFlushLeft, -2)

        self.assertEqual(CoreServices.kTextEncodingMacRoman, 0)
        self.assertEqual(CoreServices.kTextEncodingMacJapanese, 1)
        self.assertEqual(CoreServices.kTextEncodingMacChineseTrad, 2)
        self.assertEqual(CoreServices.kTextEncodingMacKorean, 3)
        self.assertEqual(CoreServices.kTextEncodingMacArabic, 4)
        self.assertEqual(CoreServices.kTextEncodingMacHebrew, 5)
        self.assertEqual(CoreServices.kTextEncodingMacGreek, 6)
        self.assertEqual(CoreServices.kTextEncodingMacCyrillic, 7)
        self.assertEqual(CoreServices.kTextEncodingMacDevanagari, 9)
        self.assertEqual(CoreServices.kTextEncodingMacGurmukhi, 10)
        self.assertEqual(CoreServices.kTextEncodingMacGujarati, 11)
        self.assertEqual(CoreServices.kTextEncodingMacOriya, 12)
        self.assertEqual(CoreServices.kTextEncodingMacBengali, 13)
        self.assertEqual(CoreServices.kTextEncodingMacTamil, 14)
        self.assertEqual(CoreServices.kTextEncodingMacTelugu, 15)
        self.assertEqual(CoreServices.kTextEncodingMacKannada, 16)
        self.assertEqual(CoreServices.kTextEncodingMacMalayalam, 17)
        self.assertEqual(CoreServices.kTextEncodingMacSinhalese, 18)
        self.assertEqual(CoreServices.kTextEncodingMacBurmese, 19)
        self.assertEqual(CoreServices.kTextEncodingMacKhmer, 20)
        self.assertEqual(CoreServices.kTextEncodingMacThai, 21)
        self.assertEqual(CoreServices.kTextEncodingMacLaotian, 22)
        self.assertEqual(CoreServices.kTextEncodingMacGeorgian, 23)
        self.assertEqual(CoreServices.kTextEncodingMacArmenian, 24)
        self.assertEqual(CoreServices.kTextEncodingMacChineseSimp, 25)
        self.assertEqual(CoreServices.kTextEncodingMacTibetan, 26)
        self.assertEqual(CoreServices.kTextEncodingMacMongolian, 27)
        self.assertEqual(CoreServices.kTextEncodingMacEthiopic, 28)
        self.assertEqual(CoreServices.kTextEncodingMacCentralEurRoman, 29)
        self.assertEqual(CoreServices.kTextEncodingMacVietnamese, 30)
        self.assertEqual(CoreServices.kTextEncodingMacExtArabic, 31)
        self.assertEqual(CoreServices.kTextEncodingMacSymbol, 33)
        self.assertEqual(CoreServices.kTextEncodingMacDingbats, 34)
        self.assertEqual(CoreServices.kTextEncodingMacTurkish, 35)
        self.assertEqual(CoreServices.kTextEncodingMacCroatian, 36)
        self.assertEqual(CoreServices.kTextEncodingMacIcelandic, 37)
        self.assertEqual(CoreServices.kTextEncodingMacRomanian, 38)
        self.assertEqual(CoreServices.kTextEncodingMacCeltic, 39)
        self.assertEqual(CoreServices.kTextEncodingMacGaelic, 40)
        self.assertEqual(CoreServices.kTextEncodingMacKeyboardGlyphs, 41)

        self.assertEqual(
            CoreServices.kTextEncodingMacTradChinese,
            CoreServices.kTextEncodingMacChineseTrad,
        )
        self.assertEqual(CoreServices.kTextEncodingMacRSymbol, 8)
        self.assertEqual(
            CoreServices.kTextEncodingMacSimpChinese,
            CoreServices.kTextEncodingMacChineseSimp,
        )
        self.assertEqual(
            CoreServices.kTextEncodingMacGeez, CoreServices.kTextEncodingMacEthiopic
        )
        self.assertEqual(
            CoreServices.kTextEncodingMacEastEurRoman,
            CoreServices.kTextEncodingMacCentralEurRoman,
        )
        self.assertEqual(CoreServices.kTextEncodingMacUninterp, 32)

        self.assertEqual(CoreServices.kTextEncodingMacUnicode, 0x7E)

        self.assertEqual(CoreServices.kTextEncodingMacFarsi, 0x8C)
        self.assertEqual(CoreServices.kTextEncodingMacUkrainian, 0x98)
        self.assertEqual(CoreServices.kTextEncodingMacInuit, 0xEC)
        self.assertEqual(CoreServices.kTextEncodingMacVT100, 0xFC)

        self.assertEqual(CoreServices.kTextEncodingMacHFS, 0xFF)

        self.assertEqual(CoreServices.kTextEncodingUnicodeDefault, 0x0100)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV1_1, 0x0101)
        self.assertEqual(CoreServices.kTextEncodingISO10646_1993, 0x0101)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV2_0, 0x0103)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV2_1, 0x0103)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV3_0, 0x0104)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV3_1, 0x0105)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV3_2, 0x0106)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV4_0, 0x0108)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV5_0, 0x010A)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV5_1, 0x010B)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV6_0, 0x010D)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV6_1, 0x010E)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV6_3, 0x0110)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV7_0, 0x0111)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV8_0, 0x0112)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV9_0, 0x0113)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV10_0, 0x0114)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV11_0, 0x0115)
        self.assertEqual(CoreServices.kTextEncodingUnicodeV12_1, 0x0116)

        self.assertEqual(CoreServices.kTextEncodingISOLatin1, 0x0201)
        self.assertEqual(CoreServices.kTextEncodingISOLatin2, 0x0202)
        self.assertEqual(CoreServices.kTextEncodingISOLatin3, 0x0203)
        self.assertEqual(CoreServices.kTextEncodingISOLatin4, 0x0204)
        self.assertEqual(CoreServices.kTextEncodingISOLatinCyrillic, 0x0205)
        self.assertEqual(CoreServices.kTextEncodingISOLatinArabic, 0x0206)
        self.assertEqual(CoreServices.kTextEncodingISOLatinGreek, 0x0207)
        self.assertEqual(CoreServices.kTextEncodingISOLatinHebrew, 0x0208)
        self.assertEqual(CoreServices.kTextEncodingISOLatin5, 0x0209)
        self.assertEqual(CoreServices.kTextEncodingISOLatin6, 0x020A)
        self.assertEqual(CoreServices.kTextEncodingISOLatin7, 0x020D)
        self.assertEqual(CoreServices.kTextEncodingISOLatin8, 0x020E)
        self.assertEqual(CoreServices.kTextEncodingISOLatin9, 0x020F)
        self.assertEqual(CoreServices.kTextEncodingISOLatin10, 0x0210)

        self.assertEqual(CoreServices.kTextEncodingDOSLatinUS, 0x0400)
        self.assertEqual(CoreServices.kTextEncodingDOSGreek, 0x0405)
        self.assertEqual(CoreServices.kTextEncodingDOSBalticRim, 0x0406)
        self.assertEqual(CoreServices.kTextEncodingDOSLatin1, 0x0410)
        self.assertEqual(CoreServices.kTextEncodingDOSGreek1, 0x0411)
        self.assertEqual(CoreServices.kTextEncodingDOSLatin2, 0x0412)
        self.assertEqual(CoreServices.kTextEncodingDOSCyrillic, 0x0413)
        self.assertEqual(CoreServices.kTextEncodingDOSTurkish, 0x0414)
        self.assertEqual(CoreServices.kTextEncodingDOSPortuguese, 0x0415)
        self.assertEqual(CoreServices.kTextEncodingDOSIcelandic, 0x0416)
        self.assertEqual(CoreServices.kTextEncodingDOSHebrew, 0x0417)
        self.assertEqual(CoreServices.kTextEncodingDOSCanadianFrench, 0x0418)
        self.assertEqual(CoreServices.kTextEncodingDOSArabic, 0x0419)
        self.assertEqual(CoreServices.kTextEncodingDOSNordic, 0x041A)
        self.assertEqual(CoreServices.kTextEncodingDOSRussian, 0x041B)
        self.assertEqual(CoreServices.kTextEncodingDOSGreek2, 0x041C)
        self.assertEqual(CoreServices.kTextEncodingDOSThai, 0x041D)
        self.assertEqual(CoreServices.kTextEncodingDOSJapanese, 0x0420)
        self.assertEqual(CoreServices.kTextEncodingDOSChineseSimplif, 0x0421)
        self.assertEqual(CoreServices.kTextEncodingDOSKorean, 0x0422)
        self.assertEqual(CoreServices.kTextEncodingDOSChineseTrad, 0x0423)
        self.assertEqual(CoreServices.kTextEncodingWindowsLatin1, 0x0500)
        self.assertEqual(CoreServices.kTextEncodingWindowsANSI, 0x0500)
        self.assertEqual(CoreServices.kTextEncodingWindowsLatin2, 0x0501)
        self.assertEqual(CoreServices.kTextEncodingWindowsCyrillic, 0x0502)
        self.assertEqual(CoreServices.kTextEncodingWindowsGreek, 0x0503)
        self.assertEqual(CoreServices.kTextEncodingWindowsLatin5, 0x0504)
        self.assertEqual(CoreServices.kTextEncodingWindowsHebrew, 0x0505)
        self.assertEqual(CoreServices.kTextEncodingWindowsArabic, 0x0506)
        self.assertEqual(CoreServices.kTextEncodingWindowsBalticRim, 0x0507)
        self.assertEqual(CoreServices.kTextEncodingWindowsVietnamese, 0x0508)
        self.assertEqual(CoreServices.kTextEncodingWindowsKoreanJohab, 0x0510)

        self.assertEqual(CoreServices.kTextEncodingUS_ASCII, 0x0600)
        self.assertEqual(CoreServices.kTextEncodingANSEL, 0x0601)
        self.assertEqual(CoreServices.kTextEncodingJIS_X0201_76, 0x0620)
        self.assertEqual(CoreServices.kTextEncodingJIS_X0208_83, 0x0621)
        self.assertEqual(CoreServices.kTextEncodingJIS_X0208_90, 0x0622)
        self.assertEqual(CoreServices.kTextEncodingJIS_X0212_90, 0x0623)
        self.assertEqual(CoreServices.kTextEncodingJIS_C6226_78, 0x0624)
        self.assertEqual(CoreServices.kTextEncodingShiftJIS_X0213, 0x0628)
        self.assertEqual(CoreServices.kTextEncodingJIS_X0213_MenKuTen, 0x0629)
        self.assertEqual(CoreServices.kTextEncodingGB_2312_80, 0x0630)
        self.assertEqual(CoreServices.kTextEncodingGBK_95, 0x0631)
        self.assertEqual(CoreServices.kTextEncodingGB_18030_2000, 0x0632)
        self.assertEqual(CoreServices.kTextEncodingGB_18030_2005, 0x0632)
        self.assertEqual(CoreServices.kTextEncodingKSC_5601_87, 0x0640)
        self.assertEqual(CoreServices.kTextEncodingKSC_5601_92_Johab, 0x0641)
        self.assertEqual(CoreServices.kTextEncodingCNS_11643_92_P1, 0x0651)
        self.assertEqual(CoreServices.kTextEncodingCNS_11643_92_P2, 0x0652)
        self.assertEqual(CoreServices.kTextEncodingCNS_11643_92_P3, 0x0653)

        self.assertEqual(CoreServices.kTextEncodingISO_2022_JP, 0x0820)
        self.assertEqual(CoreServices.kTextEncodingISO_2022_JP_2, 0x0821)
        self.assertEqual(CoreServices.kTextEncodingISO_2022_JP_1, 0x0822)
        self.assertEqual(CoreServices.kTextEncodingISO_2022_JP_3, 0x0823)
        self.assertEqual(CoreServices.kTextEncodingISO_2022_CN, 0x0830)
        self.assertEqual(CoreServices.kTextEncodingISO_2022_CN_EXT, 0x0831)
        self.assertEqual(CoreServices.kTextEncodingISO_2022_KR, 0x0840)

        self.assertEqual(CoreServices.kTextEncodingEUC_JP, 0x0920)
        self.assertEqual(CoreServices.kTextEncodingEUC_CN, 0x0930)
        self.assertEqual(CoreServices.kTextEncodingEUC_TW, 0x0931)
        self.assertEqual(CoreServices.kTextEncodingEUC_KR, 0x0940)

        self.assertEqual(CoreServices.kTextEncodingShiftJIS, 0x0A01)
        self.assertEqual(CoreServices.kTextEncodingKOI8_R, 0x0A02)
        self.assertEqual(CoreServices.kTextEncodingBig5, 0x0A03)
        self.assertEqual(CoreServices.kTextEncodingMacRomanLatin1, 0x0A04)
        self.assertEqual(CoreServices.kTextEncodingHZ_GB_2312, 0x0A05)
        self.assertEqual(CoreServices.kTextEncodingBig5_HKSCS_1999, 0x0A06)
        self.assertEqual(CoreServices.kTextEncodingVISCII, 0x0A07)
        self.assertEqual(CoreServices.kTextEncodingKOI8_U, 0x0A08)
        self.assertEqual(CoreServices.kTextEncodingBig5_E, 0x0A09)

        self.assertEqual(CoreServices.kTextEncodingNextStepLatin, 0x0B01)
        self.assertEqual(CoreServices.kTextEncodingNextStepJapanese, 0x0B02)

        self.assertEqual(CoreServices.kTextEncodingEBCDIC_LatinCore, 0x0C01)
        self.assertEqual(CoreServices.kTextEncodingEBCDIC_CP037, 0x0C02)

        self.assertEqual(CoreServices.kTextEncodingMultiRun, 0x0FFF)
        self.assertEqual(CoreServices.kTextEncodingUnknown, 0xFFFF)

        self.assertEqual(CoreServices.kTextEncodingEBCDIC_US, 0x0C01)

        self.assertEqual(CoreServices.kTextEncodingDefaultVariant, 0)

        self.assertEqual(CoreServices.kMacRomanDefaultVariant, 0)
        self.assertEqual(CoreServices.kMacRomanCurrencySignVariant, 1)
        self.assertEqual(CoreServices.kMacRomanEuroSignVariant, 2)

        self.assertEqual(CoreServices.kMacCyrillicDefaultVariant, 0)
        self.assertEqual(CoreServices.kMacCyrillicCurrSignStdVariant, 1)
        self.assertEqual(CoreServices.kMacCyrillicCurrSignUkrVariant, 2)
        self.assertEqual(CoreServices.kMacCyrillicEuroSignVariant, 3)

        self.assertEqual(CoreServices.kMacIcelandicStdDefaultVariant, 0)
        self.assertEqual(CoreServices.kMacIcelandicTTDefaultVariant, 1)
        self.assertEqual(CoreServices.kMacIcelandicStdCurrSignVariant, 2)
        self.assertEqual(CoreServices.kMacIcelandicTTCurrSignVariant, 3)
        self.assertEqual(CoreServices.kMacIcelandicStdEuroSignVariant, 4)
        self.assertEqual(CoreServices.kMacIcelandicTTEuroSignVariant, 5)

        self.assertEqual(CoreServices.kMacCroatianDefaultVariant, 0)
        self.assertEqual(CoreServices.kMacCroatianCurrencySignVariant, 1)
        self.assertEqual(CoreServices.kMacCroatianEuroSignVariant, 2)

        self.assertEqual(CoreServices.kMacRomanianDefaultVariant, 0)
        self.assertEqual(CoreServices.kMacRomanianCurrencySignVariant, 1)
        self.assertEqual(CoreServices.kMacRomanianEuroSignVariant, 2)

        self.assertEqual(CoreServices.kMacJapaneseStandardVariant, 0)
        self.assertEqual(CoreServices.kMacJapaneseStdNoVerticalsVariant, 1)
        self.assertEqual(CoreServices.kMacJapaneseBasicVariant, 2)
        self.assertEqual(CoreServices.kMacJapanesePostScriptScrnVariant, 3)
        self.assertEqual(CoreServices.kMacJapanesePostScriptPrintVariant, 4)
        self.assertEqual(CoreServices.kMacJapaneseVertAtKuPlusTenVariant, 5)

        self.assertEqual(CoreServices.kMacArabicStandardVariant, 0)
        self.assertEqual(CoreServices.kMacArabicTrueTypeVariant, 1)
        self.assertEqual(CoreServices.kMacArabicThuluthVariant, 2)
        self.assertEqual(CoreServices.kMacArabicAlBayanVariant, 3)

        self.assertEqual(CoreServices.kMacFarsiStandardVariant, 0)
        self.assertEqual(CoreServices.kMacFarsiTrueTypeVariant, 1)

        self.assertEqual(CoreServices.kMacHebrewStandardVariant, 0)
        self.assertEqual(CoreServices.kMacHebrewFigureSpaceVariant, 1)

        self.assertEqual(CoreServices.kMacGreekDefaultVariant, 0)
        self.assertEqual(CoreServices.kMacGreekNoEuroSignVariant, 1)
        self.assertEqual(CoreServices.kMacGreekEuroSignVariant, 2)

        self.assertEqual(CoreServices.kMacVT100DefaultVariant, 0)
        self.assertEqual(CoreServices.kMacVT100CurrencySignVariant, 1)
        self.assertEqual(CoreServices.kMacVT100EuroSignVariant, 2)

        self.assertEqual(CoreServices.kUnicodeNoSubset, 0)
        self.assertEqual(CoreServices.kUnicodeNormalizationFormD, 5)
        self.assertEqual(CoreServices.kUnicodeNormalizationFormC, 3)
        self.assertEqual(CoreServices.kUnicodeHFSPlusDecompVariant, 8)
        self.assertEqual(CoreServices.kUnicodeHFSPlusCompVariant, 9)

        self.assertEqual(CoreServices.kISOLatin1StandardVariant, 0)
        self.assertEqual(CoreServices.kISOLatin1MusicCDVariant, 1)

        self.assertEqual(CoreServices.kISOLatinArabicImplicitOrderVariant, 0)
        self.assertEqual(CoreServices.kISOLatinArabicVisualOrderVariant, 1)
        self.assertEqual(CoreServices.kISOLatinArabicExplicitOrderVariant, 2)

        self.assertEqual(CoreServices.kISOLatinHebrewImplicitOrderVariant, 0)
        self.assertEqual(CoreServices.kISOLatinHebrewVisualOrderVariant, 1)
        self.assertEqual(CoreServices.kISOLatinHebrewExplicitOrderVariant, 2)

        self.assertEqual(CoreServices.kWindowsLatin1StandardVariant, 0)
        self.assertEqual(CoreServices.kWindowsLatin1PalmVariant, 1)

        self.assertEqual(CoreServices.kDOSJapaneseStandardVariant, 0)
        self.assertEqual(CoreServices.kDOSJapanesePalmVariant, 1)

        self.assertEqual(CoreServices.kEUC_CN_BasicVariant, 0)
        self.assertEqual(CoreServices.kEUC_CN_DOSVariant, 1)

        self.assertEqual(CoreServices.kEUC_KR_BasicVariant, 0)
        self.assertEqual(CoreServices.kEUC_KR_DOSVariant, 1)

        self.assertEqual(CoreServices.kShiftJIS_BasicVariant, 0)
        self.assertEqual(CoreServices.kShiftJIS_DOSVariant, 1)
        self.assertEqual(CoreServices.kShiftJIS_MusicCDVariant, 2)

        self.assertEqual(CoreServices.kBig5_BasicVariant, 0)
        self.assertEqual(CoreServices.kBig5_StandardVariant, 1)
        self.assertEqual(CoreServices.kBig5_ETenVariant, 2)
        self.assertEqual(CoreServices.kBig5_DOSVariant, 3)

        self.assertEqual(CoreServices.kMacRomanLatin1DefaultVariant, 0)
        self.assertEqual(CoreServices.kMacRomanLatin1StandardVariant, 2)
        self.assertEqual(CoreServices.kMacRomanLatin1TurkishVariant, 6)
        self.assertEqual(CoreServices.kMacRomanLatin1CroatianVariant, 8)
        self.assertEqual(CoreServices.kMacRomanLatin1IcelandicVariant, 11)
        self.assertEqual(CoreServices.kMacRomanLatin1RomanianVariant, 14)

        self.assertEqual(CoreServices.kUnicodeNoCompatibilityVariant, 1)
        self.assertEqual(CoreServices.kUnicodeNoCorporateVariant, 4)

        self.assertEqual(CoreServices.kMacRomanStandardVariant, 0)
        self.assertEqual(CoreServices.kMacIcelandicStandardVariant, 0)
        self.assertEqual(CoreServices.kMacIcelandicTrueTypeVariant, 1)
        self.assertEqual(CoreServices.kJapaneseStandardVariant, 0)
        self.assertEqual(CoreServices.kJapaneseStdNoVerticalsVariant, 1)
        self.assertEqual(CoreServices.kJapaneseBasicVariant, 2)
        self.assertEqual(CoreServices.kJapanesePostScriptScrnVariant, 3)
        self.assertEqual(CoreServices.kJapanesePostScriptPrintVariant, 4)
        self.assertEqual(CoreServices.kJapaneseVertAtKuPlusTenVariant, 5)
        self.assertEqual(CoreServices.kTextEncodingShiftJIS_X0213_00, 0x0628)
        self.assertEqual(CoreServices.kHebrewStandardVariant, 0)
        self.assertEqual(CoreServices.kHebrewFigureSpaceVariant, 1)
        self.assertEqual(CoreServices.kUnicodeCanonicalDecompVariant, 2)
        self.assertEqual(CoreServices.kUnicodeMaxDecomposedVariant, 2)
        self.assertEqual(CoreServices.kUnicodeCanonicalCompVariant, 3)
        self.assertEqual(CoreServices.kUnicodeNoComposedVariant, 3)

        self.assertEqual(CoreServices.kTextEncodingDefaultFormat, 0)
        self.assertEqual(CoreServices.kUnicodeUTF16Format, 0)
        self.assertEqual(CoreServices.kUnicodeUTF7Format, 1)
        self.assertEqual(CoreServices.kUnicodeUTF8Format, 2)
        self.assertEqual(CoreServices.kUnicodeUTF32Format, 3)
        self.assertEqual(CoreServices.kUnicodeUTF16BEFormat, 4)
        self.assertEqual(CoreServices.kUnicodeUTF16LEFormat, 5)
        self.assertEqual(CoreServices.kUnicodeUTF32BEFormat, 6)
        self.assertEqual(CoreServices.kUnicodeUTF32LEFormat, 7)
        self.assertEqual(CoreServices.kUnicodeSCSUFormat, 8)
        self.assertEqual(CoreServices.kUnicode16BitFormat, 0)
        self.assertEqual(CoreServices.kUnicode32BitFormat, 3)

        self.assertEqual(CoreServices.kTextEncodingFullName, 0)
        self.assertEqual(CoreServices.kTextEncodingBaseName, 1)
        self.assertEqual(CoreServices.kTextEncodingVariantName, 2)
        self.assertEqual(CoreServices.kTextEncodingFormatName, 3)

        self.assertEqual(CoreServices.kTextScriptDontCare, -128)
        self.assertEqual(CoreServices.kTextLanguageDontCare, -128)
        self.assertEqual(CoreServices.kTextRegionDontCare, -128)

        self.assertEqual(CoreServices.kTECInfoCurrentFormat, 2)

        self.assertEqual(CoreServices.kTECKeepInfoFixBit, 0)
        self.assertEqual(CoreServices.kTECFallbackTextLengthFixBit, 1)
        self.assertEqual(CoreServices.kTECTextRunBitClearFixBit, 2)
        self.assertEqual(CoreServices.kTECTextToUnicodeScanFixBit, 3)
        self.assertEqual(CoreServices.kTECAddForceASCIIChangesBit, 4)
        self.assertEqual(CoreServices.kTECPreferredEncodingFixBit, 5)
        self.assertEqual(CoreServices.kTECAddTextRunHeuristicsBit, 6)
        self.assertEqual(CoreServices.kTECAddFallbackInterruptBit, 7)

        self.assertEqual(
            CoreServices.kTECKeepInfoFixMask, 1 << CoreServices.kTECKeepInfoFixBit
        )
        self.assertEqual(
            CoreServices.kTECFallbackTextLengthFixMask,
            1 << CoreServices.kTECFallbackTextLengthFixBit,
        )
        self.assertEqual(
            CoreServices.kTECTextRunBitClearFixMask,
            1 << CoreServices.kTECTextRunBitClearFixBit,
        )
        self.assertEqual(
            CoreServices.kTECTextToUnicodeScanFixMask,
            1 << CoreServices.kTECTextToUnicodeScanFixBit,
        )
        self.assertEqual(
            CoreServices.kTECAddForceASCIIChangesMask,
            1 << CoreServices.kTECAddForceASCIIChangesBit,
        )
        self.assertEqual(
            CoreServices.kTECPreferredEncodingFixMask,
            1 << CoreServices.kTECPreferredEncodingFixBit,
        )
        self.assertEqual(
            CoreServices.kTECAddTextRunHeuristicsMask,
            1 << CoreServices.kTECAddTextRunHeuristicsBit,
        )
        self.assertEqual(
            CoreServices.kTECAddFallbackInterruptMask,
            1 << CoreServices.kTECAddFallbackInterruptBit,
        )

        self.assertEqual(CoreServices.kUnicodeByteOrderMark, 0xFEFF)
        self.assertEqual(CoreServices.kUnicodeObjectReplacement, 0xFFFC)
        self.assertEqual(CoreServices.kUnicodeReplacementChar, 0xFFFD)
        self.assertEqual(CoreServices.kUnicodeSwappedByteOrderMark, 0xFFFE)
        self.assertEqual(CoreServices.kUnicodeNotAChar, 0xFFFF)

        self.assertEqual(CoreServices.kUCCharPropTypeGenlCategory, 1)
        self.assertEqual(CoreServices.kUCCharPropTypeCombiningClass, 2)
        self.assertEqual(CoreServices.kUCCharPropTypeBidiCategory, 3)
        self.assertEqual(CoreServices.kUCCharPropTypeDecimalDigitValue, 4)

        self.assertEqual(CoreServices.kUCGenlCatOtherNotAssigned, 0)
        self.assertEqual(CoreServices.kUCGenlCatOtherControl, 1)
        self.assertEqual(CoreServices.kUCGenlCatOtherFormat, 2)
        self.assertEqual(CoreServices.kUCGenlCatOtherSurrogate, 3)
        self.assertEqual(CoreServices.kUCGenlCatOtherPrivateUse, 4)
        self.assertEqual(CoreServices.kUCGenlCatMarkNonSpacing, 5)
        self.assertEqual(CoreServices.kUCGenlCatMarkSpacingCombining, 6)
        self.assertEqual(CoreServices.kUCGenlCatMarkEnclosing, 7)
        self.assertEqual(CoreServices.kUCGenlCatNumberDecimalDigit, 8)
        self.assertEqual(CoreServices.kUCGenlCatNumberLetter, 9)
        self.assertEqual(CoreServices.kUCGenlCatNumberOther, 10)
        self.assertEqual(CoreServices.kUCGenlCatSeparatorSpace, 11)
        self.assertEqual(CoreServices.kUCGenlCatSeparatorLine, 12)
        self.assertEqual(CoreServices.kUCGenlCatSeparatorParagraph, 13)
        self.assertEqual(CoreServices.kUCGenlCatLetterUppercase, 14)
        self.assertEqual(CoreServices.kUCGenlCatLetterLowercase, 15)
        self.assertEqual(CoreServices.kUCGenlCatLetterTitlecase, 16)
        self.assertEqual(CoreServices.kUCGenlCatLetterModifier, 17)
        self.assertEqual(CoreServices.kUCGenlCatLetterOther, 18)
        self.assertEqual(CoreServices.kUCGenlCatPunctConnector, 20)
        self.assertEqual(CoreServices.kUCGenlCatPunctDash, 21)
        self.assertEqual(CoreServices.kUCGenlCatPunctOpen, 22)
        self.assertEqual(CoreServices.kUCGenlCatPunctClose, 23)
        self.assertEqual(CoreServices.kUCGenlCatPunctInitialQuote, 24)
        self.assertEqual(CoreServices.kUCGenlCatPunctFinalQuote, 25)
        self.assertEqual(CoreServices.kUCGenlCatPunctOther, 26)
        self.assertEqual(CoreServices.kUCGenlCatSymbolMath, 28)
        self.assertEqual(CoreServices.kUCGenlCatSymbolCurrency, 29)
        self.assertEqual(CoreServices.kUCGenlCatSymbolModifier, 30)
        self.assertEqual(CoreServices.kUCGenlCatSymbolOther, 31)

        self.assertEqual(CoreServices.kUCBidiCatNotApplicable, 0)
        self.assertEqual(CoreServices.kUCBidiCatLeftRight, 1)
        self.assertEqual(CoreServices.kUCBidiCatRightLeft, 2)
        self.assertEqual(CoreServices.kUCBidiCatEuroNumber, 3)
        self.assertEqual(CoreServices.kUCBidiCatEuroNumberSeparator, 4)
        self.assertEqual(CoreServices.kUCBidiCatEuroNumberTerminator, 5)
        self.assertEqual(CoreServices.kUCBidiCatArabicNumber, 6)
        self.assertEqual(CoreServices.kUCBidiCatCommonNumberSeparator, 7)
        self.assertEqual(CoreServices.kUCBidiCatBlockSeparator, 8)
        self.assertEqual(CoreServices.kUCBidiCatSegmentSeparator, 9)
        self.assertEqual(CoreServices.kUCBidiCatWhitespace, 10)
        self.assertEqual(CoreServices.kUCBidiCatOtherNeutral, 11)
        self.assertEqual(CoreServices.kUCBidiCatRightLeftArabic, 12)
        self.assertEqual(CoreServices.kUCBidiCatLeftRightEmbedding, 13)
        self.assertEqual(CoreServices.kUCBidiCatRightLeftEmbedding, 14)
        self.assertEqual(CoreServices.kUCBidiCatLeftRightOverride, 15)
        self.assertEqual(CoreServices.kUCBidiCatRightLeftOverride, 16)
        self.assertEqual(CoreServices.kUCBidiCatPopDirectionalFormat, 17)
        self.assertEqual(CoreServices.kUCBidiCatNonSpacingMark, 18)
        self.assertEqual(CoreServices.kUCBidiCatBoundaryNeutral, 19)
        self.assertEqual(CoreServices.kUCBidiCatLeftRightIsolate, 20)
        self.assertEqual(CoreServices.kUCBidiCatRightLeftIsolate, 21)
        self.assertEqual(CoreServices.kUCBidiCatFirstStrongIsolate, 22)
        self.assertEqual(CoreServices.kUCBidiCatPopDirectionalIsolate, 23)

        self.assertEqual(CoreServices.kUCHighSurrogateRangeStart, 0xD800)
        self.assertEqual(CoreServices.kUCHighSurrogateRangeEnd, 0xDBFF)
        self.assertEqual(CoreServices.kUCLowSurrogateRangeStart, 0xDC00)
        self.assertEqual(CoreServices.kUCLowSurrogateRangeEnd, 0xDFFF)

    def test_structs(self):
        v = CoreServices.TextEncodingRun()
        self.assertEqual(v.offset, 0)
        self.assertEqual(v.textEncoding, 0)

        v = CoreServices.ScriptCodeRun()
        self.assertEqual(v.offset, 0)
        self.assertEqual(v.script, 0)

        # XXX tecTextEncodingsFolderName and tecExtensionFileName are Str31
        v = CoreServices.TECInfo()
        self.assertEqual(v.format, 0)
        self.assertEqual(v.tecVersion, 0)
        self.assertEqual(v.tecTextConverterFeatures, 0)
        self.assertEqual(v.tecUnicodeConverterFeatures, 0)
        self.assertEqual(v.tecTextCommonFeatures, 0)
        self.assertEqual(v.tecTextEncodingsFolderName, None)
        self.assertEqual(v.tecExtensionFileName, None)
        self.assertEqual(v.tecLowestTEFileVersion, 0)
        self.assertEqual(v.tecHighestTEFileVersion, 0)

    def test_functions(self):
        CoreServices.CreateTextEncoding
        CoreServices.GetTextEncodingBase
        CoreServices.GetTextEncodingVariant
        CoreServices.GetTextEncodingFormat
        CoreServices.ResolveDefaultTextEncoding

        self.assertArgIsOut(CoreServices.GetTextEncodingName, 5)
        self.assertArgIsOut(CoreServices.GetTextEncodingName, 6)
        self.assertArgIsOut(CoreServices.GetTextEncodingName, 7)
        self.assertArgIsOut(CoreServices.GetTextEncodingName, 8)
        self.assertArgSizeInArg(CoreServices.GetTextEncodingName, 8, (4, 5))

        self.assertArgIsOut(CoreServices.TECGetInfo, 0)

        self.assertArgIsOut(CoreServices.UpgradeScriptInfoToTextEncoding, 4)

        # XXX: Last argument is Str255
        self.assertArgIsOut(CoreServices.RevertTextEncodingToScriptInfo, 1)
        self.assertArgIsOut(CoreServices.RevertTextEncodingToScriptInfo, 2)
        self.assertArgIsOut(CoreServices.RevertTextEncodingToScriptInfo, 3)

        self.assertArgIsOut(CoreServices.GetTextEncodingFromScriptInfo, 3)

        self.assertArgIsOut(CoreServices.GetScriptInfoFromTextEncoding, 1)
        self.assertArgIsOut(CoreServices.GetScriptInfoFromTextEncoding, 2)

        self.assertArgIsOut(CoreServices.NearestMacTextEncodings, 1)
        self.assertArgIsOut(CoreServices.NearestMacTextEncodings, 2)

        self.assertArgIsIn(CoreServices.UCGetCharProperty, 0)
        self.assertArgSizeInArg(CoreServices.UCGetCharProperty, 0, 1)
        self.assertArgIsOut(CoreServices.UCGetCharProperty, 3)

    def test_inline_functions(self):
        self.assertResultIsBOOL(CoreServices.UCIsSurrogateHighCharacter)
        self.assertResultIsBOOL(CoreServices.UCIsSurrogateLowCharacter)
        CoreServices.UCGetUnicodeScalarValueForSurrogatePair


if __name__ == "__main__":
    main()
