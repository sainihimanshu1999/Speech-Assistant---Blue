from PyObjCTools.TestSupport import *
import CoreServices
import sys
import os


class TestLSInfo(TestCase):
    def setUp(self):
        self.path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "dummy.txt"
        )
        fp = open(self.path, "w")
        fp.write("test contents")
        fp.close()

        self.bpath = self.path.encode("utf-8")

    def tearDown(self):
        if os.path.exists(self.path):
            os.unlink(self.path)

    def testConstants(self):
        if sys.maxsize < 2 ** 32:
            self.assertEqual(CoreServices.kLSInvalidExtensionIndex, 0xFFFFFFFF)
        else:
            self.assertEqual(CoreServices.kLSInvalidExtensionIndex, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(CoreServices.kLSAppInTrashErr, -10660)
        self.assertEqual(CoreServices.kLSExecutableIncorrectFormat, -10661)
        self.assertEqual(CoreServices.kLSAttributeNotFoundErr, -10662)
        self.assertEqual(CoreServices.kLSAttributeNotSettableErr, -10663)
        self.assertEqual(CoreServices.kLSIncompatibleApplicationVersionErr, -10664)
        self.assertEqual(CoreServices.kLSNoRosettaEnvironmentErr, -10665)
        self.assertEqual(CoreServices.kLSUnknownErr, -10810)
        self.assertEqual(CoreServices.kLSNotAnApplicationErr, -10811)
        self.assertEqual(CoreServices.kLSNotInitializedErr, -10812)
        self.assertEqual(CoreServices.kLSDataUnavailableErr, -10813)
        self.assertEqual(CoreServices.kLSApplicationNotFoundErr, -10814)
        self.assertEqual(CoreServices.kLSUnknownTypeErr, -10815)
        self.assertEqual(CoreServices.kLSDataTooOldErr, -10816)
        self.assertEqual(CoreServices.kLSDataErr, -10817)
        self.assertEqual(CoreServices.kLSLaunchInProgressErr, -10818)
        self.assertEqual(CoreServices.kLSNotRegisteredErr, -10819)
        self.assertEqual(CoreServices.kLSAppDoesNotClaimTypeErr, -10820)
        self.assertEqual(CoreServices.kLSAppDoesNotSupportSchemeWarning, -10821)
        self.assertEqual(CoreServices.kLSServerCommunicationErr, -10822)
        self.assertEqual(CoreServices.kLSCannotSetInfoErr, -10823)
        self.assertEqual(CoreServices.kLSNoRegistrationInfoErr, -10824)
        self.assertEqual(CoreServices.kLSIncompatibleSystemVersionErr, -10825)
        self.assertEqual(CoreServices.kLSNoLaunchPermissionErr, -10826)
        self.assertEqual(CoreServices.kLSNoExecutableErr, -10827)
        self.assertEqual(CoreServices.kLSNoClassicEnvironmentErr, -10828)
        self.assertEqual(CoreServices.kLSMultipleSessionsNotSupportedErr, -10829)
        self.assertEqual(CoreServices.kLSInitializeDefaults, 0x00000001)
        self.assertEqual(CoreServices.kLSMinCatInfoBitmap, 6154)
        self.assertEqual(CoreServices.kLSRequestExtension, 0x00000001)
        self.assertEqual(CoreServices.kLSRequestTypeCreator, 0x00000002)
        self.assertEqual(CoreServices.kLSRequestBasicFlagsOnly, 0x00000004)
        self.assertEqual(CoreServices.kLSRequestAppTypeFlags, 0x00000008)
        self.assertEqual(CoreServices.kLSRequestAllFlags, 0x00000010)
        self.assertEqual(CoreServices.kLSRequestIconAndKind, 0x00000020)
        self.assertEqual(CoreServices.kLSRequestExtensionFlagsOnly, 0x00000040)
        self.assertEqual(CoreServices.kLSRequestAllInfo, 0xFFFFFFFF)
        self.assertEqual(CoreServices.kLSItemInfoIsPlainFile, 0x00000001)
        self.assertEqual(CoreServices.kLSItemInfoIsPackage, 0x00000002)
        self.assertEqual(CoreServices.kLSItemInfoIsApplication, 0x00000004)
        self.assertEqual(CoreServices.kLSItemInfoIsContainer, 0x00000008)
        self.assertEqual(CoreServices.kLSItemInfoIsAliasFile, 0x00000010)
        self.assertEqual(CoreServices.kLSItemInfoIsSymlink, 0x00000020)
        self.assertEqual(CoreServices.kLSItemInfoIsInvisible, 0x00000040)
        self.assertEqual(CoreServices.kLSItemInfoIsNativeApp, 0x00000080)
        self.assertEqual(CoreServices.kLSItemInfoIsClassicApp, 0x00000100)
        self.assertEqual(CoreServices.kLSItemInfoAppPrefersNative, 0x00000200)
        self.assertEqual(CoreServices.kLSItemInfoAppPrefersClassic, 0x00000400)
        self.assertEqual(CoreServices.kLSItemInfoAppIsScriptable, 0x00000800)
        self.assertEqual(CoreServices.kLSItemInfoIsVolume, 0x00001000)
        self.assertEqual(CoreServices.kLSItemInfoExtensionIsHidden, 0x00100000)
        self.assertEqual(CoreServices.kLSRolesNone, 0x00000001)
        self.assertEqual(CoreServices.kLSRolesViewer, 0x00000002)
        self.assertEqual(CoreServices.kLSRolesEditor, 0x00000004)
        self.assertEqual(CoreServices.kLSRolesShell, 0x00000008)
        self.assertEqual(CoreServices.kLSRolesAll, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(CoreServices.kLSUnknownKindID, 0)
        self.assertEqual(CoreServices.kLSUnknownType, 0)
        self.assertEqual(CoreServices.kLSUnknownCreator, 0)
        self.assertEqual(CoreServices.kLSAcceptDefault, 0x00000001)
        self.assertEqual(CoreServices.kLSAcceptAllowLoginUI, 0x00000002)

        self.assertIsInstance(CoreServices.kLSItemContentType, unicode)
        self.assertIsInstance(CoreServices.kLSItemFileType, unicode)
        self.assertIsInstance(CoreServices.kLSItemFileCreator, unicode)
        self.assertIsInstance(CoreServices.kLSItemExtension, unicode)
        self.assertIsInstance(CoreServices.kLSItemDisplayName, unicode)
        self.assertIsInstance(CoreServices.kLSItemDisplayKind, unicode)
        self.assertIsInstance(CoreServices.kLSItemRoleHandlerDisplayName, unicode)
        self.assertIsInstance(CoreServices.kLSItemIsInvisible, unicode)
        self.assertIsInstance(CoreServices.kLSItemExtensionIsHidden, unicode)
        self.assertIsInstance(CoreServices.kLSItemQuarantineProperties, unicode)

        self.assertEqual(CoreServices.kLSHandlerOptionsDefault, 0)
        self.assertEqual(CoreServices.kLSHandlerOptionsIgnoreCreator, 1)

    def testStructs(self):
        v = CoreServices.LSItemInfoRecord()
        self.assertHasAttr(v, "flags")
        self.assertHasAttr(v, "filetype")
        self.assertHasAttr(v, "creator")
        self.assertHasAttr(v, "extension")
        if sys.maxsize < 2 ** 32:
            self.assertHasAttr(v, "iconFileName")
            self.assertHasAttr(v, "kindID")
        else:
            self.assertNotHasAttr(v, "iconFileName")
            self.assertNotHasAttr(v, "kindID")

    def testFunctions(self):
        CoreServices.LSInit(CoreServices.kLSInitializeDefaults)
        CoreServices.LSTerm()

        url = CoreServices.CFURLCreateFromFileSystemRepresentation(
            None, self.bpath, len(self.bpath), True
        )
        self.assertIsInstance(url, CoreServices.CFURLRef)

        ok, info = CoreServices.LSCopyItemInfoForURL(
            url,
            CoreServices.kLSRequestExtension | CoreServices.kLSRequestTypeCreator,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, CoreServices.LSItemInfoRecord)

        self.assertArgIsOut(CoreServices.LSGetExtensionInfo, 2)
        ok, info = CoreServices.LSGetExtensionInfo(len(self.path), self.path, None)
        self.assertEqual(ok, 0)
        self.assertEqual(info, self.path.rindex(".") + 1)

        self.assertArgIsOut(CoreServices.LSCopyDisplayNameForURL, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyDisplayNameForURL, 1)
        ok, info = CoreServices.LSCopyDisplayNameForURL(url, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsBOOL(CoreServices.LSSetExtensionHiddenForURL, 1)
        ok = CoreServices.LSSetExtensionHiddenForURL(url, True)
        self.assertEqual(ok, 0)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForURL, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForURL, 1)
        ok, info = CoreServices.LSCopyKindStringForURL(url, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForTypeInfo, 3)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForTypeInfo, 3)
        ok, info = CoreServices.LSCopyKindStringForTypeInfo(
            CoreServices.kLSUnknownType, CoreServices.kLSUnknownCreator, "jpg", None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForMIMEType, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForMIMEType, 1)
        ok, info = CoreServices.LSCopyKindStringForMIMEType("text/plain", None)
        self.assertIsInstance(ok, (int, long))
        # XXX: For some reason this fails sometimes...
        # self.assertEqual(ok, 0)
        self.assertIsInstance(info, (unicode, type(None)))

        self.assertArgIsOut(CoreServices.LSGetApplicationForInfo, 4)
        self.assertArgIsOut(CoreServices.LSGetApplicationForInfo, 5)
        self.assertArgIsCFRetained(CoreServices.LSGetApplicationForInfo, 5)

        ok, ref, info_url = CoreServices.LSGetApplicationForInfo(
            CoreServices.kLSUnknownType,
            CoreServices.kLSUnknownCreator,
            "txt",
            CoreServices.kLSRolesAll,
            None,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSCopyApplicationForMIMEType, 2)
        self.assertArgIsCFRetained(CoreServices.LSCopyApplicationForMIMEType, 2)
        ok, info_url = CoreServices.LSCopyApplicationForMIMEType(
            "text/plain", CoreServices.kLSRolesAll, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSGetApplicationForURL, 2)
        self.assertArgIsOut(CoreServices.LSGetApplicationForURL, 3)
        self.assertArgIsCFRetained(CoreServices.LSGetApplicationForURL, 3)
        ok, ref, info_url = CoreServices.LSGetApplicationForURL(
            url, CoreServices.kLSRolesAll, None, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSFindApplicationForInfo, 3)
        self.assertArgIsOut(CoreServices.LSFindApplicationForInfo, 4)
        self.assertArgIsCFRetained(CoreServices.LSFindApplicationForInfo, 4)
        ok, ref, info_url = CoreServices.LSFindApplicationForInfo(
            CoreServices.kLSUnknownCreator, None, "foo.app", None, None
        )
        # XXX: The code looks correct but fails, however the corresponding C code also fails.
        # self.assertEqual(ok, 0)
        self.assertIsInstance(ok, (int, long))
        if ref is not None:
            self.assertIsInstance(ref, objc.FSRef)
        if info_url is not None:
            self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSCanURLAcceptURL, 4)
        ok, status = CoreServices.LSCanURLAcceptURL(
            url, url, CoreServices.kLSRolesAll, CoreServices.kLSAcceptDefault, None
        )
        self.assertIsInstance(ok, (int, long))
        self.assertIsInstance(status, bool)

        ok = CoreServices.LSRegisterURL(url, False)
        self.assertIsInstance(ok, (int, long))

        v = CoreServices.LSCopyApplicationURLsForURL(url, CoreServices.kLSRolesAll)
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, CoreServices.CFURLRef)

        default_role = CoreServices.LSCopyDefaultRoleHandlerForContentType(
            "public.plain-text", CoreServices.kLSRolesAll
        )
        if os_level_key(os_release()) < os_level_key("10.7"):
            if default_role is not None:
                self.assertIsInstance(default_role, unicode)
        else:
            self.assertIsInstance(default_role, unicode)

        v = CoreServices.LSCopyAllRoleHandlersForContentType(
            "public.plain-text", CoreServices.kLSRolesAll
        )
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, unicode)

        ok = CoreServices.LSSetDefaultRoleHandlerForContentType(
            "public.plain-text", CoreServices.kLSRolesAll, default_role
        )
        self.assertIsInstance(ok, (int, long))

        v = CoreServices.LSGetHandlerOptionsForContentType("public.plain-text")
        self.assertIsInstance(v, (int, long))

        ok = CoreServices.LSSetHandlerOptionsForContentType("public.plain-text", v)
        self.assertIsInstance(ok, (int, long))

        self.assertResultIsCFRetained(CoreServices.LSCopyDefaultHandlerForURLScheme)
        default_handler = CoreServices.LSCopyDefaultHandlerForURLScheme("http")
        if os_level_key(os_release()) < os_level_key("10.7"):
            if default_handler is not None:
                self.assertIsInstance(default_handler, unicode)
        else:
            self.assertIsInstance(default_handler, unicode)

        self.assertResultIsCFRetained(CoreServices.LSCopyAllHandlersForURLScheme)
        v = CoreServices.LSCopyAllHandlersForURLScheme("http")
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, unicode)

        ok = CoreServices.LSSetDefaultHandlerForURLScheme("http", default_handler)
        self.assertIsInstance(ok, (int, long))

    def testFSRef(self):
        ref = objc.FSRef.from_pathname(self.path)
        self.assertIsInstance(ref, objc.FSRef)

        ok, info = CoreServices.LSCopyItemInfoForRef(
            ref,
            CoreServices.kLSRequestExtension | CoreServices.kLSRequestTypeCreator,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, CoreServices.LSItemInfoRecord)

        self.assertArgIsOut(CoreServices.LSCopyDisplayNameForRef, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyDisplayNameForRef, 1)
        ok, info = CoreServices.LSCopyDisplayNameForRef(ref, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsBOOL(CoreServices.LSSetExtensionHiddenForRef, 1)
        ok = CoreServices.LSSetExtensionHiddenForRef(ref, True)
        self.assertEqual(ok, 0)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForRef, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForRef, 1)
        ok, info = CoreServices.LSCopyKindStringForRef(ref, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsOut(CoreServices.LSGetApplicationForItem, 2)
        self.assertArgIsOut(CoreServices.LSGetApplicationForItem, 3)
        self.assertArgIsCFRetained(CoreServices.LSGetApplicationForItem, 3)
        ok, info_ref, info_url = CoreServices.LSGetApplicationForItem(
            ref, CoreServices.kLSRolesAll, None, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info_ref, objc.FSRef)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        if os.path.exists("/Applications/TextEdit.app"):
            app_ref = objc.FSRef.from_pathname("/Applications/TextEdit.app")
        else:
            app_ref = objc.FSRef.from_pathname("/System/Applications/TextEdit.app")
        self.assertArgIsOut(CoreServices.LSCanRefAcceptItem, 4)
        ok, accepts = CoreServices.LSCanRefAcceptItem(
            ref, app_ref, CoreServices.kLSRolesAll, CoreServices.kLSAcceptDefault, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(accepts, bool)

        ok = CoreServices.LSRegisterFSRef(ref, False)
        self.assertIsInstance(ok, (int, long))

        self.assertArgHasType(CoreServices.LSCopyItemAttribute, 3, b"o^@")
        ok, value = CoreServices.LSCopyItemAttribute(
            ref, CoreServices.kLSRolesAll, CoreServices.kLSItemExtensionIsHidden, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(value, bool)

        ok = CoreServices.LSSetItemAttribute(
            ref,
            CoreServices.kLSRolesAll,
            CoreServices.kLSItemRoleHandlerDisplayName,
            b"foo".decode("latin1"),
        )
        self.assertIsInstance(ok, (int, long))

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(CoreServices.LSCopyDefaultApplicationURLForURL)
        self.assertArgIsOut(CoreServices.LSCopyDefaultApplicationURLForURL, 2)

        self.assertResultIsCFRetained(
            CoreServices.LSCopyDefaultApplicationURLForContentType
        )
        self.assertArgIsOut(CoreServices.LSCopyDefaultApplicationURLForContentType, 2)

        self.assertResultIsCFRetained(
            CoreServices.LSCopyApplicationURLsForBundleIdentifier
        )
        self.assertArgIsOut(CoreServices.LSCopyApplicationURLsForBundleIdentifier, 1)


if __name__ == "__main__":
    main()
