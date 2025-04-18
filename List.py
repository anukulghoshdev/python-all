# list mutable, different value allow, 
"""
mixed = [1, "Hello", 3.14, True]
numbers = [10, 20, 30, 40, 50]

numbers.append(100)
numbers.insert(4, 33)

numbers.remove(20)
popped = numbers.pop() #100
print(popped) 

print(numbers)
"""

#list slicing 
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[::-1]) 
#[start, end, steps]  -1 মানে উল্টো দিকে যাবে, অর্থাৎ লিস্ট রিভার্স হবে!

nums = [5, 10, 15, 20, 25, 30, 35]
print(nums[::2][::-1]) #***

#List Comprehension***
squares = [x**2 for x in range(1, 6)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

"""
number = [5, 10, 15, 20, 25, 30]
double = [x*2 for x in list]
print(double)
"""

number2 = [2, 4, 6, 8, 10]
total = sum(number2)
print(total)

"""
sum = 0
for x in number2:
    sum += x
print(sum)
"""

#List modification
numbers = [10, 20, 30, 40]
numbers[1] = 25  # দ্বিতীয় উপাদান পরিবর্তন
print(numbers)  # [10, 25, 30, 40]  লিস্ট mutable, তাই যেকোনো উপাদান পরিবর্তন করা যায়।

#list merge (Concatenation & Extend)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combind = list1+list2
print(combind)

list1.extend(list2)
print(list1)

#list copy(shallow Copy vs Deep Copy)
original = [1, 2, 3]
copy1 = original  # Shallow Copy
copy2 = original[:]  # নতুন লিস্ট তৈরি (Deep Copy), অপরিবর্তিত থাকবে P

original[0] = 100
print(copy1)  # [100, 2, 3] (Shallow Copy, একই রেফারেন্স)
print(copy2)  # [1, 2, 3] (Deep Copy, আলাদা লিস্ট)

#list counting
nums = [1, 2, 3, 2, 4, 2, 5]
print(nums.count(2))  # 3 (লিস্টে ২ কতবার আছে)

#list reverse and 
numbers = [5, 2, 9, 1, 5]
numbers.sort(reverse=True) # make desecnding order - high to low
sorted_numbers = sorted(numbers, reverse=True) 
# numbers.reverse()
print(numbers)
print(sorted_numbers)

#2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][1])

matrix_3 = [
    [3, 4, 5],
    [5, 2, 9],
    [7, 4, 3]
]
new_1d_matrix = [num for row in matrix for num in row]
print(f"New 1D matrix: {new_1d_matrix}")


#sum of all row in a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(f"sum of rows: {sum(row)}")