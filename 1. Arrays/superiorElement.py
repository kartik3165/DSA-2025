nu = [1, 2, 3, 2]
ans = []
max_so_far = float('-inf')

for i in range(len(nu) - 1, -1, -1):
    if nu[i] > max_so_far:
        ans.append(nu[i])
        max_so_far = nu[i]

ans.reverse()
print("Superior numbers:", ans)
