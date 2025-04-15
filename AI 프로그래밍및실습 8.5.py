#8.5

import math

for degree in range(0, 181, 10):
    rad = math.radians(degree)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)
    
    print(f"sin({degree:3}) = {sin_val:7.3f}, cos({degree:3}) = {cos_val:7.3f}, tan({degree:3}) = {tan_val:7.3f}")
