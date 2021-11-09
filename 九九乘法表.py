for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end='')
    print()


# \t是空格
# end=''是取消输出的回车不自动换行
# range 是一个函数创建一个整数列表