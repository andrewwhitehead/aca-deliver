# aca-deliver

A sample service for pulling outbound messages from Redis and delivering them to the
requested endpoint.

To run the test redis server, execute `run.sh` in the `test-server` directory.

## Running the Python demo service

From the `python` directory:

```sh
pip install -r requirements.txt
python service.py $REDIS_HOST
```
