import numpy as np

list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a.shape)

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b.shape)

a = np.zeros((2, 2))
print(a)
a = np.ones((2, 3))
print(a)
a = np.full((2, 3), 5)
print(a)
a = np.eye(3)
print(a)
a = np.array(range(20)).reshape((4, 5))
print(a)
array1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
array1_re = np.array(array1)
a = np.array(range(10, 19)).reshape(array1_re.shape)
print(a)

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)

#슬라이싱
a = arr[0:2, 0:2]
print(a)
a = arr[1:, 1:]
print(a)

lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
s = a[[0, 1], [1, 3]]
print(s)

# s = a[[n1, n2], [n3, n4]]를 입력하면
# a[n1, n2], a[n3, n4]가 들어가는 것이 아니라
# a[n1, n3], a[n2, n4]가 들어간다.


#boolean 인덱싱
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)

bool_indexing_array = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
])

n = a[bool_indexing_array]
print(n)

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)

bool_indexing = (a % 2 == 0)

print(bool_indexing)
print(a[bool_indexing])
n = a[ a % 2 == 0]
print(n)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.add(a, b)
print(c)
c = a + b
print(c)

c = np.subtract(a, b)
print(c)
c = a - b
print(c)

c = a * b
print(c)
c = np.multiply(a, b)
print(c)

c = a / b
print(c)
c = np.divide(a, b)
print(c)