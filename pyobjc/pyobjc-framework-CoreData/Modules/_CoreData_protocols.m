/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1012
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(NSFetchedResultsControllerDelegate));
    Py_XDECREF(p);
#endif
}
