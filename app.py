from flask import Flask
from flask_restful import Api
from controllers import helloController

app = Flask(__name__)

api = Api(app)


api.add_resource(helloController.HelloController, '/api/hello')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
