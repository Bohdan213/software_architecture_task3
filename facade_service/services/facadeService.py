from facade_service.services.utils import generate_uuid, perform_get_request, perform_post_request
import random
from facade_service import queue_writer_1, queue_writer_2


class PostService:

    logging_service_urls = ["http://127.0.0.1:8083/api/v1/logging_service",
                            "http://127.0.0.1:8084/api/v1/logging_service",
                            "http://127.0.0.1:8085/api/v1/logging_service"]

    @staticmethod
    def post_message(msg):
        uuid = generate_uuid()
        print(f"POST request, msg: {msg}, generated uuid: {uuid}")
        response_logging = perform_post_request(url=random.choice(PostService.logging_service_urls),
                                                data={"msg": msg, "uuid": uuid})
        print(f"RESPONSE from the post request to logging service, status: {response_logging.status_code}")

        queue_writers = [queue_writer_1, queue_writer_2]
        random_queue_writer = random.choice(queue_writers)
        random_queue_writer.write(msg)
        print(f"Message {msg} written to the writer {random_queue_writer.num}")
        return {"Status": "Success", "uuid": uuid, "msg": msg}, 201


class GetService:

    @staticmethod
    def get_messages():

        response_logging = perform_get_request(url=random.choice(PostService.logging_service_urls),
                                               params=None)
        print(f"RESPONSE from the get request to logging service, status: {response_logging.status_code}")

        messages_messages = ""
        for i in range(1, 3):
            response_messages = perform_get_request(url=f"http://127.0.0.1:{8080 + i}/api/v1/messages_service", params=None)
            messages_messages += response_messages.json()["msgs"]
            print(f"RESPONSE from the get request to messages service {i}, status: {response_messages.status_code}")
        return {"Result": "Success", "msgs": response_logging.json()["msgs"] + messages_messages}, 200
