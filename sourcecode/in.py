
# allowed characters
# `abcdefghipqrstuvwxy
import numpy as np

data = '`abcdefghipqrstuvwxy'
#ashex = hex(data)
#print(hex(data))
for i in range(0, len(data), 2):
    v = data[i]
    print(v)
    uint8 = hex(np.frombuffer(str.encode(v), dtype=np.uint8)[0])
    print(uint8)
    