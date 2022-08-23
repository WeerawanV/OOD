'''เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล'''

import math
r = input('r=')
a = math.pi*float(r)*float(r)
print('Area=',a,sep='')
