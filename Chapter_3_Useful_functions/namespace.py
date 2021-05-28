a_num = 10
b_num = 11
 
def outer_func():
    global a_num
    a_num = 15
    b_num = 16
    def inner_func():
        global a_num
        a_num = 20
        b_num = 21
        print('a_num inside inner_func :', a_num)
        print('b_num inside inner_func :', b_num)
    inner_func()
    print('a_num inside outer_func :', a_num)
    print('b_num inside outer_func :', b_num)
     
outer_func()
print('a_num outside all functions :', a_num)
print('b_num outside all functions :', b_num)
 
# a_num inside inner_func : 20
# b_num inside inner_func : 21
 
# a_num inside outer_func : 20
# b_num inside outer_func : 16
 
# a_num outside all functions : 20
# b_num outside all functions : 11