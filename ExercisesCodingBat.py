def big_diff(nums):
    min_result = 100500
    max_result = -1
    for i in nums:
        min_result = min(min_result, i)
        max_result = max(max_result, i)

    return max_result - min_result

def has22(nums):
    for i in range(0, len(nums), 1):
        print(i)

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1] and nums[i] == 2:
      return True
  return False

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      count = count+1
  return count


def main():
    nums = ([10, 3, 5, 6])
    print(big_diff(nums))

    nums2 = ([1, 1, 2])
    print(has22(nums2))

    count_hi('abc hi ho')
    count_hi('ABChi hi')
    count_hi('hihi')

if __name__  == "__main__": main()


1 loop.. Use + to combine strings, len(str) is the number of chars in a String, str[i:j] extracts the substring starting
at index i and running up to but not including index j.

