"""
Examples of how to consume the REST API from Python, using the 'requests' module:
http://www.python-requests.org/

From the wiki documentation located here:
http://wiki.opencog.org/w/REST_API

Prerequisisites:
  sudo easy_install requests
"""

__author__ = 'Cosmo Harrigan'

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

data = {'command': """(ConceptNode "Peter" (av 0 0 0) (stv 0.001000 0.111111))

(ConceptNode "Frog" (av 0 0 0) (stv 0.010000 0.111111))

(ConceptNode "Intelligent" (av 0 0 0) (stv 0.050000 0.111111))

(ConceptNode "Slimy" (av 0 0 0) (stv 0.010000 0.111111))

(ConceptNode "Animal" (av 0 0 0) (stv 0.100000 0.111111))

(ConceptNode "Being" (av 0 0 0) (stv 0.100000 0.111111))

(InheritanceLink (av 0 0 0) (stv 0.900000 0.111111)
  (ConceptNode "Animal" (av 0 0 0) (stv 0.100000 0.111111))
  (PredicateNode "Moves" (av 0 0 0) (stv 0.100000 0.111111)))
"""}

post_response = post(uri + 'scheme', data=json.dumps(data), headers=headers)

print post_response.content