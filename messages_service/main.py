from messages_service import app_messages, api_messages, queue_reader
from messages_service.controllers.routes import MessagesService
import sys


api_messages.add_resource(MessagesService, '/api/v1/messages_service')


if __name__ == "__main__":
    msg_num = sys.argv[1]
    print("Here")
    queue_reader.init_queue(msg_num)
    app_messages.run(port=8080 + int(msg_num), debug=False)
