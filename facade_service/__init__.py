from flask import Flask
from flask_restful import Api
from facade_service.services.queue_writer import QueueWriter


queue_writer_1 = QueueWriter(1)
queue_writer_2 = QueueWriter(2)

app_facade = Flask(__name__)
api_facade = Api(app_facade)
