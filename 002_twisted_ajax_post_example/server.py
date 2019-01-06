from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
import cgi

class PostHandler(Resource):

    def render_POST(self, request):
        content = request.content.read().decode("utf-8")
        escapedContent = cgi.escape(content)
        print(escapedContent)
        return b"12345"

root = File('www')
root.putChild(b"post_test", PostHandler())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(factory)
reactor.run()