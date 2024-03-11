from flask_restful import Resource, reqparse
from logging_service.services.loggingService import PostService, GetService


class LoggingService(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('msg', type=str, help='Message to be logged')
        self.post_parser.add_argument('uuid', type=str, help='uuid of the message')

        self.get_parser = reqparse.RequestParser()

    def post(self):
        args = self.post_parser.parse_args()

        return PostService.post_message(args['msg'], args['uuid'])

    def get(self):
        return GetService.get_messages()
