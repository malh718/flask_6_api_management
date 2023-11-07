from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f' "Hello from MALIHAS Flask API Endpoint Server" '

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    return f'Hello {name}!'

@app.route('/hello', methods=['POST'])
def hello_post():
    """
    This endpoint returns a greeting message based on the name provided in the JSON body.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          required:
            - name
          properties:
            name:
              type: string
              default: World
    responses:
      200:
        description: A greeting message
      400:
        description: Invalid JSON
    """
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)


## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooper