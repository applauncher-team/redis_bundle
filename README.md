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

Using it
-----------------
Inject RedisManager

```python
import inject
from redis_bundle import RedisManager
redis_manager = inject.instance(RedisManager)

# Then use it as StrictRedis (its a wrapper) object (https://pypi.python.org/pypi/redis)
redis_manager.set('foo', 'bar')
redis_manager.get('foo')

```