string = input().split(" ")
h = int(string[0])
n = int(string[1])


h_withlastleap = h - 10
block_h = 0
i = 0

print(n)

while n > i:
    i = i + 1
    
    n = n - i
    block_h = block_h + 10
    print(f"block_h: {block_h} | n: {n} | i: {i}")
    
    
print(f"block_h: {block_h} vs h_withlastleap: {h_withlastleap}")
if(h_withlastleap <= block_h):
    print("YES")
else:
    print("NO")