import unittest
import pcap, dpkt, os


class TestUrl(unittest.TestCase):
    def setUp(self):
        f = open(os.path.join('sample_pcaps', 'test.pcap'), 'rb')
        pcap = dpkt.pcap.Reader(f)
        eth = [dpkt.ethernet.Ethernet(buf) for ts, buf in pcap]
        f.close()

    def test_url_extractor(self):
        # Todo(toby): implement test
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
