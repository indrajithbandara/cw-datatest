#!/usr/bin/python 
import sys 

def merge(array, q, p, r): 
left_array = array[q:p+1] 
right_array = array[p+1:r+1] 

left_array_num = len(left_array) 
right_array_num = len(right_array) 

i, j , k= [0, 0, q] 
while i < left_array_num and j < right_array_num: 
if (left_array[i] < right_array[j]): 
array[k] = left_array[i] 
i+=1 
else: 
array[k] = right_array[j] 
j+=1 
k+=1 

while i < left_array_num: 
array[k] = left_array[i]; 
k+=1 
i+=1 

while j < right_array_num: 
array[k] = right_array[j] 
k+=1 
j+=1 

def merge_sort(array, q, r): 
if q < r: 
p = (q + r) / 2 
merge_sort(array, q, p) 
merge_sort(array, p + 1, r) 
merge(array, q, p, r) 

if __name__ == "__main__": 
array = [2, 45, 5, 7, 34, 456, 345, 89, 8, 1, 341, 4, 98, 67] 
merge_sort(array, 0, len(array) - 1) 

for a in array: 
sys.stdout.write("%d " % a) 