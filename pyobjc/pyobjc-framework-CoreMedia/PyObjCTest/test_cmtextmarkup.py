from PyObjCTools.TestSupport import *

import CoreMedia


class TestCMTextMarkup(TestCase):
    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_ForegroundColorARGB, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_BackgroundColorARGB, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_CharacterBackgroundColorARGB, unicode
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_BoldStyle, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_ItalicStyle, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_UnderlineStyle, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_FontFamilyName, unicode)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_GenericFontFamilyName, unicode
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Default, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Serif, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_SansSerif, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Monospace, unicode)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_ProportionalSerif, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_ProportionalSansSerif, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_MonospaceSerif, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_MonospaceSansSerif, unicode
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Casual, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Cursive, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Fantasy, unicode)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_SmallCapital, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight,
            unicode,
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_RelativeFontSize, unicode
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_VerticalLayout, unicode)
        self.assertIsInstance(CoreMedia.kCMTextVerticalLayout_LeftToRight, unicode)
        self.assertIsInstance(CoreMedia.kCMTextVerticalLayout_RightToLeft, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_Alignment, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Start, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Middle, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_End, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Left, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Right, unicode)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection,
            unicode,
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection,
            unicode,
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_WritingDirectionSizePercentage, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_CharacterEdgeStyle, unicode
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_None, unicode)
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_Raised, unicode)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupCharacterEdgeStyle_Depressed, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupCharacterEdgeStyle_Uniform, unicode
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupCharacterEdgeStyle_DropShadow, unicode
        )


if __name__ == "__main__":
    main()
