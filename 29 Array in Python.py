from array import *

# vals = array('i',[5,9,-8,4,2])
#
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
#
# for i in range(5):
# for i in range(len(vals)):
# for e in vals:
#     print(e)


# vals = array('u',['a','e','i'])
#
#
# for e in vals:
#     print(e)


# vals = array('i',[5,9,8,4,2])
# newArr = array(vals.typecode, (a*a for a in vals))
#
# for e in newArr:
#     print(e)


vals = array('i', [5, 9, 8, 4, 2])
newArr = array(vals.typecode, (a*a for a in vals))

i = 0

while i < len(newArr):
    print(newArr[i])
    i += 1
