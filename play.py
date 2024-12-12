L = [4,5,8,3,9,7,2,1]
print("Original List:",L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("Total =", count)
print("Average =", avg)
L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])