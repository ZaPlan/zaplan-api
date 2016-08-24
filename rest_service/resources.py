import json
import random

from flask import Flask
from flask_restful import Resource, Api, reqparse

from rest_service import app, api
from src import create_timeline

parser = reqparse.RequestParser()

parser.add_argument('latitude')
parser.add_argument('longitude')
parser.add_argument('budget')
parser.add_argument('radius')
parser.add_argument('start_time')
parser.add_argument('end_time')

class Root(Resource):
    def get(self):
        return {"Welcome"  : "This is the Zaplan API", "Sample Query:" : "localhost/timeline?latitude=12.844413099999999&longitude=80.1524191&budget=1500&radius=100000&start_time=9&end_time=22"}

class Timeline(Resource):
    def get(self):
        args = parser.parse_args()
        timeline = create_timeline.lets_do_this(args['latitude'], args['longitude'], args['budget'], args['radius'], args['start_time'], args['end_time'])
        print timeline
        return {"timeline" : timeline }

api.add_resource(Root, '/')
api.add_resource(Timeline, '/timeline')