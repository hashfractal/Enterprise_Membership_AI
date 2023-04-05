from heap import *

A = [3, 8, 2, 4, 8, 1, 2, 0, 5, 9]
print ("A: ", A)
temp = Heap(A)
temp.buildHeap()
A = temp.heapToList()
print ("A:", A)


h1 = Heap([1, 11, 9, 2, 3])
h1.buildHeap()
h1.heapPrint()
h1.clear()
h1.heapPrint()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)
h1.heapPrint()