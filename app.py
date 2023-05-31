import time 
from flask import Flask
import redis

app = Flask(__name__)
chche = redis.Redis(host='redis',port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return chche.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1 
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'hello you have been seen {} times.\n'.format(count)
