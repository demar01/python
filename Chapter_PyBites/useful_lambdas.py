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