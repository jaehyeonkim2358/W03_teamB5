from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline
nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

def post_order(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if nums[i] > nums[start]:
            mid = i
            break

    post_order(start + 1, mid - 1)      
    post_order(mid, end)                
    print(nums[start])                  

post_order(0, len(nums) - 1)
