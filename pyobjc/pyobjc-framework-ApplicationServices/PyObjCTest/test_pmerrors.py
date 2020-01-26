import PrintCore
import sys
from PyObjCTools.TestSupport import *


class TestPMErrors(TestCase):
    def test_constants(self):
        self.assertEqual(PrintCore.kPMAllocationFailure, -108)
        self.assertEqual(PrintCore.kPMInternalError, PrintCore.kPMGeneralError)

        self.assertEqual(PrintCore.kPMInvalidIndex, -30882)
        self.assertEqual(PrintCore.kPMStringConversionFailure, -30883)
        self.assertEqual(PrintCore.kPMXMLParseError, -30884)

        self.assertEqual(PrintCore.kPMInvalidJobTemplate, -30885)
        self.assertEqual(PrintCore.kPMInvalidPrinterInfo, -30886)
        self.assertEqual(PrintCore.kPMInvalidConnection, -30887)
        self.assertEqual(PrintCore.kPMInvalidKey, -30888)
        self.assertEqual(PrintCore.kPMInvalidValue, -30889)
        self.assertEqual(PrintCore.kPMInvalidAllocator, -30890)
        self.assertEqual(PrintCore.kPMInvalidTicket, -30891)
        self.assertEqual(PrintCore.kPMInvalidItem, -30892)
        self.assertEqual(PrintCore.kPMInvalidType, -30893)
        self.assertEqual(PrintCore.kPMInvalidReply, -30894)
        self.assertEqual(PrintCore.kPMInvalidFileType, -30895)
        self.assertEqual(PrintCore.kPMInvalidObject, -30896)
        self.assertEqual(PrintCore.kPMInvalidPaper, -30897)
        self.assertEqual(PrintCore.kPMInvalidCalibrationTarget, -30898)

        self.assertEqual(PrintCore.kPMNoDefaultItem, -9500)
        self.assertEqual(PrintCore.kPMNoDefaultSettings, -9501)
        self.assertEqual(PrintCore.kPMInvalidPDEContext, -9530)
        self.assertEqual(PrintCore.kPMDontSwitchPDEError, -9531)
        self.assertEqual(PrintCore.kPMUnableToFindProcess, -9532)
        self.assertEqual(PrintCore.kPMFeatureNotInstalled, -9533)

        self.assertEqual(PrintCore.kPMInvalidPBMRef, -9540)
        self.assertEqual(PrintCore.kPMNoSelectedPrinters, -9541)
        self.assertEqual(PrintCore.kPMInvalidLookupSpec, -9542)
        self.assertEqual(PrintCore.kPMSyncRequestFailed, -9543)
        self.assertEqual(PrintCore.kPMEditRequestFailed, -9544)
        self.assertEqual(PrintCore.kPMPrBrowserNoUI, -9545)

        self.assertEqual(PrintCore.kPMTicketTypeNotFound, -9580)
        self.assertEqual(PrintCore.kPMUpdateTicketFailed, -9581)
        self.assertEqual(PrintCore.kPMValidateTicketFailed, -9582)
        self.assertEqual(PrintCore.kPMSubTicketNotFound, -9583)
        self.assertEqual(PrintCore.kPMInvalidSubTicket, -9584)
        self.assertEqual(PrintCore.kPMDeleteSubTicketFailed, -9585)
        self.assertEqual(PrintCore.kPMItemIsLocked, -9586)
        self.assertEqual(PrintCore.kPMTicketIsLocked, -9587)
        self.assertEqual(PrintCore.kPMTemplateIsLocked, -9588)
        self.assertEqual(PrintCore.kPMKeyNotFound, -9589)
        self.assertEqual(PrintCore.kPMKeyNotUnique, -9590)
        self.assertEqual(PrintCore.kPMUnknownDataType, -9591)

        self.assertEqual(PrintCore.kPMCreateMessageFailed, -9620)
        self.assertEqual(PrintCore.kPMServerCommunicationFailed, -9621)
        self.assertEqual(PrintCore.kPMKeyOrValueNotFound, -9623)
        self.assertEqual(PrintCore.kPMMessagingError, -9624)

        self.assertEqual(PrintCore.kPMServerNotFound, -9630)
        self.assertEqual(PrintCore.kPMServerAlreadyRunning, -9631)
        self.assertEqual(PrintCore.kPMServerSuspended, -9632)
        self.assertEqual(PrintCore.kPMServerAttributeRestricted, -9633)
        self.assertEqual(PrintCore.kPMFileOrDirOperationFailed, -9634)
        self.assertEqual(PrintCore.kPMUserOrGroupNotFound, -9635)
        self.assertEqual(PrintCore.kPMPermissionError, -9636)
        self.assertEqual(PrintCore.kPMUnknownMessage, -9637)
        self.assertEqual(PrintCore.kPMQueueNotFound, -9638)
        self.assertEqual(PrintCore.kPMQueueAlreadyExists, -9639)
        self.assertEqual(PrintCore.kPMQueueJobFailed, -9640)
        self.assertEqual(PrintCore.kPMJobNotFound, -9641)
        self.assertEqual(PrintCore.kPMJobBusy, -9642)
        self.assertEqual(PrintCore.kPMJobCanceled, -9643)
        self.assertEqual(PrintCore.kPMDocumentNotFound, -9644)

        self.assertEqual(PrintCore.kPMPMSymbolNotFound, -9660)
        self.assertEqual(PrintCore.kPMIOMSymbolNotFound, -9661)
        self.assertEqual(PrintCore.kPMCVMSymbolNotFound, -9662)
        self.assertEqual(PrintCore.kPMInvalidPMContext, -9663)
        self.assertEqual(PrintCore.kPMInvalidIOMContext, -9664)
        self.assertEqual(PrintCore.kPMInvalidCVMContext, -9665)
        self.assertEqual(PrintCore.kPMInvalidJobID, -9666)
        self.assertEqual(PrintCore.kPMNoPrinterJobID, -9667)
        self.assertEqual(PrintCore.kPMJobStreamOpenFailed, -9668)
        self.assertEqual(PrintCore.kPMJobStreamReadFailed, -9669)
        self.assertEqual(PrintCore.kPMJobStreamEndError, -9670)
        self.assertEqual(PrintCore.kPMJobManagerAborted, -9671)
        self.assertEqual(PrintCore.kPMJobGetTicketBadFormatError, -9672)
        self.assertEqual(PrintCore.kPMJobGetTicketReadError, -9673)

        self.assertEqual(PrintCore.kPMPluginNotFound, -9701)
        self.assertEqual(PrintCore.kPMPluginRegisterationFailed, -9702)
        self.assertEqual(PrintCore.kPMFontNotFound, -9703)
        self.assertEqual(PrintCore.kPMFontNameTooLong, -9704)
        self.assertEqual(PrintCore.kPMGeneralCGError, -9705)
        self.assertEqual(PrintCore.kPMInvalidState, -9706)
        self.assertEqual(PrintCore.kPMUnexpectedImagingError, -9707)

        self.assertEqual(PrintCore.kPMInvalidPrinterAddress, -9780)
        self.assertEqual(PrintCore.kPMOpenFailed, -9781)
        self.assertEqual(PrintCore.kPMReadFailed, -9782)
        self.assertEqual(PrintCore.kPMWriteFailed, -9783)
        self.assertEqual(PrintCore.kPMStatusFailed, -9784)
        self.assertEqual(PrintCore.kPMCloseFailed, -9785)
        self.assertEqual(PrintCore.kPMUnsupportedConnection, -9786)
        self.assertEqual(PrintCore.kPMIOAttrNotAvailable, -9787)
        self.assertEqual(PrintCore.kPMReadGotZeroData, -9788)

        self.assertEqual(
            PrintCore.kPMLastErrorCodeToMakeMaintenanceOfThisListEasier, -9799
        )


if __name__ == "__main__":
    main()
