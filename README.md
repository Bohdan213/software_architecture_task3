Hazelcast cluster with 3 nodes were initialised for both hash_map and messaging_queue.

![img.png](imgs/img.png)

Run 7 POST requests to the facade service:

Messages services:
![img_1.png](imgs/img_1.png)

![img.png](imgs/img2.png)

Logging services:

![img_2.png](imgs/img_2.png)

![img_3.png](imgs/img_3.png)

Facade service:

![img_4.png](imgs/img_4.png)

Run GET request to the facade service:

Result:
```json
{
  "Result": "Success",
  "msgs": "Hello, World2Hello, World5Hello, World7Hello, World3Hello, World4Hello, World7Hello, World6Hello, World1Hello, World1, Hello, World2, Hello, World3, Hello, World6, Hello, World7Hello, World4, Hello, World5"
}
```

Facade service logs:
![img_5.png](imgs/img_5.png)
