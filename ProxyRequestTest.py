__author__ = 'user'

import ProxyRequest

def Test_SucceedSSL():

    value, message = ProxyRequest.Request('https://www.google.com/', '/')
    print value, message

def Test_FailSSL():
    value, message = ProxyRequest.Request('https://web4.alexfrazer.us:10000/', '/')
    print value, message

def Test_FailNoSSL():
    value, message = ProxyRequest.Request('http://www.abc123kdfhaksdhfkjabjhbdjshasd.com', '/')
    print value, message

def Test_SucceedNoSSL():
    value, message = ProxyRequest.Request('http://www.cnn.com', '/')
    print value, message

Test_SucceedSSL()
Test_FailSSL()
Test_FailNoSSL()
Test_SucceedNoSSL()
