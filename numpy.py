# Processing time of numpy and normal call
import numpy as np
from time import process_time
list_1 = [i for i in range(2000)]
print('with out numpy')
start = process_time()
list_1 = [i+2 for i in list_1] 
end = process_time()
print(end - start)

print('With numpy(libarary)')
np_array = np.array([i for i in range(2000)])
start_np = process_time()
np_array = np_array+2
end_np = process_time()
print(end_np - start_np)
