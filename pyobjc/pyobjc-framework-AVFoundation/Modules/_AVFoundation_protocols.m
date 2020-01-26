/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(AVAssetResourceLoaderDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVAudioPlayerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVAudioRecorderDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVCaptureAudioDataOutputSampleBufferDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVCaptureFileOutputDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVCaptureFileOutputRecordingDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVCaptureMetadataOutputObjectsDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVCaptureVideoDataOutputSampleBufferDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPlayerItemLegibleOutputPushDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPlayerItemMetadataOutputPushDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPlayerItemOutputPullDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPlayerItemOutputPushDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVVideoCompositionValidationHandling));
    Py_XDECREF(p);
#if PyObjC_BUILD_RELEASE >= 1009
    p = PyObjC_IdToPython(@protocol(AVVideoCompositing));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVVideoCompositionInstruction));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(AVAudioMixing));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVAudioStereoMixing));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVAudio3DMixing));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(AVFragmentMinding));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(AVQueuedSampleBufferRendering));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPlayerItemMetadataCollectorPushDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1014
    // Defined in the AVFAudio subframework, but header is never included in the
    // toplevel framework...
    // p = PyObjC_IdToPython(@protocol(AVSpeechSynthesizerDelegate)); Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    // p = PyObjC_IdToPython(@protocol(AVAssetDownloadDelegate)); Py_XDECREF(p);
#endif
}