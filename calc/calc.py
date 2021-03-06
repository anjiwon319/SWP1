import os, sys
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))
from cgi import parse_qs
from TEMPLATE import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a',[''])[0]
    b = d.get('b',[''])[0]
    add, mul = 0, 0
    try:    
        a, b = int(a), int(b)
        add = a + b
        mul = a * b
    except ValueError:
        if '' in [a, b]:
            add = "You didn't input value"
            mul = "You didn't input value"
        else:
            add = "Please input number not string"
            mul = "Please input number not string"
    response_body = html % {'add':add, 'mul':mul}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

