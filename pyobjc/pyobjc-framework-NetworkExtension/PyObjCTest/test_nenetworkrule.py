from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNENetworkRule(TestCase):
        def test_constants(self):
            self.assertEqual(NetworkExtension.NENetworkRuleProtocolAny, 0)
            self.assertEqual(NetworkExtension.NENetworkRuleProtocolTCP, 1)
            self.assertEqual(NetworkExtension.NENetworkRuleProtocolUDP, 2)

            self.assertEqual(NetworkExtension.NETrafficDirectionAny, 0)
            self.assertEqual(NetworkExtension.NETrafficDirectionInbound, 1)
            self.assertEqual(NetworkExtension.NETrafficDirectionOutbound, 2)


if __name__ == "__main__":
    main()
