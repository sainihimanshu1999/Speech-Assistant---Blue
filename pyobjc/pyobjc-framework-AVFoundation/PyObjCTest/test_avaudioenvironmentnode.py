from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVAudioEnvironmentNode(TestCase):
    def testConstants(self):
        self.assertEqual(
            AVFoundation.AVAudioEnvironmentDistanceAttenuationModelExponential, 1
        )
        self.assertEqual(
            AVFoundation.AVAudioEnvironmentDistanceAttenuationModelInverse, 2
        )
        self.assertEqual(
            AVFoundation.AVAudioEnvironmentDistanceAttenuationModelLinear, 3
        )

        self.assertEqual(AVFoundation.AVAudioEnvironmentOutputTypeAuto, 0)
        self.assertEqual(AVFoundation.AVAudioEnvironmentOutputTypeHeadphones, 1)
        self.assertEqual(AVFoundation.AVAudioEnvironmentOutputTypeBuiltInSpeakers, 2)
        self.assertEqual(AVFoundation.AVAudioEnvironmentOutputTypeExternalSpeakers, 3)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioEnvironmentReverbParameters.enable)
        self.assertArgIsBOOL(
            AVFoundation.AVAudioEnvironmentReverbParameters.setEnable_, 0
        )


if __name__ == "__main__":
    main()
