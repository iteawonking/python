#Reading the example code
a = np.arange(6)
a2 = a[np.newaxis, :]
a2.shape
(1, 6)

#What is an array?
a = np.array([1, 2, 3, 4, 5, 6])
#or
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0])
[1 2 3 4]

#More information about arrays
[[0., 0., 0.],
 [1., 1., 1.]]

#How to create a basic array
import numpy as np
a = np.array([1, 2, 3])
np.zeros(2)
array([0., 0.])
np.ones(2)
array([1., 1.])
# Create an empty array with 2 elements
np.empty(2) 
array([3.14, 42.  ])  # may vary
np.arange(4)
array([0, 1, 2, 3])
np.arange(2, 9, 2)
array([2, 4, 6, 8])
np.linspace(0, 10, num=5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
x = np.ones(2, dtype=np.int64)
x
array([1, 1])

#Adding, removing, and sorting elements

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])

#How do you know the shape and size of an array?

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

array_example.ndim
3

array_example.size
24

array_example.shape
(3, 2, 4)

#Can you reshape an array?

a = np.arange(6)
print(a)
[0 1 2 3 4 5]
b = a.reshape(3, 2)
print(b)
[[0 1]
 [2 3]
 np.reshape(a, newshape=(1, 6), order='C')
array([[0, 1, 2, 3, 4, 5]])

 #How to convert a 1D array into a 2D array (how to add a new axis to an array)

 a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)
 a2 = a[np.newaxis, :]
a2.shape
(1, 6)
row_vector = a[np.newaxis, :]
row_vector.shape
(1, 6)
 col_vector = a[:, np.newaxis]
col_vector.shape
(6, 1)
 a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)
b = np.expand_dims(a, axis=1)
b.shape
(6, 1)
 c = np.expand_dims(a, axis=0)
c.shape
(1, 6)

#Indexing and slicing


data = np.array([1, 2, 3])

data[1]
2
data[0:2]
array([1, 2])
data[1:]
array([2, 3])
data[-2:]
array([2, 3])
 a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[a < 5])
[1 2 3 4]

 five_up = (a >= 5)
print(a[five_up])
[ 5  6  7  8  9 10 11 12]
 
 divisible_by_2 = a[a%2==0]
print(divisible_by_2)
[ 2  4  6  8 10 12]

 c = a[(a > 2) & (a < 11)]
print(c)
[ 3  4  5  6  7  8  9 10]

 five_up = (a > 5) | (a == 5)
print(five_up)
[[False False False False]
 [ True  True  True  True]
 [ True  True  True True]]

 a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)
(array([0, 0, 0, 0]), array([0, 1, 2, 3]))
list_of_coordinates= list(zip(b[0], b[1]))

for coord in list_of_coordinates:
    print(coord)
(0, 0)
(0, 1)
(0, 2)
(0, 3)

 print(a[b])
[1 2 3 4]

 not_there = np.nonzero(a == 42)
print(not_there)
(array([], dtype=int64), array([], dtype=int64))

 #How to create an array from existing data

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
 arr1 = a[3:8]
arr1
array([4, 5, 6, 7, 8])
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

 np.vstack((a1, a2))
array([[1, 1],
       [2, 2],
       [3, 3],
       [4, 4]])

 np.hstack((a1, a2))
array([[1, 1, 3, 3],
       [2, 2, 4, 4]])

 x = np.arange(1, 25).reshape(2, 12)
x
array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])

 np.hsplit(x, 3)
  [array([[ 1,  2,  3,  4],
         [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
         [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
         [21, 22, 23, 24]])]

 np.hsplit(x, (3, 4))
  [array([[ 1,  2,  3],
         [13, 14, 15]]), array([[ 4],
         [16]]), array([[ 5,  6,  7,  8,  9, 10, 11, 12],
         [17, 18, 19, 20, 21, 22, 23, 24]])]

 a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


b1 = a[0, :]
b1
array([1, 2, 3, 4])
b1[0] = 99
b1
array([99,  2,  3,  4])
a
array([[99,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])

 b2 = a.copy()


#Basic array operations

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data + ones
array([2, 3])

 data - ones
array([0, 1])
data * data
array([1, 4])
data / data
array([1., 1.])

 a = np.array([1, 2, 3, 4])

a.sum()
10

 b = np.array([[1, 1], [2, 2]])

 b.sum(axis=0)
array([3, 3])

 b.sum(axis=1)
array([2, 4])

 #Broadcasting

 
data = np.array([1.0, 2.0])
data * 1.6
array([1.6, 3.2])

 #More useful array operations

data.max()
2.0
data.min()
1.0
data.sum()
3.0

 a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

 a.sum()
4.8595784

 a.min()
0.05093587

 a.min(axis=0)
array([0.12697628, 0.05093587, 0.26590556, 0.5510652 ])

#Creating matrices


 data = np.array([[1, 2], [3, 4], [5, 6]])
data
array([[1, 2],
       [3, 4],
       [5, 6]])

 
data[0, 1]
2
data[1:3]
array([[3, 4],
       [5, 6]])
data[0:2, 0]
array([1, 3])
 
 data.max()
6
data.min()
1
data.sum()
21

 data = np.array([[1, 2], [5, 3], [4, 6]])
data
array([[1, 2],
       [5, 3],
       [4, 6]])
data.max(axis=0)
array([5, 6])
data.max(axis=1)
array([2, 5, 6])

 data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
data + ones
array([[2, 3],
       [4, 5]])

data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
data + ones_row
array([[2, 3],
       [4, 5],
       [6, 7]])

 np.ones((4, 3, 2))
array([[[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]]])

 np.ones(3)
array([1., 1., 1.])
np.zeros(3)
array([0., 0., 0.])
rng = np.random.default_rng()  # the simplest way to generate random numbers
rng.random(3) 
array([0.63696169, 0.26978671, 0.04097352])


np.ones((3, 2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
np.zeros((3, 2))
array([[0., 0.],
       [0., 0.],
       [0., 0.]])
rng.random((3, 2)) 
array([[0.01652764, 0.81327024],
       [0.91275558, 0.60663578],
       [0.72949656, 0.54362499]])  # may vary

 #Generating random numbers

rng.integers(5, size=(2, 4)) 
array([[2, 1, 1, 0],
       [0, 0, 0, 4]])  # may vary

 #How to get unique items and counts

 a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])

 unique_values = np.unique(a)
print(unique_values)
[11 12 13 14 15 16 17 18 19 20]

 unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)
[ 0  2  3  4  5  6  7 12 13 14]

 unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count)
[3 2 2 2 1 1 1 1 1 1]

 a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])

 unique_values = np.unique(a_2d)
print(unique_values)
[ 1  2  3  4  5  6  7  8  9 10 11 12]

 unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

 unique_rows, indices, occurrence_count = np.unique(
     a_2d, axis=0, return_counts=True, return_index=True)
print(unique_rows)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
print(indices)
[0 1 2]
print(occurrence_count)
[2 1 1]

 #Transposing and reshaping a matrix

data.reshape(2, 3)
array([[1, 2, 3],
       [4, 5, 6]])
data.reshape(3, 2)
array([[1, 2],
       [3, 4],
       [5, 6]])

arr = np.arange(6).reshape((2, 3))
arr
array([[0, 1, 2],
       [3, 4, 5]])

 arr.transpose()
array([[0, 3],
       [1, 4],
       [2, 5]])

 arr.T
array([[0, 3],
       [1, 4],
       [2, 5]])

 #How to reverse an array

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
 reversed_arr = np.flip(arr)

print('Reversed Array: ', reversed_arr)
Reversed Array:  [8 7 6 5 4 3 2 1]
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

reversed_arr = np.flip(arr_2d)
print(reversed_arr)
[[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]

 reversed_arr_rows = np.flip(arr_2d, axis=0)
print(reversed_arr_rows)
[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]

 reversed_arr_columns = np.flip(arr_2d, axis=1)
print(reversed_arr_columns)
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]

 arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)
[[ 1  2  3  4]
 [ 8  7  6  5]
 [ 9 10 11 12]]

 arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)
[[ 1 10  3  4]
 [ 8  7  6  5]
 [ 9  2 11 12]]


#Reshaping and flattening multidimensional arrays


x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
x.flatten()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])

 a1 = x.flatten()
a1[0] = 99
print(x)  # Original array
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
print(a1)  # New array
[99  2  3  4  5  6  7  8  9 10 11 12]

 a2 = x.ravel()
a2[0] = 98
print(x)  # Original array
[[98  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
print(a2)  # New array
[98  2  3  4  5  6  7  8  9 10 11 12]

 
 


 

