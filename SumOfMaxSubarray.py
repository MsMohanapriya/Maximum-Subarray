def maxSumSubarray(array_Size, max_sum, array):
    maxSum = float('-inf')
    currentSum = 0
    start = 0
    end = 0

    while end < array_Size:
        currentSum += array[end]

        while currentSum > max_sum:
            currentSum -= array[start]
            start += 1

        maxSum = max(maxSum, currentSum)

        end += 1

    return maxSum

array_Size=int(input("Enter array size: "))
max_sum=int(input("Enter the maximum sum: "))
array=list(map(int,input("Enter the array ").split()))
result = maxSumSubarray(array_Size, max_sum, array)
print(result)
