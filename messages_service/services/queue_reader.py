from hazelcast import HazelcastClient
# from messages_service import memory


ip = '192.168.1.67'


class QueueReader:
    def __init__(self, memory):
        self.client = HazelcastClient(
            cluster_name="hazelcast-cluster",
            cluster_members=[f'{ip}:5701', f'{ip}:5702', f'{ip}:5703']
        )
        self.memory = memory

    def init_queue(self, num):
        queue = self.client.get_queue(f"msg-{num}").blocking()
        queue.add_listener(include_value=True, item_added_func=self.on_item_added)

    def on_item_added(self, event):
        print(f"Readed {event.item} from queue")
        self.memory.append(event.item)
