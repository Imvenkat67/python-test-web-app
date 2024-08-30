from flask import Flask, jsonify, request
import logging
import os
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

#JSON log formatting
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "remote_addr": "%(remote_addr)s", "method": "%(remote_addr)s", "method": "%(method)s", "scheme": "%(scheme)s", "full_path": "%(full_path)s"}')
handler.setFormatter(formatter)
logger.addHandler(handler)

#Expose metric
http_requests_total = Counter('http_requests_total', 'Total HTTP Requests')

#Custom message
MESSAGE = os.getenv('MESSAGE', 'Hello user!')

@app.before_request
def log_request_info():
    logger.info('', extra={
        'remote_addr': request.remote_addr,
        'method': request.method,
        'scheme': request.scheme,
        'full_path': request.full_path
    })

#define welcome page
@app.route('/', methods=['GET'])
def welcome():
    http_requests_total.inc()
    return "Welcome to the test app"

#define custom message
@app.route('/message', methods=['GET'])
def get_message():
    http_requests_total.inc()
    return jsonify({"message": MESSAGE})

#expose metrics on a endpoint for prometheus
@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)