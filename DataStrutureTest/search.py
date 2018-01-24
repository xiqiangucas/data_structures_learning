#coding=utf-8

#搜索最小值
def indexOfMin(lyst):
    minIndex=0
    currentIndex=1
    while currentIndex<len(lyst):
        if lyst[currentIndex]<lyst[minIndex]:
            minIndex=currentIndex
        currentIndex += 1
    return minIndex

if __name__=='__main__':
    pass
    lst=[9,1,5,3,8,6,4,2]
    minindex=indexOfMin(lst)
    print(minindex)

#顺序搜索
def sequentialSearch(target,lyst):
    position=0
    while position < len(lyst):
        if target == lyst[position]:
            return 1
        position += 1
    return -1

if __name__=='__main__':
    pass
    lst=[9,1,5,3,8,6,4,2]
    flag=sequentialSearch(target=8,lyst=lst)
    print(flag)

#二分查找
def binarySearch(target,sortedLyst):
    left=0
    right=len(sortedLyst)-1
    while left<right:
        mid=(left+right)//2
        if target == sortedLyst[mid]:
            return mid
        elif target<sortedLyst[mid]:
            right=mid - 1
        else:
            left=mid + 1
    return -1

if __name__=='__main__':
    pass
    lst=[1,2,3,4,5,6,7,8,9]
    flag=binarySearch(target=0,sortedLyst=lst)
    print(flag)
