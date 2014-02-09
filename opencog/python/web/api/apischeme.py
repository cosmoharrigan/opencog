__author__ = 'Cosmo Harrigan'

from flask import json, current_app
from flask.ext.restful import Resource, reqparse
from scheme_wrapper import *


class SchemeAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('callback', type=str, location='args')
        super(SchemeAPI, self).__init__()

    def post(self):
        """
        Evaluates a Scheme expression.
        Uri: scheme

        Include data with the POST request providing the Scheme expression to be evaluated

        Valid data elements:

        expression (required) Should contain a valid Scheme expression

        Example:

        {
          'expression': '(ConceptNode "Peter" (stv 0.001000 0.111111))'
        }

        :return success: Returns a response indicating whether the expression was successfully evaluated. Example:
        {
          'success': true
        }
        """

        # Prepare the atom data and validate it
        data = reqparse.request.get_json()

        if 'expression' not in data:
            abort(400, 'Invalid request: required parameter expression is missing')

        result = scheme_eval(data['command'])

        print "Evaluating Scheme expression:\n{0}".format(data['expression'])

        if len(result) > 0:
            print "Success"
            return current_app.response_class(json.dumps({'success': True}))
        else:
            return current_app.response_class(json.dumps({'success': False}))
