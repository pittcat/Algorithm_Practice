```
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(set(nums))
    c_nums = nums.copy()
    nums = []
    for i in set(c_nums):
        nums.append(i)
    return length

nums=[1,1,2]
res=removeDuplicates(nums)
```
为什么nums 依然是[1,1,2]

