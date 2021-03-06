from PyObjCTools.TestSupport import *
from QTKit import *


class TestQTMedia(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTMediaTypeVideo, unicode)
        self.assertIsInstance(QTMediaTypeSound, unicode)
        self.assertIsInstance(QTMediaTypeText, unicode)
        self.assertIsInstance(QTMediaTypeBase, unicode)
        self.assertIsInstance(QTMediaTypeMPEG, unicode)
        self.assertIsInstance(QTMediaTypeMusic, unicode)
        self.assertIsInstance(QTMediaTypeTimeCode, unicode)
        self.assertIsInstance(QTMediaTypeSprite, unicode)
        self.assertIsInstance(QTMediaTypeFlash, unicode)
        self.assertIsInstance(QTMediaTypeMovie, unicode)
        self.assertIsInstance(QTMediaTypeTween, unicode)
        self.assertIsInstance(QTMediaType3D, unicode)
        self.assertIsInstance(QTMediaTypeSkin, unicode)
        self.assertIsInstance(QTMediaTypeQTVR, unicode)
        self.assertIsInstance(QTMediaTypeHint, unicode)
        self.assertIsInstance(QTMediaTypeStream, unicode)
        self.assertIsInstance(QTMediaTypeMuxed, unicode)
        self.assertIsInstance(QTMediaTypeQuartzComposer, unicode)
        self.assertIsInstance(QTMediaCharacteristicVisual, unicode)
        self.assertIsInstance(QTMediaCharacteristicAudio, unicode)
        self.assertIsInstance(QTMediaCharacteristicCanSendVideo, unicode)
        self.assertIsInstance(QTMediaCharacteristicProvidesActions, unicode)
        self.assertIsInstance(QTMediaCharacteristicNonLinear, unicode)
        self.assertIsInstance(QTMediaCharacteristicCanStep, unicode)
        self.assertIsInstance(QTMediaCharacteristicHasNoDuration, unicode)
        self.assertIsInstance(QTMediaCharacteristicHasSkinData, unicode)
        self.assertIsInstance(QTMediaCharacteristicProvidesKeyFocus, unicode)
        self.assertIsInstance(QTMediaCharacteristicHasVideoFrameRate, unicode)
        self.assertIsInstance(QTMediaCreationTimeAttribute, unicode)
        self.assertIsInstance(QTMediaDurationAttribute, unicode)
        self.assertIsInstance(QTMediaModificationTimeAttribute, unicode)
        self.assertIsInstance(QTMediaSampleCountAttribute, unicode)
        self.assertIsInstance(QTMediaQualityAttribute, unicode)
        self.assertIsInstance(QTMediaTimeScaleAttribute, unicode)
        self.assertIsInstance(QTMediaTypeAttribute, unicode)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(QTMediaTypeSubtitle, unicode)
        self.assertIsInstance(QTMediaTypeClosedCaption, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QTMedia.hasCharacteristic_)

    @onlyOn32Bit
    def testMethods32bit(self):
        self.assertArgIsOut(QTMedia.mediaWithQuickTimeMedia_error_, 1)
        self.assertArgIsOut(QTMedia.initWithQuickTimeMedia_error_, 1)


if __name__ == "__main__":
    main()
