def deep(arr):

    max_dp=0
    dp=0
    for char in arr:
        if char=='[':
            dp+=1
        else:
            max_dp=max(dp,max_dp)
            dp-=1

    return max_dp




bracket={}
with open("dane2_3.txt") as file:
    for row in file:
        row=row.strip()
        bracket[row]=deep(row)
        

print(bracket)