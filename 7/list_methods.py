food_list = ['pizza','burger','fries']

print(*food_list)
print()

food_list.insert(-20,'Sushi')
print("after inserting sushi:")
print(*food_list)
print()

food_list.remove('burger')
print("after removing burger:")
print(*food_list)
print()

food_list.sort()
print("after sorting")
print(*food_list)
print()

del food_list[0]
#del food_list[30]

print(*food_list)
print()

print(max(food_list))
