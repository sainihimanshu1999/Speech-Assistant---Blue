from PyObjCTools.TestSupport import *

import CoreMotion


class TestCMMagnetometer(TestCase):
    def test_structs(self):
        v = CoreMotion.CMMagneticField()
        self.assertEqual(v.x, 0.0)
        self.assertEqual(v.y, 0.0)
        self.assertEqual(v.z, 0.0)
