

def recursion():
    # 用list 計數
    # count_lst = [0]
    # num = b(5, 2, count_lst)
    num = b(5, 2)
    print(num)
    # print(count_lst)


def b(n, k):
    if k == 0 or k == n:
        print('Base Case!')
        # 夾在同一個位置
        # count_lst[0] += 1
        return 2
    else:
        # return b(n-1, k-1,count_lst) + b(n-1, k,count_lst)
        return  b(n-1, k-1) + b(n-1, k)




if __name__ == '__main__':
    recursion()