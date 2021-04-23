from collections import deque


# def my_queue(n=5):
#     dq = deque(['Geeks','for','Geeks', 'is', 'good','out']) 
#     return(collections.deque(itertools.islice(dq,0,n)))


def my_queue(n=5):
    q = deque(maxlen=n)
    return q


if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))