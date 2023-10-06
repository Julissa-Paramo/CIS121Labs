'''
Julissa Paramo
10 / 6 / 23
Filter and Sort a List
'''


nums = input()

nums1 = nums.split()

nums2 = list(map(int, nums1))

sortedlist = sorted(nums2)

negvals = []

for num in sortedlist:

    if num < 0:

        negvals.append(num)
        
print(' '.join(map(str, negvals[::-1])))
