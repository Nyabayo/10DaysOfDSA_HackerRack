#Accessing and using Arrays
#What is an array: An array is a data structure that stores elements of the same type in a contiguous block of memory.
#In an array A of size N, each memory location has some unique index, i(where 0 is less than or equal to i which is less than N), that can be referenced as A[i] or
# Ai.
#Your task is to reverse an array of integers

#define the function
def reverse_array(arr):
    return arr[::-1]
#the array
arr = [2,5,8,1]
#calling the function
result = reverse_array(arr)
print(result)