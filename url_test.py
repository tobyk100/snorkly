import unittest
import dpkt, os
import utilities, bad_traffic


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

    def test_simple_good_traffic(self):
        ip = self.eth[0].data
        tcp = ip.data
        res = bad_traffic.land_attack(ip, tcp)
        self.assertEqual(res[0], 0.0)

    def test_simple_bad_traffic(self):
        ip = self.eth[0].data
        tcp = ip.data
        ip.src = ip.dst
        tcp.sport = tcp.dport
        res = bad_traffic.land_attack(ip, tcp)
        self.assertEqual(res[0], 1.0)



if __name__ == '__main__':
    unittest.main()
