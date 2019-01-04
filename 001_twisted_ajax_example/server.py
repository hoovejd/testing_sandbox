from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
import json

json_data = {}
json_data['apple'] = 'green'
json_data['banana'] = 'yellow'
json_data['cherry'] = 'red'

class JsonHandler(Resource):

    def render_GET(self, request):
        return json.dumps(json_data)

root = File('www')
root.putChild(b"get_json", JsonHandler())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(factory)
reactor.run()