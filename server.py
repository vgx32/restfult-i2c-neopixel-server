from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class NeoPixelControl(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(NeoPixelControl, '/test')

@app.route("/")
def root():
    return "Hello from root"

if __name__ == '__main__':
    app.run(debug=True)
