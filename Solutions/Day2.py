# Q4 solution
my_list = input().split(',')
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)

#Q5 solution
class IOtest():
    def get_string(self):
        self.s = input()
    
    def print_string(self):
        print(self.s.upper())

ob1 = IOtest()
ob1.get_string()
ob1.print_string()

# Q6 Solution
import math
my_list = input().split(',')
my_list = [int(i) for i in my_list]
c,h = 50,30
for d in my_list:
    q = int(math.sqrt( 2*d*c//h)) 
    print(f'{q},', end='')

# Q7 solution
X = int(input('enter no of rows\n'))
Y = int(input('enter no of columns \n'))
my_array=[[0 for row in range(Y)] for col in range(X)]
for i in range(0,X):
    for j in range(0,Y):
        my_array[i][j] = i*j

print(my_array)

# Q8 Solution
my_list = input().split(',')
my_list.sort()
print(','.join(item for item in my_list))

# Q9 Solution

s= []
while True:
    string= input()
    if string:
        s.append(string.upper())
    else: break
print('\n'.join(s))
