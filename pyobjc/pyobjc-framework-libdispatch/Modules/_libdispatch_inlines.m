#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <dispatch/dispatch.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability"

static PyObjC_function_map function_map[] = {
    {"dispatch_get_main_queue", (PyObjC_Function_Pointer)&dispatch_get_main_queue},
    {0, 0}};

#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
#if PY_MAJOR_VERSION == 3

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_inlines", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__inlines(void);

PyObject*
PyInit__inlines(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_inlines(void);

void
init_inlines(void)
#endif
{
    PyObject* m;
#if PY_MAJOR_VERSION == 3
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("_inlines", mod_methods, NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) <
        0) {
        INITERROR();
    }

    INITDONE();
}
