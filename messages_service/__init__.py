from flask import Flask
from flask_restful import Api
from messages_service.services.queue_reader import QueueReader


memory = []

queue_reader = QueueReader(memory)

app_messages = Flask(__name__)
api_messages = Api(app_messages)
