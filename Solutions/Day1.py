# Q1 solution
nums = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]

print(nums)

# Q2 solution
n = 8
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Q3 Solution
n=8
my_dict = {i: i*i for i in range(1, n+1)}
print(my_dict)

