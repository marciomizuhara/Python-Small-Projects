from __future__ import with_statement
from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib


def short_url(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    url_long = str(input('Insert the URL you want to shorten: '))
    print('Shortened url: ', short_url(url_long))


if __name__ == '__main__':
    main()
