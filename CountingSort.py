def counting_sort(arr):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
arr = [4,5,1,3,1,2,3,8]
print(counting_sort(arr))

#ord("A")->this is function for assci value
#chr(65)->this is function for character