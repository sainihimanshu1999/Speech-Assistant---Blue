from PyObjCTools.TestSupport import *

import CoreAudio


class TestAudioDriverPlugIn(TestCase):
    def testFunctions(self):
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInOpen"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInClose"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInDeviceGetPropertyInfo"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInDeviceGetProperty"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInDeviceSetProperty"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInStreamGetPropertyInfo"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInStreamGetProperty"))
        self.assertFalse(hasattr(CoreAudio, "AudioDriverPlugInStreamSetProperty"))


if __name__ == "__main__":
    main()
