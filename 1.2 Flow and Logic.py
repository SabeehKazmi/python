# and or not operators
(2 < 3) or (3 < 2)
(12+3*2 == 3+3*5) and (1 == 1)
not (2 < 3)

#while loop exp.1
a = 5
while a < 10:
    print(a)
    a = a + 1
print("done")

#while loop exp.2
while True:
    print('Enter your name: ')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

#continuous loop
while True:
    print('Who are you?')
    name = input()
    if name != 'Hassan':
        continue
    print('Hello, Hassan. What is the password?')
    passw = input()
    if passw == 'death':
        break
print('Access granted.')
