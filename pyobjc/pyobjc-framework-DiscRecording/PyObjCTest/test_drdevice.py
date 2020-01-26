from PyObjCTools.TestSupport import *

import DiscRecording


class TestDRDevice(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRDevice.isValid)
        self.assertResultIsBOOL(DiscRecording.DRDevice.openTray)
        self.assertResultIsBOOL(DiscRecording.DRDevice.closeTray)
        self.assertResultIsBOOL(DiscRecording.DRDevice.ejectMedia)
        self.assertResultIsBOOL(DiscRecording.DRDevice.acquireExclusiveAccess)
        self.assertResultIsBOOL(DiscRecording.DRDevice.isEqualToDevice_)
        self.assertResultIsBOOL(DiscRecording.DRDevice.writesCD)
        self.assertResultIsBOOL(DiscRecording.DRDevice.writesDVD)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsPresent)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsTransitioning)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsBusy)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsBlank)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsAppendable)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsOverwritable)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsErasable)
        self.assertResultIsBOOL(DiscRecording.DRDevice.mediaIsReserved)
        self.assertResultIsBOOL(DiscRecording.DRDevice.trayIsOpen)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRDeviceBurnSpeedCD1x, float)
        self.assertIsInstance(DiscRecording.DRDeviceBurnSpeedDVD1x, float)
        self.assertIsInstance(DiscRecording.DRDeviceBurnSpeedBD1x, float)
        self.assertIsInstance(DiscRecording.DRDeviceBurnSpeedHDDVD1x, float)
        self.assertIsInstance(DiscRecording.DRDeviceBurnSpeedMax, float)

        self.assertIsInstance(DiscRecording.DRDeviceAppearedNotification, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceDisappearedNotification, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceStatusChangedNotification, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceSupportLevelKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceIORegistryEntryPathKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceWriteCapabilitiesKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceVendorNameKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceProductNameKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceFirmwareRevisionKey, unicode)
        self.assertIsInstance(DiscRecording.DRDevicePhysicalInterconnectKey, unicode)
        self.assertIsInstance(
            DiscRecording.DRDevicePhysicalInterconnectLocationKey, unicode
        )
        self.assertIsInstance(
            DiscRecording.DRDeviceLoadingMechanismCanEjectKey, unicode
        )
        self.assertIsInstance(
            DiscRecording.DRDeviceLoadingMechanismCanInjectKey, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceLoadingMechanismCanOpenKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceWriteBufferSizeKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceSupportLevelNone, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceSupportLevelUnsupported, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceSupportLevelVendorSupported, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceSupportLevelAppleSupported, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceSupportLevelAppleShipping, unicode)
        self.assertIsInstance(DiscRecording.DRDevicePhysicalInterconnectATAPI, unicode)
        self.assertIsInstance(
            DiscRecording.DRDevicePhysicalInterconnectFibreChannel, unicode
        )
        self.assertIsInstance(
            DiscRecording.DRDevicePhysicalInterconnectFireWire, unicode
        )
        self.assertIsInstance(DiscRecording.DRDevicePhysicalInterconnectSCSI, unicode)
        self.assertIsInstance(DiscRecording.DRDevicePhysicalInterconnectUSB, unicode)
        self.assertIsInstance(
            DiscRecording.DRDevicePhysicalInterconnectLocationInternal, unicode
        )
        self.assertIsInstance(
            DiscRecording.DRDevicePhysicalInterconnectLocationExternal, unicode
        )
        self.assertIsInstance(
            DiscRecording.DRDevicePhysicalInterconnectLocationUnknown, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDRKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDRWKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDRKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDRDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDRWKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDRWDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDRAMKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDPlusRKey, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceCanWriteDVDPlusRDoubleLayerKey, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDPlusRWKey, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceCanWriteDVDPlusRWDoubleLayerKey, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteBDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteBDRKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteBDREKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteHDDVDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteHDDVDRKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteHDDVDRDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteHDDVDRAMKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteHDDVDRWKey, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceCanWriteHDDVDRWDualLayerKey, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDTextKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteIndexPointsKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteISRCKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDTAOKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDSAOKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteCDRawKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanWriteDVDDAOKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanTestWriteCDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanTestWriteDVDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanUnderrunProtectCDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCanUnderrunProtectDVDKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceIsBusyKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceIsTrayOpenKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMaximumWriteSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceCurrentWriteSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaStateKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaInfoKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceBurnSpeedsKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceTrackRefsKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceTrackInfoKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaStateMediaPresent, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaStateInTransition, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaStateNone, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaBSDNameKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaIsBlankKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaIsAppendableKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaIsOverwritableKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaIsErasableKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaIsReservedKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaOverwritableSpaceKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaFreeSpaceKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaUsedSpaceKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaBlocksOverwritableKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaBlocksFreeKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaBlocksUsedKey, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceMediaDoubleLayerL0DataZoneBlocksKey, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceMediaTrackCountKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaSessionCountKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaClassKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaClassCD, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaClassDVD, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaClassBD, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaClassHDDVD, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaClassUnknown, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeCDROM, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeCDR, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeCDRW, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDROM, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDRAM, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDR, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDRDualLayer, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDRW, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDRWDualLayer, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDPlusR, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceMediaTypeDVDPlusRDoubleLayer, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeDVDPlusRW, unicode)
        self.assertIsInstance(
            DiscRecording.DRDeviceMediaTypeDVDPlusRWDoubleLayer, unicode
        )
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeBDR, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeBDRE, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeBDROM, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeHDDVDROM, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeHDDVDR, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeHDDVDRDualLayer, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeHDDVDRAM, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeHDDVDRW, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeHDDVDRWDualLayer, unicode)
        self.assertIsInstance(DiscRecording.DRDeviceMediaTypeUnknown, unicode)


if __name__ == "__main__":
    main()
