from PyObjCTools.TestSupport import *
from Quartz import *


class TestCVOpenGLBufferPool(TestCase):
    def testTypes(self):
        self.assertIsCFType(CVOpenGLBufferPoolRef)

    def testConstants(self):
        self.assertIsInstance(kCVOpenGLBufferPoolMinimumBufferCountKey, unicode)
        self.assertIsInstance(kCVOpenGLBufferPoolMaximumBufferAgeKey, unicode)

    def testFunctions(self):
        self.assertIsInstance(CVOpenGLBufferPoolGetTypeID(), (int, long))

        # FIXME: find some good creation parameters
        self.assertArgIsOut(CVOpenGLBufferPoolCreate, 3)
        self.assertArgIsCFRetained(CVOpenGLBufferPoolCreate, 3)
        rv, pool = CVOpenGLBufferPoolCreate(
            None,
            {
                kCVOpenGLBufferPoolMinimumBufferCountKey: 1,
                kCVOpenGLBufferPoolMaximumBufferAgeKey: 42.0,
            },
            {},
            None,
        )
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, CVOpenGLBufferPoolRef)

        v = CVOpenGLBufferPoolRetain(pool)
        self.assertTrue(v is pool)
        CVOpenGLBufferPoolRelease(v)

        v = CVOpenGLBufferPoolGetAttributes(pool)
        self.assertIsInstance(v, (dict, CFDictionaryRef))

        v = CVOpenGLBufferPoolGetOpenGLBufferAttributes(pool)
        self.assertIsInstance(v, (dict, CFDictionaryRef))

        self.assertArgIsOut(CVOpenGLBufferPoolCreateOpenGLBuffer, 2)
        self.assertArgIsCFRetained(CVOpenGLBufferPoolCreateOpenGLBuffer, 2)
        rv, buf = CVOpenGLBufferPoolCreateOpenGLBuffer(None, pool, None)
        self.assertIsInstance(rv, (int, long))
        if rv == 0:
            self.assertIsInstance(buf, CVOpenGLBufferRef)
        else:
            self.assertTrue(buf is None)


if __name__ == "__main__":
    main()
