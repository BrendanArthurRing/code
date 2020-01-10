def arrayChange(arr):

    counter = 0
    arr_index = 1

    for i, j in zip(arr, arr[1:]):
        if i >= j:
            value = abs(j - i) + 1
            arr[arr_index] += value
            counter += value
            arr_index += 1
        elif i < j:
            arr_index += 1

    return counter


# Top Voted solution was
def arrayChange(inputArray):
    a = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            a += f
    return a

# My Spin off


def arrayChange(arr):
    c = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            v = (arr[i - 1] - arr[i]) + 1
            arr[i] += v
            c += v
    return c
