import unittest
import dpkt, os
from url_extractor import UrlExtractor


class TestUrl(unittest.TestCase):
    def setUp(self):
        f = open(os.path.join('sample_pcaps', 'http.cap'), 'rb')
        pcap = dpkt.pcap.Reader(f)
        self.eth = [dpkt.ethernet.Ethernet(buf) for ts, buf in pcap]
        f.close()

    def test_url_extractor(self):
        # Todo(toby): implement test
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
