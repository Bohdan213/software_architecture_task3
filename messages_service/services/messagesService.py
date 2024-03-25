from messages_service import memory


class GetService:

    @staticmethod
    def get_messages():
        print("GET request")
        return {"msgs": ", ".join(memory)}, 200