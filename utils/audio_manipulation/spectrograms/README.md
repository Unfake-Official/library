Replace:
```
import os
...
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "intervals.msgpack"), "rb") as _fdesc:
```
With:
```
import os
...
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "intervals.msgpack"), "rb") as _fdesc:
```
In Librosa's ```intervals.py``` file