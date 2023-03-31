import numpy
import random

datalen = 2160

arr = list(range(0, 2159))
random.shuffle(arr)

split1 = int(datalen*0.7)
split2 = int(datalen*0.8)
split3 = int(datalen*0.6)
split4 = int(datalen*0.5)
split5 = int(datalen*0.4)
split6 = int(datalen*0.3)
split7 = int(datalen*0.2)
split8 = int(datalen*0.1)



arr20 = arr[split6:]
arr21 = arr[: split7]
arr22 = arr[split7: split6]

arr13 = arr[:split8]
arr14 = arr[split5:]
arr15 = arr13 + arr14
arr16 = arr[split7: split5]
arr17 = arr[split8: split7]

arr8 = arr[:split6]
arr9 = arr[split3:]
arr10 = arr8 + arr9
arr11 = arr[split5: split3]
arr12 = arr[split6: split5]

arr0 = arr[:split1]
arr1 = arr[split1: split2]
arr2 = arr[split2:]

arr3 = arr[:split4]
arr4 = arr[split2:]
arr5 = arr3 + arr4
arr6 = arr[split3: split2]
arr7 = arr[split4: split3]
train_idx1 =  numpy.array(arr0)
val_idx1   =  numpy.array(arr1)
test_idx1  =  numpy.array(arr2)

train_idx2 =  numpy.array(arr5)
val_idx2   =  numpy.array(arr7)
test_idx2  =  numpy.array(arr6)

train_idx3 =  numpy.array(arr10)
val_idx3   =  numpy.array(arr12)
test_idx3  =  numpy.array(arr11)

train_idx4 =  numpy.array(arr15)
val_idx4   =  numpy.array(arr17)
test_idx4  =  numpy.array(arr16)

train_idx5 =  numpy.array(arr20)
val_idx5   =  numpy.array(arr22)
test_idx5  =  numpy.array(arr21)

numpy.savez('example1.npz', train_idx=train_idx1, val_idx=val_idx1, test_idx=test_idx1)
numpy.savez('example2.npz', train_idx=train_idx2, val_idx=val_idx2, test_idx=test_idx2)
numpy.savez('example3.npz', train_idx=train_idx3, val_idx=val_idx3, test_idx=test_idx3)
numpy.savez('example4.npz', train_idx=train_idx4, val_idx=val_idx4, test_idx=test_idx4)
numpy.savez('example5.npz', train_idx=train_idx5, val_idx=val_idx5, test_idx=test_idx5)


