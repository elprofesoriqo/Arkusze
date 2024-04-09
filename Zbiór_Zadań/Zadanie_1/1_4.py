def maxarr(arr):
    max_ending_here = max_so_far = arr[0]
    start_index = end_index = temp_start_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start_index = i
        else:
            max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start_index = temp_start_index
            end_index = i

    return max_so_far, start_index, end_index
arr=[]
with open("dane1_4.txt") as file:
    for row in file:
        arr.append(int(row.strip()))

print(maxarr(arr))