from hazelcast import HazelcastClient


ip = '192.168.1.67'


class QueueWriter:
    def __init__(self, num):
        self.client = HazelcastClient(
            cluster_name="hazelcast-cluster",
            cluster_members=[f'{ip}:5701', f'{ip}:5702', f'{ip}:5703']
        )
        self.num = num
        self.queue = self.client.get_queue(f"msg-{num}").blocking()

    def write(self, message):
        self.queue.put(message)
