import os
import socket
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis-service"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/")
def index():
    count = r.incr("visitor_count")
    return f"Visitor Count: {count} | Pod: {socket.gethostname()}\n"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)