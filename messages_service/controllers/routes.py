from flask_restful import Resource, reqparse
from messages_service.services.messagesService import GetService


class MessagesService(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        pass

    def get(self):
        return GetService.get_messages()