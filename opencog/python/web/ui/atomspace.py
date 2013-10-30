from requests import *
import json

# Define the API Endpoint - replace 127.0.0.1 with the server IP address if necessary
IP_ADDRESS = '127.0.0.1'
PORT = '5000'
uri = 'http://' + IP_ADDRESS + ':' + PORT + '/api/v1.0/'
headers = {'content-type': 'application/json'}

# Pretty print function for displaying JSON request/response information
def pprint(call, contents):
    print '\n' + call.request.method + ' ' + call.request.path_url + ':'
    print json.dumps(contents, indent=2)

get_response = get(uri + 'atoms', params={'type': 'ConceptNode'})
atoms = get_response.json()['result']['atoms']
#pprint(get_response, atoms)

for atom in atoms:
    print atom['name']