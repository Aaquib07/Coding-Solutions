def houseRobber(arr):
    def findMaxAmount(arr):
        """
        TC - O(n)
        SC - O(1)
        """
        prev = arr[0]
        prevOfPrev = 0
        for i in range(1, len(arr)):
            take = arr[i]
            if i > 1:
                take += prevOfPrev
            notTake = 0 + prev
            curr = max(take, notTake)
            prevOfPrev = prev
            prev = curr
        return prev
    
    temp1 = arr[1:]
    temp2 = arr[:-1]
    if len(arr) == 1:
        return arr[0]
    result = max(findMaxAmount(temp1), findMaxAmount(temp2))
    return result

if __name__ == '__main__':
    arr = [2, 3, 2, 10, 20]
    result = houseRobber(arr)
    print(result)