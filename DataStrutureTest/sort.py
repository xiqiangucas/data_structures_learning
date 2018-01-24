#coding=utf-8

#交换函数
def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp

#选择排序
def selectionSort(lyst):
    i=0
    while i<len(lyst)-1:
        minIdex=i
        j=i+1
        while j < len(lyst):            #找到最小项的位置
            if lyst[j]<lyst[minIdex]:
                minIdex=j
            j += 1
        if minIdex != i:                #交换最小项的位置
            swap(lyst,minIdex,i)
        i += 1                          #移动位置

#冒泡排序
def bubbleSort(lyst):

    swapped=False
    n = len(lyst)
    while n > 1:
        j=1
        while j<len(lyst):
            if lyst[j-1]>lyst[j]:
                swap(lyst,j-1,j)
                swapped=True
            if not swapped:
                return
            j += 1
        n -= 1

#插入排序
def insertionSort(lyst):
    i = 1
    while i <len(lyst):
        itemToInsert = lyst[i]
        j = i-1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j+1]=lyst[j]
                j -= 1
            else:
                break
        lyst[j+1]=itemToInsert
        i += 1

#快速排序
class quicksort():

    def __init__(self,lyst):

        self.quicksortHelper(lyst,0,len(lyst)-1)

    #递归调用此过程
    def quicksortHelper(self,lyst,left,right):

        if left<right:
            pivotlocation = self.partition(lyst,left,right)
            self.quicksortHelper(lyst,left,pivotlocation-1)
            self.quicksortHelper(lyst,pivotlocation+1,right)

    #left:子列表最左索引
    #right：子列表最优索引
    def partition(self,lyst,left,right):

        middle=(left + right)//2
        pivot = lyst[middle]    #选定基准点

        lyst[middle] = lyst[right]  #基准点与最后一项进行交换
        lyst[right] = pivot

        boundary = left #设置边界
        #从第一项开始扫描整个列表
        for index in range(left,right):
            if lyst[index] < pivot:         #每当遇到小于基准点的项
                swap(lyst,boundary,index)   #将该项与boundary位置的项进行交换
                boundary += 1               #并将边界后移
        swap(lyst,boundary,right)           #最后将基准点与boundary位置的项进行交换

        return boundary                     #返回当前分割点

# from arrays import Array
#合并排序
class mergesort():

    def __init__(self,lyst):
        copyBuffer=[0]*len(lyst)
        self.mergeSortHelper(lyst,copyBuffer,0,len(lyst)-1)

    def mergeSortHelper(self,lyst,copyBuffer,low,high):
        pass
        """
        lyst        list being sorted
        copyBuffer  temp space needed during merge
        low,high    bounds of sublist
        middle      midpoint of sublist
       """
        if low < high :
            middle = (low + high)//2
            self.mergeSortHelper(lyst,copyBuffer,low,middle)
            self.mergeSortHelper(lyst,copyBuffer,middle+1,high)
            self.merge(lyst,copyBuffer,low,middle,high)

    def merge(self,lyst,copyBuffer,low,middle,high):
        pass
        """
        lyst        list that is being sorted
        copyBuffer  temp space needed during the merge process
        low         begining of first sorted sublist
        middle      end of first sorted sublist
        middle+1    begining of second sorted sublist
        high        end of second sorted sublist
       """
        #initialize i1 and i2 to the first items in each sublist
        i1=low
        i2=middle+1

        #interleave items from the sublists into the copyBuffer in such a way that order is maintained
        for i in range(low,high+1):
            if i1 >middle:
                copyBuffer[i]=lyst[i2]      #first sublist exhausted
                i2 += 1
            elif i2>high:
                copyBuffer[i]=lyst[i1]
                i1 += 1
            elif lyst[i1]<lyst[i2]:
                copyBuffer[i]=lyst[i1]
                i1 += 1
            else:
                copyBuffer[i]=lyst[i2]
                i2 += 1

        for i in range(low,high+1):
            lyst[i]=copyBuffer[i]




if __name__=="__main__":
    lst=[2,4,1,5,3,5,7,1,9,0]
    # selectionSort(lst)
    print(lst)
    # bubbleSort(lyst=lst)
    # insertionSort(lst)
    # print(lst)
    # qs=quicksort(lyst=lst)
    ms=mergesort(lyst=lst)
    print(lst)