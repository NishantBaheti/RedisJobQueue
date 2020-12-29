# RedisJobQueue

## Setup Redis Docker container

- pull redis image

        docker pull redis

- start container with port 6379(default of redis and bridging with host machine)

        docker run -p 6379:6379 --name my-redis-container -d redis

## Start redis queue worker

- start rq worker

        rq worker --with-scheduler
