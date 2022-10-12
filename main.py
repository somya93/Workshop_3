from flask import Flask  # Import the Flask class. An instance of this class will be our WSGI (Web Server Gateway
# Interface) application. - This is what talks to the web application.
from flask_restful import Api, Resource, reqparse  # flask_restful is an extension for Flask that adds support for
# quickly building REST APIs. It encourages best practices with minimal setup.

app = Flask(__name__)  # Create an instance of this class.
api = Api(app)  # main entry point of the application. You need to initialize it with a Flask Application object (app)

rider_data = {'R0': 'Karim', 'R1': 'Somya', 'R2': 'Manuja'}  # Contains ID:Name of riders.


# Resource supporting GET method with no parameters.
class SampleResource(Resource):
    def get(self):
        sample_response = "SampleResource got GET request."
        return sample_response


# Concrete example of RiderResource supporting GET method with rider ID query parameter.
class RiderResource(Resource):
    def get(self):
        get_parser = reqparse.RequestParser()  # From flask library.
        get_parser.add_argument('id',
                                type=str)  # Expect a query param called "id". Replicate this line for each query param.
        args = get_parser.parse_args()  # Stores value of "id" (and any other query params), defaults to None.
        if args.id in rider_data:  # Check if "id" exists.
            sample_response = "Rider with ID %s is %s" % (args.id, rider_data[args.id])
        else:  # Provided "id" doesn't exist, return a useful message.
            sample_response = "Rider ID %s doesn't exist, legal values are: %s" \
                              % (args.id, list(rider_data.keys()))
        return sample_response


# http://localhost:5000/sample_route
api.add_resource(SampleResource, '/sample_route')  # add_resource method maps a url/route to a resource.

# http://localhost:5000/rider
# http://localhost:5000/rider?id=R5
api.add_resource(RiderResource, '/rider')

if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default.
