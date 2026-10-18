import os
import time
import redis

from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

REQ = Counter("app_requests_total", "Total requests", ["path", "status"])
LAT = Histogram("app_request_latency_seconds", "Latency", ["path"])

@app.route("/healthz")
def healthz():
    return {"status": "ok"}

@app.route("/api/products")
def products():
    start = time.time()
    r.incr("hits")
    LAT.labels("/api/products").observe(time.time() - start)
    REQ.labels("/api/products", "200").inc()
    return jsonify({"products": ["a", "b", "c"], "hits": r.get("hits")})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)