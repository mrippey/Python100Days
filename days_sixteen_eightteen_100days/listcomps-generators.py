#List Comprehension Exercise 1: Find all words in string that are less than four letters
exercise_str = """This string is a practice problem to work on list comprehensions, 
    which particularly I find quite difficult sometimes""".split()

def get_lessthan_four(s=exercise_str):
    return [word for word in s if len(word) < 4]


get_lessthan_four()


# Another one
nums = range(1, 1001)
def find_nums_div_by_eight(n = nums):
    for i in n:
        return [i for i in n if i  % 8 == 0]

find_nums_div_by_eight()


# A third list comprehension challenge 
# Below idea from: https://www.learnpython.org/en/List_Comprehensions
numbers = [34.6, -203.4, 44.9, 68.3, 12.2, 44.6, 12.7]

def get_only_positive(nums = numbers):
    newlst = [n for n in nums if n > 0]
    return newlst

get_only_positive()


# Trying a generator this time
def even_nums_only(num):
    even_nums = set() 
    for item in num:
        if item not in even_nums and (item % 2 == 0):
            yield item
            even_nums.add(item)
print('Even numbers from your list: ')

for k in even_nums_only([1, 2, 2, 1, 1, 3, 2, 1, 8 , 10, 11, 13]):
    print(k)
