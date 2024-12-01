list1 = []
list2 = []

with open("../../inputs/day1.txt", "r") as file:
    for line in file :
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))


list1.sort()
list2.sort()

sum = 0

for i in range(len(list1)) :
    n1 = list1[i]
    n2 = list2[i]
    sum += (abs(n1 - n2))


print(sum)


