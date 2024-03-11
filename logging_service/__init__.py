from flask import Flask
from flask_restful import Api
from hazelcast import HazelcastClient


client = HazelcastClient(
    cluster_name="hazelcast-cluster",
    cluster_members=["192.168.1.67:5701",
                     "192.168.1.67:5702",
                     "192.168.1.67:5703"]
    ,
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)

hash_map = client.get_map("hash_map").blocking()

app_logging = Flask(__name__)
api_logging = Api(app_logging)
