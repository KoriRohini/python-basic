num = [12, 13, 67, 88]

num.append(12)



num.insert(3, 14)
num.remove(12)
num.pop(2)

del num[3:4]
num.extend([12, 13])

print(min(num))
print(max(num))
print(sum(num))

num[2] = 13
num.sort()
num.reverse()
