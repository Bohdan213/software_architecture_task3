from flask_restful import Resource, reqparse

from facade_service.services.facadeService import PostService, GetService


class FacadeService(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('msg', type=str, help='Message to be sent')

        self.get_parser = reqparse.RequestParser()


    def post(self):
        args = self.post_parser.parse_args()
        return PostService.post_message(args["msg"])


    def get(self):
        return GetService.get_messages()
