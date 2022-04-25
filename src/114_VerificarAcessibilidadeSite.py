import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessivel no momento :(\033[m')
else:
    print('\033[32mTudo ok, site Pudim está acessível!\033[m')
