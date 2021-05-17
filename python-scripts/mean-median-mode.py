# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections
import math

x = int(input())
nums = list(map(int, input().split(' ')))
nums.sort()

mean = sum(nums)/x


if((x % 2) == 0):
    middleIndex = int(x/2)
    median = (nums[middleIndex-1] + nums[middleIndex]) / 2
else:
    middelIndex = int(math.floor(x/2))
    median = [middelIndex]

counterList = collections.Counter(nums).most_common(1)


print(mean)
print(median)
print([x[0] for x in counterList][0])

