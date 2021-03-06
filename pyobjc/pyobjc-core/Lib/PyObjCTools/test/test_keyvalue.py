"""
Tests for PyObjCTools.KeyValueCoding

TODO:
    - Accessing properties in superclass of ObjC hybrids (see also Foundation.test.test_keyvalue)

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in objc.test.test_keyvalue and Foundation.test.test_keyvalue.
"""

from PyObjCTools.KeyValueCoding import *
from objc.test.keyvaluehelper import *
import objc
import unittest
from objc.test import ctests
from Foundation import *
import datetime


class KeyValueClass5(object):
    def __init__(self):
        self.key3 = 3
        self._key4 = "4"
        self.__private = "private"

    def addMultiple(self):
        self.multiple = KeyValueClass5()
        self.multiple.level2 = KeyValueClass5()
        self.multiple.level2.level3 = KeyValueClass5()
        self.multiple.level2.level3.keyA = "hello"
        self.multiple.level2.level3.keyB = "world"

    def getKey1(self):
        return 1

    def get_key2(self):
        return 2

    def setKey4(self, value):
        self._key4 = value * 4

    def set_key5(self, value):
        self.key5 = value * 5


class KeyValueClass6(object):
    __slots__ = ("foo",)

    def __init__(self):
        self.foo = "foobar"

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar(self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: "read-only")


class KeyValueClass7(NSObject):
    def init(self):
        self = super(KeyValueClass7, self).init()
        self.key3 = 3
        self._key4 = "4"
        self.__private = "private"
        return self

    def addMultiple(self):
        self.multiple = KeyValueClass5()
        self.multiple.level2 = KeyValueClass5()
        self.multiple.level2.level3 = KeyValueClass5()
        self.multiple.level2.level3.keyA = "hello"
        self.multiple.level2.level3.keyB = "world"

    def getKey1(self):
        return 1

    def key2(self):
        return 2

    def setKey4_(self, value):
        self._key4 = value * 4

    def setKey5_(self, value):
        self.key5 = value * 5

    def keyM(self):
        return "m"


class KeyValueClass8(NSObject):
    __slots__ = ("foo",)

    def init(self):
        self = super(KeyValueClass8, self).init()
        self.foo = "foobar"
        return self

    # Definition for property 'bar'. Use odd names for the methods
    # because the KeyValue support recognizes the usual names.
    def read_bar(self):
        return self.foo + self.foo

    def write_bar(self, value):
        self.foo = value + value

    bar = property(read_bar, write_bar)

    roprop = property(lambda self: "read-only")


class PyKeyValueCoding(unittest.TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.

        o = KeyValueClass5()
        self.assertRaises(KeyError, getKey, o, "private")

    def testValueForKey(self):
        o = KeyValueClass5()
        o.addMultiple()

        self.assertEquals(getKey(o, "key1"), 1)
        self.assertEquals(getKey(o, "key2"), 2)
        self.assertEquals(getKey(o, "key3"), 3)
        self.assertEquals(getKey(o, "key4"), "4")
        self.assertEquals(getKey(o, "multiple"), o.multiple)

        self.assertRaises(KeyError, getKey, o, "nokey")

    def testValueForKey2(self):
        o = KeyValueClass6()

        self.assertEquals(getKey(o, "foo"), "foobar")
        self.assertEquals(getKey(o, "bar"), "foobarfoobar")
        self.assertEquals(getKey(o, "roprop"), "read-only")

    def testValueForKeyPath(self):
        o = KeyValueClass5()
        o.addMultiple()

        self.assertEquals(getKeyPath(o, "multiple"), o.multiple)
        self.assertEquals(getKeyPath(o, "multiple.level2"), o.multiple.level2)
        self.assertEquals(
            getKeyPath(o, "multiple.level2.level3.keyA"), o.multiple.level2.level3.keyA
        )
        self.assertEquals(
            getKeyPath(o, "multiple.level2.level3.keyB"), o.multiple.level2.level3.keyB
        )

        self.assertRaises(KeyError, getKeyPath, o, "multiple.level2.nokey")

    def testTakeValueForKey(self):
        o = KeyValueClass5()

        self.assertEquals(o.key3, 3)
        setKey(o, "key3", "drie")
        self.assertEquals(o.key3, "drie")

        self.assertEquals(o._key4, "4")
        setKey(o, "key4", "vier")
        self.assertEquals(o._key4, "viervierviervier")

        o.key5 = 1
        setKey(o, "key5", "V")
        self.assertEquals(o.key5, "VVVVV")

        self.assert_(not hasattr(o, "key9"))
        setKey(o, "key9", "IX")
        self.assert_(hasattr(o, "key9"))
        self.assertEquals(o.key9, "IX")

    def testTakeValueForKey2(self):
        o = KeyValueClass6()

        self.assertEquals(o.foo, "foobar")
        setKey(o, "foo", "FOO")
        self.assertEquals(o.foo, "FOO")

        self.assertRaises(KeyError, setKey, o, "key9", "IX")

    def testTakeValueForKeyPath(self):
        o = KeyValueClass5()
        o.addMultiple()

        self.assertEquals(o.multiple.level2.level3.keyA, "hello")
        self.assertEquals(o.multiple.level2.level3.keyB, "world")

        setKeyPath(o, "multiple.level2.level3.keyA", "KeyAValue")
        self.assertEquals(o.multiple.level2.level3.keyA, "KeyAValue")

        setKeyPath(o, "multiple.level2.level3.keyB", 9.999)
        self.assertEquals(o.multiple.level2.level3.keyB, 9.999)


class OcKeyValueCoding(unittest.TestCase):
    def testNoPrivateVars(self):
        # Private instance variables ('anObject.__value') are not accessible using
        # key-value coding.

        o = KeyValueClass7.alloc().init()
        self.assertRaises(KeyError, getKey, o, "private")

    def testArrayValueForKey(self):
        o = KeyValueClass7.alloc().init()
        o.addMultiple()

        self.assertEquals(getKey(o, "key1"), 1)
        self.assertEquals(getKey(o, "key2"), 2)
        self.assertEquals(getKey(o, "key3"), 3)
        self.assertEquals(getKey(o, "key4"), "4")
        self.assertEquals(getKey(o, "multiple"), o.multiple)

        self.assertEquals(o.valueForKey_("keyM"), "m")

        a = NSMutableArray.array()
        a.addObject_(o)
        a.addObject_({"keyM": "5"})
        a.addObject_(NSDictionary.dictionaryWithObject_forKey_("foo", "keyM"))
        b = NSMutableArray.arrayWithObjects_("m", "5", "foo", None)

        # See Modules/objc/unittest.m for an explantion of this test
        try:
            ctests.TestArrayCoding()
            arrayObservingWorks = True
        except AssertionError:
            arrayObservingWorks = False

        if arrayObservingWorks:
            self.assertEquals(a.valueForKey_("keyM"), b)
        else:
            self.assertRaises(KeyError, a.valueForKey_, "keyM")

        self.assertRaises(KeyError, getKey, o, "nokey")

    def testValueForKey2(self):
        o = KeyValueClass8.alloc().init()

        self.assertEquals(getKey(o, "foo"), "foobar")
        self.assertEquals(getKey(o, "bar"), "foobarfoobar")
        self.assertEquals(getKey(o, "roprop"), "read-only")

    def testValueForKeyPath(self):
        o = KeyValueClass7.alloc().init()
        o.addMultiple()

        self.assertEquals(getKeyPath(o, "multiple"), o.multiple)
        self.assertEquals(getKeyPath(o, "multiple.level2"), o.multiple.level2)
        self.assertEquals(
            getKeyPath(o, "multiple.level2.level3.keyA"), o.multiple.level2.level3.keyA
        )
        self.assertEquals(
            getKeyPath(o, "multiple.level2.level3.keyB"), o.multiple.level2.level3.keyB
        )

        self.assertRaises(KeyError, getKeyPath, o, "multiple.level2.nokey")

    def testTakeValueForKey(self):
        o = KeyValueClass7.alloc().init()

        self.assertEquals(o.key3, 3)
        setKey(o, "key3", "drie")
        self.assertEquals(o.key3, "drie")

        self.assertEquals(o._key4, "4")
        setKey(o, "key4", "vier")
        self.assertEquals(o._key4, "viervierviervier")

        o.key5 = 1
        setKey(o, "key5", "V")
        self.assertEquals(o.key5, "VVVVV")

        self.assert_(not hasattr(o, "key9"))
        setKey(o, "key9", "IX")
        self.assert_(hasattr(o, "key9"))
        self.assertEquals(o.key9, "IX")

    def testTakeValueForKey2(self):
        o = KeyValueClass8.alloc().init()

        self.assertEquals(o.foo, "foobar")
        setKey(o, "foo", "FOO")
        self.assertEquals(o.foo, "FOO")

        self.assertRaises(KeyError, setKey, o, "key9", "IX")

    def testTakeValueForKeyPath(self):
        o = KeyValueClass7.alloc().init()
        o.addMultiple()

        self.assertEquals(o.multiple.level2.level3.keyA, "hello")
        self.assertEquals(o.multiple.level2.level3.keyB, "world")

        setKeyPath(o, "multiple.level2.level3.keyA", "KeyAValue")
        self.assertEquals(o.multiple.level2.level3.keyA, "KeyAValue")

        setKeyPath(o, "multiple.level2.level3.keyB", 9.999)
        self.assertEquals(o.multiple.level2.level3.keyB, 9.999)


class MethodsAsKeys(unittest.TestCase):
    def testStrCap(self):
        s = "hello"

        self.assertEquals(getKey(s, "capitalize"), "Hello")


class AbstractKVCodingTest:
    def testBaseValueForKey(self):
        self.assertEquals(DirectString, getKey(self.base, "directString"))
        self.assertEquals(IndirectString, getKey(self.base, "indirectString"))
        self.assertEquals(DirectNumber, getKey(self.base, "directNumber"))
        self.assertEquals(IndirectNumber, getKey(self.base, "indirectNumber"))

    def testPathValueForKey(self):
        self.assertEquals(
            DirectString, getKeyPath(self.path, "directHead.directString")
        )
        self.assertEquals(
            DirectString, getKeyPath(self.path, "indirectHead.directString")
        )
        self.assertEquals(
            IndirectString, getKeyPath(self.path, "directHead.indirectString")
        )
        self.assertEquals(
            IndirectString, getKeyPath(self.path, "indirectHead.indirectString")
        )
        self.assertEquals(
            DirectNumber, getKeyPath(self.path, "directHead.directNumber")
        )
        self.assertEquals(
            DirectNumber, getKeyPath(self.path, "indirectHead.directNumber")
        )
        self.assertEquals(
            IndirectNumber, getKeyPath(self.path, "directHead.indirectNumber")
        )
        self.assertEquals(
            IndirectNumber, getKeyPath(self.path, "indirectHead.indirectNumber")
        )


class TestObjCKVCoding(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = PyObjCTest_KVBaseClass.new()
        self.path = PyObjCTest_KVPathClass.new()


class TestPythonKVCoding(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVPyBase()
        self.path = KVPyPath()


class TestPythonSubObjCContainerCoding(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVPySubObjCBase.new()
        self.path = KVPySubObjCPath.new()


class TestPythonSubOverObjC(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVPySubOverObjCBase.new()
        self.path = KVPySubOverObjCPath.new()

    def testOverValueKey(self):
        self.assertEquals(DirectString, getKey(self.base, "overDirectString"))
        self.assertEquals(IndirectString, getKey(self.base, "overIndirectString"))

    def testOverValueKeyPath(self):
        self.assertEquals(
            DirectString, getKeyPath(self.path, "overDirectHead.directString")
        )
        self.assertEquals(
            DirectString, getKeyPath(self.path, "overIndirectHead.directString")
        )
        self.assertEquals(
            IndirectString, getKeyPath(self.path, "overDirectHead.indirectString")
        )
        self.assertEquals(
            IndirectString, getKeyPath(self.path, "overIndirectHead.indirectString")
        )


class Account(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)


class Transaction(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)


class PyObjCAccount(NSObject):
    openingBalance = objc.ivar("openingBalance", "d")
    name = objc.ivar("name")
    notes = objc.ivar("notes")
    transactions = objc.ivar("transactions")

    def __new__(cls, **kw):
        self = cls.alloc().init()
        for k, v in kw.iteritems():
            setattr(self, k, v)
        return self


class PyObjCTransaction(NSObject):
    referenceNumber = objc.ivar("referenceNumber", "I")
    amount = objc.ivar("amount", "d")
    payee = objc.ivar("payee")
    date = objc.ivar("date")
    category = objc.ivar("category")
    reconciled = objc.ivar(objc._C_BOOL)

    def __new__(cls, **kw):
        self = cls.alloc().init()
        for k, v in kw.iteritems():
            setattr(self, k, v)
        return self


def makeAccounts(Account, Transaction):
    return [
        Account(
            openingBalance=10.0,
            name="Alice",
            notes="Alice notes",
            transactions=[
                Transaction(
                    referenceNumber=1,
                    amount=20.0,
                    payee="Bob",
                    date=datetime.date(2005, 1, 1),
                    category="Tacos",
                    reconciled=True,
                ),
                Transaction(
                    referenceNumber=2,
                    amount=14.50,
                    payee="George",
                    date=datetime.date(2005, 1, 2),
                    category="Bagels",
                    reconciled=True,
                ),
                Transaction(
                    referenceNumber=3,
                    amount=250,
                    payee="Bill",
                    date=datetime.date(2005, 1, 3),
                    category="Tequila",
                    reconciled=True,
                ),
            ],
        ),
        Account(
            openingBalance=10.0,
            name="Bob",
            notes="Bob notes",
            transactions=[
                Transaction(
                    referenceNumber=4,
                    amount=25.0,
                    payee="Alice",
                    date=datetime.date(2005, 1, 4),
                    category="Beer",
                    reconciled=True,
                ),
                Transaction(
                    referenceNumber=5,
                    amount=60.0,
                    payee="George",
                    date=datetime.date(2005, 1, 5),
                    category="Book",
                    reconciled=True,
                ),
                Transaction(
                    referenceNumber=6,
                    amount=250,
                    payee="Bill",
                    date=datetime.date(2005, 1, 6),
                    category="Tequila",
                    reconciled=True,
                ),
            ],
        ),
    ]


class TestArrayOperators(unittest.TestCase):
    def setUp(self):
        self.accounts = makeAccounts(Account, Transaction)

    def testCount(self):
        self.assertEquals(getKeyPath(self, "accounts.@count"), 2)
        self.assertEquals(getKeyPath(self, "accounts.transactions.@count"), 2)
        self.assertEquals(getKeyPath(self.accounts, "@count"), 2)
        self.assertEquals(getKeyPath(self.accounts[0], "transactions.@count"), 3)
        self.assertEquals(getKeyPath(self.accounts[1], "transactions.@count"), 3)

    def testDistinctUnionOfArrays(self):
        self.assertEquals(
            getKeyPath(self.accounts, "@distinctUnionOfArrays.transactions.payee"),
            ["Bob", "George", "Bill", "Alice"],
        )
        self.assertEquals(
            getKeyPath(
                self.accounts, "@distinctUnionOfArrays.transactions.referenceNumber"
            ),
            [1, 2, 3, 4, 5, 6],
        )
        self.assertEquals(
            getKeyPath(self.accounts, "@distinctUnionOfArrays.transactions.category"),
            ["Tacos", "Bagels", "Tequila", "Beer", "Book"],
        )

    def testDistinctUnionOfObjects(self):
        alice = self.accounts[0]
        v = getKeyPath(alice, "transactions.@distinctUnionOfObjects.payee")

        def assertSameUnion(a, b):
            a = list(a)
            b = list(b)
            a.sort()
            b.sort()
            self.assertEquals(a, b)

        assertSameUnion(
            getKeyPath(alice, "transactions.@distinctUnionOfObjects.payee"),
            ["Bill", "Bob", "George"],
        )
        assertSameUnion(
            getKeyPath(alice, "transactions.@distinctUnionOfObjects.referenceNumber"),
            [1, 2, 3],
        )
        assertSameUnion(
            getKeyPath(alice, "transactions.@distinctUnionOfObjects.reconciled"), [True]
        )

    def testMax(self):
        alice = self.accounts[0]
        self.assertEquals(
            getKeyPath(alice, "transactions.@max.date"), datetime.date(2005, 1, 3)
        )
        self.assertEquals(getKeyPath(alice, "transactions.@max.referenceNumber"), 3)
        self.assertEquals(getKeyPath(alice, "transactions.@max.amount"), 250)

    def testMin(self):
        alice = self.accounts[0]
        self.assertEquals(
            getKeyPath(alice, "transactions.@min.date"), datetime.date(2005, 1, 1)
        )
        self.assertEquals(getKeyPath(alice, "transactions.@min.referenceNumber"), 1)
        self.assertEquals(getKeyPath(alice, "transactions.@min.amount"), 14.50)

    def testSum(self):
        alice = self.accounts[0]
        self.assertEquals(
            getKeyPath(alice, "transactions.@sum.amount"), 20 + 14.50 + 250
        )
        bob = self.accounts[1]
        self.assertEquals(getKeyPath(bob, "transactions.@sum.amount"), 25 + 60 + 250)

    def testUnionOfArrays(self):
        self.assertEquals(
            getKeyPath(self.accounts, "@unionOfArrays.transactions.payee"),
            ["Bob", "George", "Bill", "Alice", "George", "Bill"],
        )
        self.assertEquals(
            getKeyPath(self.accounts, "@unionOfArrays.transactions.referenceNumber"),
            [1, 2, 3, 4, 5, 6],
        )
        self.assertEquals(
            getKeyPath(self.accounts, "@unionOfArrays.transactions.category"),
            ["Tacos", "Bagels", "Tequila", "Beer", "Book", "Tequila"],
        )

    def testUnionOfObjects(self):
        alice = self.accounts[0]
        self.assertEquals(
            getKeyPath(alice, "transactions.@unionOfObjects.payee"),
            ["Bob", "George", "Bill"],
        )
        self.assertEquals(
            getKeyPath(alice, "transactions.@unionOfObjects.referenceNumber"), [1, 2, 3]
        )
        self.assertEquals(
            getKeyPath(alice, "transactions.@unionOfObjects.reconciled"),
            [True, True, True],
        )


class TestPyObjCArrayOperators(TestArrayOperators):
    def setUp(self):
        self.accounts = makeAccounts(PyObjCAccount, PyObjCTransaction)


if __name__ == "__main__":
    unittest.main()
