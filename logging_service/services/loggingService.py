from logging_service import hash_map

class PostService:

    @staticmethod
    def post_message(msg, uuid):
        hash_map.put(uuid, msg)
        print(f"POST request: msg={msg}, uuid={uuid}")
        return {"Result": "Message logged successfully."}, 201


class GetService:

    @staticmethod
    def get_messages():
        # result = hash_map.values()
        result = list(hash_map.values())
        result = "".join(result)
        print("GET request")
        return {"msgs": result}, 200
