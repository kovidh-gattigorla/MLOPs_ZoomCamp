# Processing time of numpy and normal call
from time import process_time
a = [1,2,3,4,5,6]
print('with out numpy')
start = process_time()
print(a)
end = process_time()
print(end - start)

import numpy as np
a = [1,2,3,4,5,6,]
print(a)
