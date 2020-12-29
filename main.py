from rq import Queue, Worker
from redis import Redis
from util import saveInFile
from datetime import timedelta
redisConn = Redis()
queue = Queue(connection=redisConn)


for i in range(10):
    job = queue.enqueue(saveInFile, f"process-{i}\n")
    print(job.get_status())
