# aca-deliver

A sample service for pulling outbound messages from Redis and delivering them to the
requested endpoint.

## Running a test Redis server

To start the test Redis server, execute `run.sh` in the `test-server` directory.

## Running the Python demo service

From the `python` directory:

```sh
pip install -r requirements.txt
python service.py $REDIS_HOST
```

## Sending sample messages

Sample messages can be added to the queue using:

```sh
python send.py $REDIS_HOST $ENDPOINT $MESSAGE
```
