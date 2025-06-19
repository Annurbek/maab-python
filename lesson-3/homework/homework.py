def input_int_list(prompt=""):
    return list(map(int, input(prompt).split()))

def input_int_tuple(prompt=""):
    return tuple(map(int, input(prompt).split()))

task_1 = input_int_list()
element = int(input())
print(task_1.count(element))

task_2 = input_int_list()
print(sum(task_2))

task_3 = input_int_list()
print(max(task_3) if task_3 else "Empty list")

task_4 = input_int_list()
print(min(task_4) if task_4 else "Empty list")

task_5 = input_int_list()
element = int(input())
print("YES" if element in task_5 else "NO")

task_6 = input_int_list()
print(task_6[0] if task_6 else "List is empty")

task_7 = input_int_list()
print(task_7[-1] if task_7 else "List is empty")

task_8 = input_int_list()
print(task_8[:3])

task_9 = input_int_list()
print(task_9[::-1])

task_10 = input_int_list()
task_10.sort()
print(task_10)

task_11 = input_int_list()
print(set(task_11))

def insert_element_at_index(lst, element, index):
    if index < 0 or index > len(lst):
        raise IndexError("out of range")
    lst.insert(index, element)
    return lst

task_12 = input_int_list()
new_element = int(input())
insert_index = int(input())
result = insert_element_at_index(task_12, new_element, insert_index)
print(result)

task_13 = input_int_list()
new_element = int(input())
try:
    index = task_13.index(new_element)
    print(f"Element {new_element} found at index {index}")
except ValueError:
    print("Element not found")

task_14 = input_int_list()
print(len(task_14) == 0)

task_15 = input_int_list()
even_count = sum(1 for num in task_15 if num % 2 == 0)
print(even_count)

task_16 = input_int_list()
odd_count = sum(1 for num in task_16 if num % 2 != 0)
print(odd_count)

task_17 = input_int_list()
task_17_2 = input_int_list()
task_17.extend(task_17_2)
print(task_17)

task_18 = input_int_list()
task_18_2 = input_int_list()
print(all(x in task_18 for x in task_18_2))

task_19 = input_int_list()
element_to_replace = int(input())
new_value = int(input())
try:
    idx = task_19.index(element_to_replace)
    task_19[idx] = new_value
    print(task_19)
except ValueError:
    print("Element not found")

task_20 = input_int_list()
if len(set(task_20)) < 2:
    print("No second largest")
else:
    first, second = float('-inf'), float('-inf')
    for x in set(task_20):
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    print(second)

task_21 = input_int_list()
if len(set(task_21)) < 2:
    print("No second smallest")
else:
    first, second = float('inf'), float('inf')
    for x in set(task_21):
        if x < first:
            second = first
            first = x
        elif first < x < second:
            second = x
    print(second)

task_22 = input_int_list("Enter a list of numbers for task 22: ")
even_numbers = [num for num in task_22 if num % 2 == 0]
print("Even numbers:", even_numbers)

task_23 = input_int_list("Enter a list of numbers for task 23: ")
odd_numbers = [num for num in task_23 if num % 2 != 0]
print("Odd numbers:", odd_numbers)

task_24 = input_int_list("Enter a list of numbers for task 24: ")
print("Length of list:", len(task_24))

task_25 = input_int_list("Enter a list of numbers for task 25: ")
print("Copy of list:", task_25.copy())

task_26 = input_int_list("Enter a list of numbers for task 26: ")
n = len(task_26)
if n == 0:
    print("List is empty")
elif n % 2 == 1:
    print("Middle element:", task_26[n // 2])
else:
    print("Middle elements:", task_26[n // 2 - 1], task_26[n // 2])

start_27 = int(input("Enter the start index for task 27: "))
end_27 = int(input("Enter the end index for task 27: "))
task_27 = input_int_list("Enter a list of numbers for task 27: ")
sublist = task_27[start_27:end_27]
if sublist:
    print("Max in sublist:", max(sublist))
    print("Min in sublist:", min(sublist))
else:
    print("Empty sublist")

index_29 = int(input("Enter the index to remove for task 29: "))
task_29 = input_int_list("Enter a list of numbers for task 29: ")
if 0 <= index_29 < len(task_29):
    task_29.pop(index_29)
    print("List after removal:", task_29)
else:
    print("Index out of range")

task_30 = input_int_list("Enter a list of numbers for task 30: ")
print("Is the list sorted:", task_30 == sorted(task_30))

n_31 = int(input("Enter the repetition count for task 31: "))
task_31 = input_int_list("Enter a list of numbers for task 31: ")
repeated_elements = []
for num in task_31:
    repeated_elements.extend([num] * n_31)
print("List with repeated elements:", repeated_elements)

task_32_1 = input_int_list("Enter the first list for task 32: ")
task_32_2 = input_int_list("Enter the second list for task 32: ")
merged_sorted_list = sorted(task_32_1 + task_32_2)
print("Merged and sorted list:", merged_sorted_list)

element_33 = int(input("Enter an element to find indices for task 33: "))
task_33 = input_int_list("Enter a list of numbers for task 33: ")
indices = [i for i, x in enumerate(task_33) if x == element_33]
print("Indices of element:", indices)

task_34 = input_int_list("Enter a list of numbers for task 34: ")
if task_34:
    rotated_list = [task_34[-1]] + task_34[:-1]
else:
    rotated_list = []
print("Rotated list:", rotated_list)

start_35 = int(input("Enter the start of the range for task 35: "))
end_35 = int(input("Enter the end of the range for task 35: "))
range_list = list(range(start_35, end_35 + 1))
print("Range list:", range_list)

task_36 = input_int_list("Enter a list of numbers for task 36: ")
positive_sum = sum(x for x in task_36 if x > 0)
print("Sum of positive numbers:", positive_sum)
negative_sum = sum(x for x in task_36 if x < 0)
print("Sum of negative numbers:", negative_sum)

task_38 = input_int_list("Enter a list of numbers for task 38: ")
is_palindrome = task_38 == task_38[::-1]
print("Is the list a palindrome:", is_palindrome)

size_39 = int(input("Enter the size of sublists for task 39: "))
task_39 = input_int_list("Enter a list of numbers for task 39: ")
nested_list = [task_39[i:i + size_39] for i in range(0, len(task_39), size_39)]
print("Nested list:", nested_list)

task_40 = input_int_list("Enter a list of numbers for task 40: ")
unique_elements = []
for num in task_40:
    if num not in unique_elements:
        unique_elements.append(num)
print("Unique elements in order:", unique_elements)

### Tuple Tasks

tuple_22 = input_int_tuple("Enter a tuple for task 22: ")
element_22 = int(input("Enter the element to count for task 22: "))
print("Occurrences:", tuple_22.count(element_22))

tuple_23 = input_int_tuple("Enter a tuple for task 23: ")
print("Max element:", max(tuple_23) if tuple_23 else "Empty tuple")

tuple_24 = input_int_tuple("Enter a tuple for task 24: ")
print("Min element:", min(tuple_24) if tuple_24 else "Empty tuple")

tuple_25 = input_int_tuple("Enter a tuple for task 25: ")
element_25 = int(input("Enter the element to check for task 25: "))
print("Element present:", element_25 in tuple_25)

tuple_26 = input_int_tuple("Enter a tuple for task 26: ")
print("First element:", tuple_26[0] if tuple_26 else "Tuple is empty")

tuple_27 = input_int_tuple("Enter a tuple for task 27: ")
print("Last element:", tuple_27[-1] if tuple_27 else "Tuple is empty")

tuple_28 = input_int_tuple("Enter a tuple for task 28: ")
print("Tuple length:", len(tuple_28))

tuple_29 = input_int_tuple("Enter a tuple for task 29: ")
print("First three elements:", tuple_29[:3])

tuple_30_1 = input_int_tuple("Enter the first tuple for task 30: ")
tuple_30_2 = input_int_tuple("Enter the second tuple for task 30: ")
print("Concatenated tuple:", tuple_30_1 + tuple_30_2)

tuple_31 = input_int_tuple("Enter a tuple for task 31: ")
print("Is tuple empty:", not bool(tuple_31))

tuple_32 = input_int_tuple("Enter a tuple for task 32: ")
element_32 = int(input("Enter the element for task 32: "))
indices_32 = [i for i, x in enumerate(tuple_32) if x == element_32]
print("Indices of element:", indices_32)

tuple_33 = input_int_tuple("Enter a tuple for task 33: ")
s33 = sorted(set(tuple_33))
second_largest = s33[-2] if len(s33) > 1 else None
print("Second largest element:", second_largest)

tuple_34 = input_int_tuple("Enter a tuple for task 34: ")
s34 = sorted(set(tuple_34))
second_smallest = s34[1] if len(s34) > 1 else None
print("Second smallest element:", second_smallest)

element_35 = int(input("Enter an element for task 35: "))
print("Single element tuple:", (element_35,))

list_36 = input_int_list("Enter a list for task 36: ")
print("Converted to tuple:", tuple(list_36))

tuple_37 = input_int_tuple("Enter a tuple for task 37: ")
print("Is the tuple sorted:", tuple_37 == tuple(sorted(tuple_37)))

start_38 = int(input("Enter the start index for task 38: "))
end_38 = int(input("Enter the end index for task 38: "))
tuple_38 = input_int_tuple("Enter a tuple for task 38: ")
subtuple = tuple_38[start_38:end_38]
if subtuple:
    print("Max of subtuple:", max(subtuple))
    print("Min of subtuple:", min(subtuple))
else:
    print("Empty subtuple")

tuple_39 = input_int_tuple("Enter a tuple for task 39: ")
element_39 = int(input("Enter the element to remove for task 39: "))
new_tuple_39 = tuple(x for x in tuple_39 if x != element_39)
print("Tuple after removal:", new_tuple_39)

tuple_40 = input_int_tuple("Enter a tuple for task 40: ")
size_40 = int(input("Enter the size of subtuples for task 40: "))
nested_tuple_40 = tuple(tuple_40[i:i + size_40] for i in range(0, len(tuple_40), size_40))
print("Nested tuple:", nested_tuple_40)

tuple_41 = input_int_tuple("Enter a tuple for task 41: ")
repeat_count_41 = int(input("Enter the repeat count for task 41: "))
repeated_tuple_41 = tuple(x for x in tuple_41 for _ in range(repeat_count_41))
print("Repeated tuple:", repeated_tuple_41)

start_42 = int(input("Enter the start for task 42: "))
end_42 = int(input("Enter the end for task 42: "))
range_tuple_42 = tuple(range(start_42, end_42 + 1))
print("Range tuple:", range_tuple_42)

tuple_43 = input_int_tuple("Enter a tuple for task 43: ")
print("Reversed tuple:", tuple_43[::-1])

tuple_44 = input_int_tuple("Enter a tuple for task 44: ")
print("Is the tuple palindrome:", tuple_44 == tuple_44[::-1])

tuple_45 = input_int_tuple("Enter a tuple for task 45: ")
unique_elements_45 = tuple(sorted(set(tuple_45), key=tuple_45.index))
print("Unique elements:", unique_elements_45)

set_1 = set(input_int_list())
set_2 = set(input_int_list())
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 - set_2)
print(set_1 <= set_2)
element_5 = int(input())
print(element_5 in set_1)
print(len(set_1))
list_7 = input_int_list()
print(set(list_7))
element_8 = int(input())
set_1.discard(element_8)
print(set_1)
set_9 = set(set_1)
set_9.clear()
print(set_9)
print(len(set_1) == 0)
print(set_1 ^ set_2)
element_11 = int(input())
set_1.add(element_11)
print(set_1)
if set_1:
    print(set_1.pop())
    print(max(set_1))
    print(min(set_1))
else:
    print("Set is empty")
set_12 = set(input_int_list())
even_numbers = {x for x in set_12 if x % 2 == 0}
print(even_numbers)
odd_numbers = {x for x in set_12 if x % 2 != 0}
print(odd_numbers)
start_14 = int(input())
end_14 = int(input())
range_set = set(range(start_14, end_14 + 1))
print(range_set)
list_16_1 = input_int_list()
list_16_2 = input_int_list()
merged_set = set(list_16_1 + list_16_2)
print(merged_set)
print(set_1.isdisjoint(set_2))
list_18 = input_int_list()
unique_list = list(set(list_18))
print(unique_list)
print(len(set(list_18)))
import random
set_20 = {random.randint(1, 100) for _ in range(10)}
print(set_20)

dict_1 = {"a": 1, "b": 2, "c": 3}
key_1 = input()
print(dict_1.get(key_1, "Key not found"))

key_2 = input()
print(key_2 in dict_1)

print(len(dict_1))

print(list(dict_1.keys()))

print(list(dict_1.values()))

dict_2 = {"d": 4, "e": 5}
merged_dict = dict_1.copy()
merged_dict.update(dict_2)
print(merged_dict)

key_4 = input()
dict_1.pop(key_4, None)
print(dict_1)

dict_5 = {}
print(len(dict_5) == 0)

key_6 = input()
print({key_6: dict_1.get(key_6)} if key_6 in dict_1 else "Key not found")

key_7 = input()
value_7 = input()
dict_1[key_7] = value_7
print(dict_1)

value_8 = input()
print([key for key, value in dict_1.items() if value == value_8])

keys_list = input().split()
values_list = input().split()
new_dict = dict(zip(keys_list, values_list))
print(new_dict)

print(any(isinstance(value, dict) for value in dict_1.values()))

nested_dict = {"a": {"x": 10}, "b": {"y": 20}}
key_9 = input()
nested_key_9 = input()
print(nested_dict.get(key_9, {}).get(nested_key_9, "Not Found"))

default_dict = dict.fromkeys(["a", "b", "c"], 0)
print(default_dict)

print(len(set(dict_1.values())))

sorted_dict_by_key = dict(sorted(dict_1.items()))
print(sorted_dict_by_key)

sorted_dict_by_value = dict(sorted(dict_1.items(), key=lambda item: item[1]))
print(sorted_dict_by_value)

filtered_dict = {key: value for key, value in dict_1.items() if isinstance(value, int) and value > 1}
print(filtered_dict)

dict_10 = {"a": 1, "b": 2}
dict_11 = {"b": 2, "c": 3}
print(bool(dict_10.keys() & dict_11.keys()))

tuple_12 = (("a", 1), ("b", 2))
dict_from_tuple = dict(tuple_12)
print(dict_from_tuple)

print(next(iter(dict_1.items())))