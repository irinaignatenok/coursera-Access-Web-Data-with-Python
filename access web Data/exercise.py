import re
hand = open("new_data.txt")
x = list()
sum = 0
for line in hand:
    y = re.findall('[0-9]+',line)
    x+=y
    print(y)

for num in x:
    a_string = ''.join(num)
    an_integer = int(a_string)
    sum = sum + an_integer

print(sum)
