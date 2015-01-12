__author__ = 'Alex Frazer'

# pip install urllib3

# pip install certifi


import urllib3
import certifi


def Request(HOST, URL):
    lURL = URL.lower()
    lHOST = HOST.lower()

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(), )

    try:
        r = http.request('GET', HOST)
        if (lHOST.startswith('https')):
            return 1, "Valid SSL Certificate"
        else:
            return 0.5, "Non-SSL Site, but still connects"
    except AttributeError as e:
        return 0, "Invalid SSL Certificate "
    except urllib3.exceptions.MaxRetryError:
        return 0, "URL Not Available"
