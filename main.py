from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dic1 = {}
    for i, num in enumerate(nums):
        a = target - num
        if a in dic1:
            return [dic1[a], i]
        dic1[num] = i
    return []


nums_input = input("input(콤마로 구분): ")
target_input = int(input("target = "))
nums = list(map(int, nums_input.split(',')))

result = twoSum(nums, target_input)

print("Output:", result)