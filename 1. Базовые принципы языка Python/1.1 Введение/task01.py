n = int(input())
number_list = []

for number in range(n):
    number = [int(i) for i in input().split('\n')]
    number_list.append(number)
    
number_list = sum(number_list, [])
print(sum(number_list))