from PyObjCTools.TestSupport import *

import libdispatch


class TestObjectAPI(TestCase):
    @min_os_level("10.6")
    def test_functions(self):
        self.assertFalse(hasattr(libdispatch, "dispatch_retain"))
        self.assertFalse(hasattr(libdispatch, "dispatch_release"))

        self.assertResultHasType(
            libdispatch.dispatch_get_context, objc._C_PTR + objc._C_VOID
        )
        self.assertArgHasType(libdispatch.dispatch_get_context, 0, objc._C_ID)

        self.assertResultHasType(libdispatch.dispatch_set_context, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_set_context, 0, objc._C_ID)
        self.assertArgHasType(
            libdispatch.dispatch_set_context, 1, objc._C_PTR + objc._C_VOID
        )

        self.assertResultHasType(libdispatch.dispatch_set_finalizer_f, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_set_finalizer_f, 0, objc._C_ID)
        self.assertArgIsFunction(libdispatch.dispatch_set_finalizer_f, 1, b"v^v", 1)

        self.assertResultHasType(libdispatch.dispatch_suspend, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_suspend, 0, objc._C_ID)

        self.assertResultHasType(libdispatch.dispatch_resume, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_resume, 0, objc._C_ID)

        self.assertFalse(hasattr(libdispatch, "dispatch_wait"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(libdispatch.dispatch_wait, objc._C_LNG)
        # self.assertArgHasType(libdispatch.dispatch_wait, 0, objc._C_ID)
        # self.assertArgHasType(libdispatch.dispatch_wait, 1, objc._C_ULNGLNG)

        self.assertFalse(hasattr(libdispatch, "dispatch_notify"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(libdispatch.dispatch_notify, objc._C_VOID)
        # self.assertArgHasType(libdispatch.dispatch_notify, 0, objc._C_ID)
        # self.assertArgHasType(libdispatch.dispatch_notify, 1, objc._C_ID) # dispatch_object_t
        # self.assertArgIslock(libdispatch.dispatch_notify, 2, b'v')

        self.assertFalse(hasattr(libdispatch, "dispatch_cancel"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(libdispatch.dispatch_cancel, objc._C_VOID)
        # self.assertArgHasType(libdispatch.dispatch_cancel, 0, objc._C_ID)

        self.assertFalse(hasattr(libdispatch, "dispatch_testcancel"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(libdispatch.dispatch_testcancel, objc._C_LNG)
        # self.assertArgHasType(libdispatch.dispatch_testcancel, 0, objc._C_ID)

        self.assertFalse(hasattr(libdispatch, "dispatch_debug"))
        self.assertFalse(hasattr(libdispatch, "dispatch_debugv"))

    @min_os_level("10.12")
    def test_functions_10_12(self):
        self.assertResultHasType(libdispatch.dispatch_activate, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_activate, 0, objc._C_ID)


if __name__ == "__main__":
    main()
