import urllib2
import time


class URL:

    def __init__(self, url):
        proxy = urllib2.ProxyHandler({'http': 'usr:pass@172.31.1.6:8080', 'https': 'usr:404104211@172.31.1.6:8080'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        self.url = url

    def fetch(self):
        print 'Attempting url fetch.'
        OK = False
        tries = 0
        while not OK:
            try:
                response = urllib2.urlopen(self.url)
                print 'Success : ' + self.url
                OK = True
            except urllib2.HTTPError as e:
                tries = tries + 1
                if tries >= 256:
                    return -1
                print 'Failure.\nAn HTTP error occured : ' + str(e.code)
                print 'Refetching : ' + self.url
        data = response.read()
        return data
