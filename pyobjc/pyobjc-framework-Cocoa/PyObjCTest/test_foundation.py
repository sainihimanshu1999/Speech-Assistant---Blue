"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import Foundation
import os


class TestFoundation(TestCase):
    def testValues(self):
        self.assertHasAttr(Foundation, "NSTimeIntervalSince1970")
        self.assertIsInstance(Foundation.NSTimeIntervalSince1970, float)
        self.assertEqual(Foundation.NSTimeIntervalSince1970, 978_307_200.0)

        if int(os.uname()[2].split(".")[0]) < 9:
            self.assertHasAttr(Foundation, "NSMaximumStringLength")
            self.assertIsInstance(Foundation.NSMaximumStringLength, (int, long))
        self.assertHasAttr(Foundation, "NSURLResponseUnknownLength")
        self.assertIsInstance(Foundation.NSURLResponseUnknownLength, (int, long))

    def testFunctions(self):
        self.assertHasAttr(Foundation, "NSStringFromSelector")

    def testProtocols(self):
        self.assertNotHasAttr(Foundation, "protocols")

    def test_structs(self):
        self.assertHasAttr(Foundation, "NSPoint")
        o = Foundation.NSPoint()
        self.assertHasAttr(o, "x")
        self.assertHasAttr(o, "y")

        self.assertHasAttr(Foundation, "NSSize")
        o = Foundation.NSSize()
        self.assertHasAttr(o, "width")
        self.assertHasAttr(o, "height")

        self.assertHasAttr(Foundation, "NSRange")
        o = Foundation.NSRange()
        self.assertHasAttr(o, "location")
        self.assertHasAttr(o, "length")

        self.assertHasAttr(Foundation, "NSRect")
        o = Foundation.NSRect()
        self.assertHasAttr(o, "origin")
        self.assertHasAttr(o, "size")
        self.assertIsInstance(o.origin, Foundation.NSPoint)
        self.assertIsInstance(o.size, Foundation.NSSize)

        self.assertHasAttr(Foundation, "NSAffineTransformStruct")
        o = Foundation.NSAffineTransformStruct()
        self.assertHasAttr(o, "m11")
        self.assertHasAttr(o, "m12")
        self.assertHasAttr(o, "m21")
        self.assertHasAttr(o, "m22")
        self.assertHasAttr(o, "tX")
        self.assertHasAttr(o, "tY")


if __name__ == "__main__":
    main()
