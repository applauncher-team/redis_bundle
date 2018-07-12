# Redis bundle for AppLauncher
Redis support for applauncher

Installation
-----------
```bash
pip install redis_bundle 
```
Then add to your main.py
```python
import redis_bundle

bundle_list = [
    redis_bundle.RedisBundle(),
]
```

Configuration
-------------
```yml
redis:
  hostname: 'localhost'
  database: 0
```
You can use all parameters supported by redis.Redis

Using it
-----------------
Inject Redis

```python
import inject
from redis import Redis
redis = inject.instance(Redis)

redis.set('foo', 'bar')
redis.get('foo')

```
