def selectionSort2(A):
    for last in range(len(A) - 1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

def theLargest(A: list, last: int) -> int:
    largest = 0
    for i in range(last + 1):
        if A[i] > A[largest]:
            largest = i
    return largest

if __name__ == "__main__":
    A = [3, 4, 1, 2, 6, 5]
    selectionSort2(A)
    print(A)