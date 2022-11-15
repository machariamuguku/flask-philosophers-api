from flask import Flask, request
from responses import originalResponse,  modifiedDateColumnResponse, invalidDateColumnResponse


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/philosophers", methods=['GET'])
def get_philosophers():
    response = originalResponse
    modified_since = request.headers.get('Modified-Since')
    if (modified_since):
        response = [
            resp for resp in originalResponse if resp['date_modified'] >= modified_since]
    sortedResponse = sorted(response,
                            key=lambda i: i['date_modified'])
    return sortedResponse
