import sys

def wiggleSort(arrnums):
    for i,k in enumerate(arrnums):
        if(i % 2 == 1) == (arrnums[i-1] > arrnums[i]):
            arrnums[i-1], arrnums[i] = arrnums[i], arrnums[i-1]
    return arrnums

#nums = [234,43,432,54,34,54,3,2,1,234,900]
nums = list(map(int, input().split()))
print(nums)
print(wiggleSort(nums))


