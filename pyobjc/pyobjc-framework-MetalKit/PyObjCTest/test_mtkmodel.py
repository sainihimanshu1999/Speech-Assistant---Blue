from PyObjCTools.TestSupport import *

import sys

if sys.maxsize > 2 ** 32:

    import MetalKit

    class TestMTKModel(TestCase):
        @min_os_level("10.11")
        def test_constants10_11(self):
            self.assertIsInstance(MetalKit.MTKModelErrorDomain, unicode)
            self.assertIsInstance(MetalKit.MTKModelErrorKey, unicode)

        @min_os_level("10.11")
        def test_methods10_11(self):
            self.assertArgIsOut(MetalKit.MTKMesh.initWithMesh_device_error_, 2)
            self.assertArgIsOut(
                MetalKit.MTKMesh.newMeshesFromAsset_device_sourceMeshes_error_, 3
            )

        @min_os_level("10.11")
        def test_functions10_11(self):
            MetalKit.MTKModelIOVertexDescriptorFromMetal
            MetalKit.MTKMetalVertexDescriptorFromModelIO
            MetalKit.MTKModelIOVertexFormatFromMetal
            MetalKit.MTKMetalVertexFormatFromModelIO

        @min_os_level("10.12")
        def test_functions10_12(self):
            self.assertArgIsOut(
                MetalKit.MTKModelIOVertexDescriptorFromMetalWithError, 1
            )
            self.assertArgIsOut(
                MetalKit.MTKMetalVertexDescriptorFromModelIOWithError, 1
            )
