from PyObjCTools.TestSupport import *

import IOSurface


class TestIOSurfaceAPI(TestCase):
    def testCFTypes(self):
        self.assertIsCFType(IOSurface.IOSurfaceRef)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(IOSurface.kIOSurfacePixelSizeCastingAllowed, unicode)

    @min_os_level("10.6")
    def testConstants(self):
        self.assertIsInstance(IOSurface.kIOSurfaceAllocSize, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceWidth, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceHeight, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceBytesPerRow, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceBytesPerElement, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceElementWidth, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceElementHeight, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceOffset, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneInfo, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneWidth, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneHeight, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBytesPerRow, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneOffset, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneSize, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBase, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBytesPerElement, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneElementWidth, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneElementHeight, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceCacheMode, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceIsGlobal, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePixelFormat, unicode)

        self.assertEqual(IOSurface.kIOSurfaceLockReadOnly, 0x00000001)
        self.assertEqual(IOSurface.kIOSurfaceLockAvoidSync, 0x00000002)

        self.assertEqual(IOSurface.kIOSurfaceComponentNameUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameAlpha, 1)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameRed, 2)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameGreen, 3)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameBlue, 4)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameLuma, 5)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameChromaRed, 6)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameChromaBlue, 7)

        self.assertEqual(IOSurface.kIOSurfaceComponentTypeUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeUnsignedInteger, 1)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeSignedInteger, 2)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeFloat, 3)

        self.assertEqual(IOSurface.kIOSurfaceComponentRangeUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeFullRange, 1)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeVideoRange, 2)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeWideRange, 3)

        self.assertEqual(IOSurface.kIOSurfaceSubsamplingUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceSubsamplingNone, 1)
        self.assertEqual(IOSurface.kIOSurfaceSubsampling422, 2)
        self.assertEqual(IOSurface.kIOSurfaceSubsampling420, 3)
        self.assertEqual(IOSurface.kIOSurfaceSubsampling411, 4)

        self.assertEqual(IOSurface.kIOSurfacePurgeableNonVolatile, 0)
        self.assertEqual(IOSurface.kIOSurfacePurgeableVolatile, 1)
        self.assertEqual(IOSurface.kIOSurfacePurgeableEmpty, 2)
        self.assertEqual(IOSurface.kIOSurfacePurgeableKeepCurrent, 3)

        self.assertEqual(IOSurface.kIOSurfaceDefaultCache, 0)
        self.assertEqual(IOSurface.kIOSurfaceInhibitCache, 1)
        self.assertEqual(IOSurface.kIOSurfaceWriteThruCache, 2)
        self.assertEqual(IOSurface.kIOSurfaceCopybackCache, 3)
        self.assertEqual(IOSurface.kIOSurfaceWriteCombineCache, 4)
        self.assertEqual(IOSurface.kIOSurfaceCopybackInnerCache, 5)

        self.assertEqual(IOSurface.kIOSurfaceMapCacheShift, 8)
        self.assertEqual(
            IOSurface.kIOSurfaceMapDefaultCache,
            IOSurface.kIOSurfaceDefaultCache << IOSurface.kIOSurfaceMapCacheShift,
        )
        self.assertEqual(
            IOSurface.kIOSurfaceMapInhibitCache,
            IOSurface.kIOSurfaceInhibitCache << IOSurface.kIOSurfaceMapCacheShift,
        )
        self.assertEqual(
            IOSurface.kIOSurfaceMapWriteThruCache,
            IOSurface.kIOSurfaceWriteThruCache << IOSurface.kIOSurfaceMapCacheShift,
        )
        self.assertEqual(
            IOSurface.kIOSurfaceMapCopybackCache,
            IOSurface.kIOSurfaceCopybackCache << IOSurface.kIOSurfaceMapCacheShift,
        )
        self.assertEqual(
            IOSurface.kIOSurfaceMapWriteCombineCache,
            IOSurface.kIOSurfaceWriteCombineCache << IOSurface.kIOSurfaceMapCacheShift,
        )
        self.assertEqual(
            IOSurface.kIOSurfaceMapCopybackInnerCache,
            IOSurface.kIOSurfaceCopybackInnerCache << IOSurface.kIOSurfaceMapCacheShift,
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBitsPerElement, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentBitDepths, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentBitOffsets, unicode)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentNames, unicode)
        self.assertIsInstance(IOSurface.kIOSurfaceSubsampling, unicode)

    @min_os_level("10.6")
    def testFunctions(self):
        self.assertIsInstance(IOSurface.IOSurfaceGetTypeID(), (int, long))

        self.assertResultIsCFRetained(IOSurface.IOSurfaceCreate)

        self.assertResultIsCFRetained(IOSurface.IOSurfaceLookup)

        IOSurface.IOSurfaceGetID

        self.assertArgIsInOut(IOSurface.IOSurfaceLock, 2)
        self.assertArgIsInOut(IOSurface.IOSurfaceUnlock, 2)

        IOSurface.IOSurfaceGetAllocSize
        IOSurface.IOSurfaceGetWidth
        IOSurface.IOSurfaceGetHeight
        IOSurface.IOSurfaceGetBytesPerElement
        IOSurface.IOSurfaceGetBytesPerRow

        self.assertResultHasType(IOSurface.IOSurfaceGetBaseAddress, b"^v")
        self.assertResultIsVariableSize(IOSurface.IOSurfaceGetBaseAddress)

        IOSurface.IOSurfaceGetElementWidth
        IOSurface.IOSurfaceGetElementHeight

        IOSurface.IOSurfaceGetPixelFormat

        IOSurface.IOSurfaceGetSeed
        IOSurface.IOSurfaceGetPlaneCount
        IOSurface.IOSurfaceGetWidthOfPlane
        IOSurface.IOSurfaceGetHeightOfPlane
        IOSurface.IOSurfaceGetBytesPerElementOfPlane
        IOSurface.IOSurfaceGetBytesPerRowOfPlane

        self.assertResultHasType(IOSurface.IOSurfaceGetBaseAddressOfPlane, b"^v")
        self.assertResultIsVariableSize(IOSurface.IOSurfaceGetBaseAddressOfPlane)

        IOSurface.IOSurfaceGetElementWidthOfPlane
        IOSurface.IOSurfaceGetElementHeightOfPlane

        self.assertArgHasType(IOSurface.IOSurfaceSetValue, 2, objc._C_ID)

        self.assertResultHasType(IOSurface.IOSurfaceCopyValue, objc._C_ID)

        IOSurface.IOSurfaceRemoveValue
        IOSurface.IOSurfaceSetValues

        self.assertResultIsCFRetained(IOSurface.IOSurfaceCopyAllValues)

        IOSurface.IOSurfaceRemoveAllValues

        IOSurface.IOSurfaceCreateMachPort

        self.assertResultIsCFRetained(IOSurface.IOSurfaceLookupFromMachPort)

        IOSurface.IOSurfaceGetPropertyMaximum
        IOSurface.IOSurfaceGetPropertyAlignment
        IOSurface.IOSurfaceAlignProperty
        IOSurface.IOSurfaceIncrementUseCount
        IOSurface.IOSurfaceDecrementUseCount
        IOSurface.IOSurfaceGetUseCount

        self.assertResultIsBOOL(IOSurface.IOSurfaceIsInUse)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        IOSurface.IOSurfaceCreateXPCObject

        self.assertResultIsCFRetained(IOSurface.IOSurfaceLookupFromXPCObject)

    @min_os_level("10.12")
    def testFunctions10_12(self):
        self.assertResultIsBOOL(IOSurface.IOSurfaceAllowsPixelSizeCasting)

    @min_os_level("10.13")
    def testFunctions10_13(self):
        IOSurface.IOSurfaceGetNumberOfComponentsOfPlane
        IOSurface.IOSurfaceGetNameOfComponentOfPlane
        IOSurface.IOSurfaceGetTypeOfComponentOfPlane
        IOSurface.IOSurfaceGetRangeOfComponentOfPlane
        IOSurface.IOSurfaceGetBitDepthOfComponentOfPlane
        IOSurface.IOSurfaceGetBitOffsetOfComponentOfPlane

        self.assertResultIsBOOL(IOSurface.IOSurfaceAllowsPixelSizeCasting)


if __name__ == "__main__":
    main()
