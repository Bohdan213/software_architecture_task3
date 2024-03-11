from facade_service.services.utils import generate_uuid, perform_get_request, perform_post_request
import random


class PostService:

    logging_service_urls = ["http://127.0.0.1:8082/api/v1/logging_service",
                            "http://127.0.0.1:8083/api/v1/logging_service",
                            "http://127.0.0.1:8084/api/v1/logging_service"]

    @staticmethod
    def post_message(msg):
        uuid = generate_uuid()
        print(f"POST request, msg: {msg}, generated uuid: {uuid}")
        response_logging = perform_post_request(url=random.choice(PostService.logging_service_urls),
                                                data={"msg": msg, "uuid": uuid})
        print(f"RESPONSE from the post request to logging service, status: {response_logging.status_code}")
        return {"Status": "Success", "uuid": uuid, "msg": msg}, 201


class GetService:

    @staticmethod
    def get_messages():
        response_logging = perform_get_request(url=random.choice(PostService.logging_service_urls),
                                               params=None)
        print(f"RESPONSE from the get request to logging service, status: {response_logging.status_code}")

        response_messages = perform_get_request(url="http://127.0.0.1:8081/api/v1/messages_service",
                                                params=None)
        print(f"RESPONSE from the get request to messages service, status: {response_messages.status_code}")
        return {"Result": "Success", "msgs": response_logging.json()["msgs"] + response_messages.json()["msgs"]}, 200
