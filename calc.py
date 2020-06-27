from cgi import parse_qs
from TEMPLATE import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a',[''])[0]
    b = d.get('b',[''])[0]
    add, mul = 0, 0
    if '' not in [a, b]:
        a, b = int(a), int(b)
        add = a + b
        mul = a * b
    response_body = html % {'add':add, 'mul':mul}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

