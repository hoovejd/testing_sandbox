from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.resource import Resource
import json

class GetJSON(Resource):
    def render_GET(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        data = {}
        data['apple'] = 'green'
        data['banana'] = 'yellow'
        data['cherry'] = 'red'
        request.write(json.dumps(data))

root = Resource()
root.putChild(b"get_json", GetJSON())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8890)
endpoint.listen(factory)
reactor.run()