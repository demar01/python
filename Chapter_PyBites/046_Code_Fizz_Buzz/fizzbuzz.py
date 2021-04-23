def fizzbuzz(i):
    for n in range(1, i+1):
        if n%3==0 & n%5==0:
            print("FizzBuzz")
        elif n%3==0:
            print("Fizz")
        elif n%5==0:
            print("Buzz")
        else:
            print(n)  

# def fizzbuzz(num):
#     arr = []
#     if num % 3 == 0:
#         arr.append('Fizz')
#     if num % 5 == 0:
#         arr.append('Buzz')
#     return ' '.join(arr) if arr else num