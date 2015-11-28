## System Redis

For more advanced usecases & for performance Jumpscale depends on redis.

### for what functions is it used

- logs & log rotation)
- errorconditions
- statistics & aggregation of statistics
- for workers (local execution of work in async way in queues)
- for caching of config params
- for remembering state of e.g. executors
- ...

### how does it get loaded
- When starting redis client will be loaded on j.core.redis
- first port 9999 will be checked, if available that client will be loaded
- then default redis port 6379 will be checked and loaded if found
- otherwise j.core.redis=None

### how to get a redis

on ubuntu
```
apt-get install redis-server -y
```


