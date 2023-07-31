# two conditions - first - : second - indentation

# if block
if True:
    print("hai")
print("bye")
# example 1
x = 35
r = x % 2
if r != 0:
    print("odd")
# nested if
x = 5
y = 12
if x > 0:
    if (y < x):
        print("nested if works")
    print("this is part of outer if")
print("this is part of code completely out of if block")

# if-else
x = 45
y = 'mahesh'
if x != 0 & len(y) > 0:
    print("conditions satisfied and its true")
else:
    print("false")
# bitwise & and and operate differently
x = 45
y = 'mahesh'
if x != 0 and len(y) > 0:
    print("conditions satisfied and its true")
else:
    print("false")
# if - elif - else
x = 4
y = 5
z = 6
if x>y and x>z :
    print("x i bigger")
elif y>z  :
    print("y is big")
else :
    print("z is big")