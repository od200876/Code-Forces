n = int(input())
resutl = 0
approve = 0
for _ in range(n):
    enter, approve = '', 0
    enter = list(input().replace(' ', ''))
    for i in range(3):
        approve += int(enter[i])
    if approve >= 2:
        resutl += 1
        
print(resutl) 