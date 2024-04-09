def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

with open('dane1_3.txt', 'r') as file:
    array = [int(line.strip()) for line in file]

max_sum = max_subarray_sum(array)

print("Największa suma segmentu tablicy A:", max_sum)
