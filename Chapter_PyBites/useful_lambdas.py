#adding
r = lambda a : a + 15
print(r(10))

#multiplying
def func_compute(n):
     return lambda x : x * n
result = func_compute(2)
print(result(15)) #double the number
result = func_compute(3)
print(result(15)) #triple the number

#sorting tuples
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key = lambda x: x[1])
print(subject_marks)

#sorting dict
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sorted_models = sorted(models, key = lambda x: x['color'])
print(sorted_models)

#filtering
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

#square every number (with map)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

#check if startswith
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))

#with reduce to do an operation with all the elements of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
sum = reduce((lambda x, y: x - y), li)
print (sum)

#finding intersections
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
result = list(filter(lambda x: x in array_nums1, array_nums2)) 
print ("\nIntersection of the said arrays: ",result)

#count even and odds
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)


#remove words
words=['orange', 'red', 'green', 'blue', 'white', 'black']
toremove=['orange', 'black']
filtered_words = list(filter(lambda x: x not in toremove , words))
print("Words after filtering: ", filtered_words)

#remove none
words= [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
filtered_words = list(filter(lambda x: x !=None , words))
print("Words after filtering: ", filtered_words)

mylist=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

map(lambda element: element, list(nums).count(element)), nums)

     
