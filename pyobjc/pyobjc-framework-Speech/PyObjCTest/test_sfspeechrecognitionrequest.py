from PyObjCTools.TestSupport import *

import Speech


class TestSFSpeechRecognitionRequest(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            Speech.SFSpeechRecognitionRequest.shouldReportPartialResults
        )
        self.assertArgIsBOOL(
            Speech.SFSpeechRecognitionRequest.setShouldReportPartialResults_, 0
        )
        self.assertResultIsBOOL(
            Speech.SFSpeechRecognitionRequest.requiresOnDeviceRecognition
        )
        self.assertArgIsBOOL(
            Speech.SFSpeechRecognitionRequest.setRequiresOnDeviceRecognition_, 0
        )
