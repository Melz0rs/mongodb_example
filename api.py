from flask import Flask, request
import jobs
from rq import Queue
from redis import Redis

app = Flask(__name__)
redis_conn = Redis(host='redis', port=6379)
q = Queue(connection=redis_conn)


@app.route('/add', methods=['POST'])
def add_something(obj):
    app.logger.info(f"adding obj: {request.json}")

    job = q.enqueue(jobs.add_to_db, args=[request.json, 'test_collection'])

    while job.result is None:
        pass

    app.logger.info(f"job result: {job.result}")

    return job.result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

