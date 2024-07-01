print("hello ")
print("changing")
import math
n=int(input('Enter the number of patten you want:\t'))
i=n
count=1
while count<=n:
    fun=math.log(count)
    fun=int(fun)
    print('*'*fun)
    count=count+1