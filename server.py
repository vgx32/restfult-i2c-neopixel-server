from flask import Flask
from flask_restful import Resource, Api, reqparse
import pdb

app = Flask(__name__)
api = Api(app)

class NeoPixelControl(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('mode', type=str, location='json')
        self.parser.add_argument('data', type=list, location='json')
        super(NeoPixelControl, self).__init__()

    def get(self):
        return {'hello': 'world'}

    def put(self):
        args = self.parser.parse_args()
        print("received a put of %s" % args)
        #TODO: convert to binary buffer and send to arduino
        return 201


api.add_resource(NeoPixelControl, '/pixels/')

@app.route("/")
def root():
    return "Hello from root"

if __name__ == '__main__':
    app.run(debug=True)
