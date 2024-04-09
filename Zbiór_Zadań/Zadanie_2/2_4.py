def good(arr):
    op=cl=0
    for char in arr:
        if char=='[':
            op+=1
        else:
            cl+=1
    
    if op-cl!=0:
        return False
    return True






bracket={}
with open("dane2_4.txt") as file:
    for row in file:
        row=row.strip()
        bracket[row]=good(row)

print(bracket)