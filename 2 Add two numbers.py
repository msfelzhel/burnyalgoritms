def addTwoNumbers (l1:list[int],l2:list[int]):
    sum1 = ''
    sum2 = ''
    for i in l1:
        sum1 = sum1 + str(i)
    for i in l2:
        sum2 = sum2 + str(i)
    ans_sum = int(sum1) + int(sum2)
    itt = ''
    for i in str(ans_sum):
        itt = i + itt
    it = []
    for i in itt:
        it.append(int(i))
    return it
        

print(addTwoNumbers([2,4,3],[5,6,4]))
print(addTwoNumbers([0],[0]))
print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
