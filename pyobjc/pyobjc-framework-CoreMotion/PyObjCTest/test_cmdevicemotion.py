from PyObjCTools.TestSupport import *

import CoreMotion


class TestCMDeviceMotion(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyUncalibrated, -1)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyLow, 0)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyMedium, 1)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyHigh, 2)

    def test_structs(self):
        v = CoreMotion.CMCalibratedMagneticField()
        self.assertEqual(v.field, CoreMotion.CMMagneticField())
        self.assertEqual(v.accuracy, 0)
