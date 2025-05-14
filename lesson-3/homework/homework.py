### List Tasks

task_1 = list(map(int, input().split()))
element = int(input())
print(task_1.count(element))

task_2 = list(map(int, input().split()))
print(sum(task_2))

task_3 = list(map(int, input().split()))
print(max(task_3))

task_4 = list(map(int, input().split()))
print(min(task_4))

task_5 = list(map(int, input().split()))
element = int(input())
if element in task_5:
    print("YES")
else:
    print("NO")

task_6 = list(map(int, input().split()))
if len(task_6) == 0:
    print("List is empty")
else:
    print(task_6[0])

task_7 = list(map(int, input().split()))
if len(task_7) == 0:
    print("List is empty")
else:
    print(task_7[-1])

task_8 = list(map(int, input().split()))
res = [task_8[:3]]
print(res)

task_9 = list(map(int, input().split()))
res = [task_9[-1:]]
print(res)

task_10 = list(map(int, input().split()))
print(task_10.sort())

task_11 = list(map(int, input().split()))
print(set(task_11))


def insert_element_at_index(lst, element, index):
    if index < 0 or index > len(lst):
        raise IndexError("out of range")
    lst.insert(index, element)
    return lst

task_12 = list(map(int, input().split()))
new_element = int(input())
insert_index = int(input())

result = insert_element_at_index(task_12, new_element, insert_index)
print(result)

task_13 = list(map(int, input().split()))
new_element = int(input())

index = task_13.index(new_element)
print(f"Element {new_element} found at index {index}")

task_14 = list(map(int, input().split()))
print(len(task_14)==0)

task_15 = list(map(int, input().split()))
even_count = sum(1 for num in task_15 if num % 2 == 0)
print(even_count)

task_16 = list(map(int, input().split()))
even_count = sum(1 for num in task_16 if num % 2 != 0)
print(even_count)

task_17 = list(map(int, input().split()))
task_17_2 = list(map(int, input().split()))
task_17.extend(task_17_2)
print(task_17)

task_18 = list(map(int, input().split()))
task_18_2 = list(map(int, input().split()))
print(True if task_18_2 in task_18 else False)

task_19 = list(map(int, input().split()))
task_19[0], task_19[-1] = task_19[-1], task_19[0]
print(task_19)

task_20 = list(map(int, input().split()))
task_20_2 = set(task_20)
print(sorted(task_20_2)[-2])

task_21 = list(map(int, input().split()))
task_21_2 = set(task_21)
print(sorted(task_21_2)[-2])

task_22 = list(map(int, input("Enter a list of numbers for task 22: ").split()))
even_numbers = [num for num in task_22 if num % 2 == 0]
print("Even numbers:", even_numbers)

task_23 = list(map(int, input("Enter a list of numbers for task 23: ").split()))
odd_numbers = [num for num in task_23 if num % 2 != 0]
print("Odd numbers:", odd_numbers)

task_24 = list(map(int, input("Enter a list of numbers for task 24: ").split()))
print("Length of list:", len(task_24))

task_25 = list(map(int, input("Enter a list of numbers for task 25: ").split()))
print("Copy of list:", task_25.copy())

task_26 = list(map(int, input("Enter a list of numbers for task 26: ").split()))
n = len(task_26)
if n % 2 == 1:
    print("Middle element:", task_26[n // 2])
else:
    print("Middle elements:", task_26[n // 2 - 1], task_26[n // 2])

start_27 = int(input("Enter the start index for task 27: "))
end_27 = int(input("Enter the end index for task 27: "))
task_27 = list(map(int, input("Enter a list of numbers for task 27: ").split()))
print("Max in sublist:", max(task_27[start_27:end_27]))

print("Min in sublist:", min(task_27[start_27:end_27]))

index_29 = int(input("Enter the index to remove for task 29: "))
task_29 = list(map(int, input("Enter a list of numbers for task 29: ").split()))
if 0 <= index_29 < len(task_29):
    task_29.pop(index_29)
    print("List after removal:", task_29)
else:
    print("Index out of range")

task_30 = list(map(int, input("Enter a list of numbers for task 30: ").split()))
print("Is the list sorted:", task_30 == sorted(task_30))

n_31 = int(input("Enter the repetition count for task 31: "))
task_31 = list(map(int, input("Enter a list of numbers for task 31: ").split()))
repeated_elements = [num for num in task_31 for _ in range(n_31)]
print("List with repeated elements:", repeated_elements)

task_32_1 = list(map(int, input("Enter the first list for task 32: ").split()))
task_32_2 = list(map(int, input("Enter the second list for task 32: ").split()))
merged_sorted_list = sorted(task_32_1 + task_32_2)
print("Merged and sorted list:", merged_sorted_list)

element_33 = int(input("Enter an element to find indices for task 33: "))
task_33 = list(map(int, input("Enter a list of numbers for task 33: ").split()))
indices = [i for i, x in enumerate(task_33) if x == element_33]
print("Indices of element:", indices)

task_34 = list(map(int, input("Enter a list of numbers for task 34: ").split()))
rotated_list = [task_34[-1]] + task_34[:-1]
print("Rotated list:", rotated_list)

start_35 = int(input("Enter the start of the range for task 35: "))
end_35 = int(input("Enter the end of the range for task 35: "))
range_list = list(range(start_35, end_35 + 1))
print("Range list:", range_list)

task_36 = list(map(int, input("Enter a list of numbers for task 36: ").split()))
positive_sum = sum(x for x in task_36 if x > 0)
print("Sum of positive numbers:", positive_sum)

negative_sum = sum(x for x in task_36 if x < 0)
print("Sum of negative numbers:", negative_sum)

task_38 = list(map(int, input("Enter a list of numbers for task 38: ").split()))
is_palindrome = task_38 == task_38[::-1]
print("Is the list a palindrome:", is_palindrome)

size_39 = int(input("Enter the size of sublists for task 39: "))
task_39 = list(map(int, input("Enter a list of numbers for task 39: ").split()))
nested_list = [task_39[i:i + size_39] for i in range(0, len(task_39), size_39)]
print("Nested list:", nested_list)

task_40 = list(map(int, input("Enter a list of numbers for task 40: ").split()))
unique_elements = []
for num in task_40:
    if num not in unique_elements:
        unique_elements.append(num)
print("Unique elements in order:", unique_elements)

### Tuple Tasks

tuple_22 = tuple(map(int, input("Enter a tuple for task 22: ").split()))
element_22 = int(input("Enter the element to count for task 22: "))
print("Occurrences:", tuple_22.count(element_22))

tuple_23 = tuple(map(int, input("Enter a tuple for task 23: ").split()))
print("Max element:", max(tuple_23))

tuple_24 = tuple(map(int, input("Enter a tuple for task 24: ").split()))
print("Min element:", min(tuple_24))

tuple_25 = tuple(map(int, input("Enter a tuple for task 25: ").split()))
element_25 = int(input("Enter the element to check for task 25: "))
print("Element present:", element_25 in tuple_25)

tuple_26 = tuple(map(int, input("Enter a tuple for task 26: ").split()))
print("First element:", tuple_26[0] if tuple_26 else "Tuple is empty")

tuple_27 = tuple(map(int, input("Enter a tuple for task 27: ").split()))
print("Last element:", tuple_27[-1] if tuple_27 else "Tuple is empty")

tuple_28 = tuple(map(int, input("Enter a tuple for task 28: ").split()))
print("Tuple length:", len(tuple_28))

tuple_29 = tuple(map(int, input("Enter a tuple for task 29: ").split()))
print("First three elements:", tuple_29[:3])

tuple_30_1 = tuple(map(int, input("Enter the first tuple for task 30: ").split()))
tuple_30_2 = tuple(map(int, input("Enter the second tuple for task 30: ").split()))
print("Concatenated tuple:", tuple_30_1 + tuple_30_2)

tuple_31 = tuple(map(int, input("Enter a tuple for task 31: ").split()))
print("Is tuple empty:", not bool(tuple_31))

tuple_32 = tuple(map(int, input("Enter a tuple for task 32: ").split()))
element_32 = int(input("Enter the element for task 32: "))
indices_32 = [i for i, x in enumerate(tuple_32) if x == element_32]
print("Indices of element:", indices_32)

tuple_33 = tuple(map(int, input("Enter a tuple for task 33: ").split()))
second_largest = sorted(set(tuple_33))[-2] if len(set(tuple_33)) > 1 else None
print("Second largest element:", second_largest)

tuple_34 = tuple(map(int, input("Enter a tuple for task 34: ").split()))
second_smallest = sorted(set(tuple_34))[1] if len(set(tuple_34)) > 1 else None
print("Second smallest element:", second_smallest)

element_35 = int(input("Enter an element for task 35: "))
print("Single element tuple:", (element_35,))

list_36 = list(map(int, input("Enter a list for task 36: ").split()))
print("Converted to tuple:", tuple(list_36))

tuple_37 = tuple(map(int, input("Enter a tuple for task 37: ").split()))
print("Is the tuple sorted:", tuple_37 == tuple(sorted(tuple_37)))

start_38 = int(input("Enter the start index for task 38: "))
end_38 = int(input("Enter the end index for task 38: "))
tuple_38 = tuple(map(int, input("Enter a tuple for task 38: ").split()))
print("Max of subtuple:", max(tuple_38[start_38:end_38]))

print("Min of subtuple:", min(tuple_38[start_38:end_38]))

tuple_39 = tuple(map(int, input("Enter a tuple for task 39: ").split()))
element_39 = int(input("Enter the element to remove for task 39: "))
new_tuple_39 = tuple(x for x in tuple_39 if x != element_39)
print("Tuple after removal:", new_tuple_39)

tuple_40 = tuple(map(int, input("Enter a tuple for task 40: ").split()))
size_40 = int(input("Enter the size of subtuples for task 40: "))
nested_tuple_40 = tuple(tuple_40[i:i + size_40] for i in range(0, len(tuple_40), size_40))
print("Nested tuple:", nested_tuple_40)

# Repeat Elements
tuple_41 = tuple(map(int, input("Enter a tuple for task 41: ").split()))
repeat_count_41 = int(input("Enter the repeat count for task 41: "))
repeated_tuple_41 = tuple(x for x in tuple_41 for _ in range(repeat_count_41))
print("Repeated tuple:", repeated_tuple_41)

start_42 = int(input("Enter the start for task 42: "))
end_42 = int(input("Enter the end for task 42: "))
range_tuple_42 = tuple(range(start_42, end_42 + 1))
print("Range tuple:", range_tuple_42)

tuple_43 = tuple(map(int, input("Enter a tuple for task 43: ").split()))
print("Reversed tuple:", tuple_43[::-1])

tuple_44 = tuple(map(int, input("Enter a tuple for task 44: ").split()))
print("Is the tuple palindrome:", tuple_44 == tuple_44[::-1])

tuple_45 = tuple(map(int, input("Enter a tuple for task 45: ").split()))
unique_elements_45 = tuple(sorted(set(tuple_45), key=tuple_45.index))
print("Unique elements:", unique_elements_45)

set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 - set_2)
print(set_1 <= set_2)
element_5 = int(input())
print(element_5 in set_1)
print(len(set_1))
list_7 = list(map(int, input().split()))
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
print(set_1.pop())
print(max(set_1))
print(min(set_1))
set_12 = set(map(int, input().split()))
even_numbers = {x for x in set_12 if x % 2 == 0}
print(even_numbers)
odd_numbers = {x for x in set_12 if x % 2 != 0}
print(odd_numbers)
start_14 = int(input())
end_14 = int(input())
range_set = set(range(start_14, end_14 + 1))
print(range_set)
list_16_1 = list(map(int, input().split()))
list_16_2 = list(map(int, input().split()))
merged_set = set(list_16_1 + list_16_2)
print(merged_set)
print(set_1.isdisjoint(set_2))
list_18 = list(map(int, input().split()))
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
print(list(key for key, value in dict_1.items() if value == value_8))

keys_list = list(input().split())
values_list = list(input().split())
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

filtered_dict = {key: value for key, value in dict_1.items() if value > 1}
print(filtered_dict)

dict_10 = {"a": 1, "b": 2}
dict_11 = {"b": 2, "c": 3}
print(bool(dict_10.keys() & dict_11.keys()))

tuple_12 = (("a", 1), ("b", 2))
dict_from_tuple = dict(tuple_12)
print(dict_from_tuple)

print(next(iter(dict_1.items())))