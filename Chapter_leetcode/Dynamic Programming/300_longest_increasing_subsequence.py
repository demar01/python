def lis(arr):
    # [1,3,5,4,7]
    #  1,2,3,3,4  LS
    #  1,1,1,1,2 count
    # maximum Sum (2)

    n = len(arr)
 
    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1: #this will check that each number is not less than the previous one  and that we have not seen the number before
                lis[i] = lis[j]+1
 
    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])
 
    return maximum
# end of lis function
 

#[["i "+str(nums[i]),"j "+str(nums[i])] for i in range (N) for j in range(i)]


# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print "Length of lis is", lis(arr)

lis([10,9,2,5,3,7,101,18])


# https://www.youtube.com/watch?v=td8JCnqt-JI
