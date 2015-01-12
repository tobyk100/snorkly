import unittest
import dpkt, os
import utilities


class TestUrl(unittest.TestCase):
    def setUp(self):
        f = open(os.path.join('sample_pcaps', 'http.cap'), 'rb')
        pcap = dpkt.pcap.Reader(f)
        self.eth = [dpkt.ethernet.Ethernet(buf) for ts, buf in pcap]
        f.close()

    def test_http_parser(self):
        http = utilities.get_http_request(self.eth[3])
        self.assertIsNotNone(http)

        http = utilities.get_http_request(self.eth[5])
        self.assertIsNone(http)

    def test_url_extractor(self):
        uri = utilities.extract_url(self.eth[3])
        self.assertEqual(uri, 'www.ethereal.com/download.html')


if __name__ == '__main__':
    unittest.main()
