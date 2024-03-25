from flask import Flask
from flask_restful import Api
from hazelcast import HazelcastClient


ip = '192.168.1.67'


client = HazelcastClient(
    cluster_name="hazelcast-cluster",
    cluster_members=[f"{ip}:5701",
                     f"{ip}:5702",
                     f"{ip}:5703"]
    ,
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)

hash_map = client.get_map("hash_map").blocking()

app_logging = Flask(__name__)
api_logging = Api(app_logging)
