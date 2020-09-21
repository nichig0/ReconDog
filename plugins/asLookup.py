import sys
from requests import get


def asLookup(inp):
    result = get('http://api.hackertarget.com/aslookup/?q=' + inp).text
    sys.stdout.write(result)
