def prefixSum(arr):

    prefixSum = []
    prefixSum.append(arr[0])

    for i in range(1, len(arr)):
        prefixSum.append(prefixSum[i - 1] + arr[i])

    return prefixSum


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(prefixSum(arr))