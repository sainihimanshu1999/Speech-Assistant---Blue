from PyObjCTools.TestSupport import *
import VideoToolbox


class TestVTCompressionProperties(TestCase):
    def test_constants(self):
        self.assertEqual(VideoToolbox.kVTUnlimitedFrameDelayCount, -1)

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_NumberOfPendingFrames, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PixelBufferPoolIsShared, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes,
            unicode,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxKeyFrameInterval, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AllowTemporalCompression, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AllowFrameReordering, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AverageBitRate, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_DataRateLimits, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_Quality, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MoreFramesBeforeStart, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MoreFramesAfterEnd, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ProfileLevel, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_1_3, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_3_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_3_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_3_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_4_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_3_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_3_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_3_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_4_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_4_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_5_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Extended_5_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Simple_L3, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Main_L2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Main_L3, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_MP4V_Main_L4, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L0, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L1, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L2, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L3, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_MP4V_AdvancedSimple_L4, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H263_Profile0_Level10, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H263_Profile0_Level45, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H263_Profile3_Level45, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_Depth, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxFrameDelayCount, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaxH264SliceBytes, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_SourceFrameCount, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ExpectedFrameRate, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ExpectedDuration, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTEncodeFrameOptionKey_ForceKeyFrame, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_CleanAperture, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PixelAspectRatio, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_FieldCount, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_FieldDetail, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AspectRatio16x9, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ProgressiveScan, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ColorPrimaries, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_TransferFunction, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_YCbCrMatrix, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ICCProfile, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_PixelTransferProperties, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_5_0, unicode)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_4_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_4_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_5_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_5_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Baseline_5_2, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H264_Baseline_AutoLevel, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_4_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_5_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_5_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_Main_AutoLevel, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_H264_Extended_AutoLevel, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_3_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_3_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_3_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_4_0, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_4_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_4_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_5_1, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_5_2, unicode)
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_H264_High_AutoLevel, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_H264EntropyMode, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTH264EntropyMode_CAVLC, unicode)
        self.assertIsInstance(VideoToolbox.kVTH264EntropyMode_CABAC, unicode)
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_RealTime, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder,
            unicode,
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder,
            unicode,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder,
            unicode,
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_GammaLevel, unicode
        )

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MultiPassStorage, unicode
        )

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(VideoToolbox.kVTProfileLevel_HEVC_Main_AutoLevel, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTProfileLevel_HEVC_Main10_AutoLevel, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_BaseLayerFrameRate, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MasteringDisplayColorVolume, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_ContentLightLevelInfo, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTCompressionPropertyKey_EncoderID, unicode)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AllowOpenGOP, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_MaximizePowerEfficiency, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID,
            unicode,
        )
        self.assertIsInstance(
            VideoToolbox.kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID,
            unicode,
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_TargetQualityForAlpha, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_AlphaChannelMode, unicode
        )
        self.assertIsInstance(VideoToolbox.kVTAlphaChannelMode_StraightAlpha, unicode)
        self.assertIsInstance(
            VideoToolbox.kVTAlphaChannelMode_PremultipliedAlpha, unicode
        )
        self.assertIsInstance(
            VideoToolbox.kVTCompressionPropertyKey_UsingGPURegistryID, unicode
        )


if __name__ == "__main__":
    main()
