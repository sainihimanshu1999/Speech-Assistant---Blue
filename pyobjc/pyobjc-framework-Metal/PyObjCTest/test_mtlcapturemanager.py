from PyObjCTools.TestSupport import *

import Metal


class TestMTLArgument(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLCaptureErrorNotSupported, 1)
        self.assertEqual(Metal.MTLCaptureErrorAlreadyCapturing, 2)
        self.assertEqual(Metal.MTLCaptureErrorInvalidDescriptor, 3)

        self.assertEqual(Metal.MTLCaptureDestinationDeveloperTools, 1)
        self.assertEqual(Metal.MTLCaptureDestinationGPUTraceDocument, 2)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(Metal.MTLCaptureManager.isCapturing)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(Metal.MTLCaptureManager.supportsDestination_)

        self.assertResultIsBOOL(
            Metal.MTLCaptureManager.startCaptureWithDescriptor_error_
        )
        self.assertArgIsOut(
            Metal.MTLCaptureManager.startCaptureWithDescriptor_error_, 1
        )
