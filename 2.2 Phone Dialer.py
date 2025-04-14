import msvcrt, winsound, re
# msvcrt for reading the keystoke without pressing enter
# winsound for sounds
# re for checking a format

def play(frequency, duration=200):
    winsound.Beep(frequency, duration)

def isvalid(number):
    return re.fullmatch(r'\d{4}-\d{7}',number)

print('Dial a number: (format: 0300-0000000)')
p_no=''

while True:
    p_no_digit=msvcrt.getch().decode('utf-8')
    if p_no_digit.isdigit() or p_no_digit=='-':
        print(p_no_digit, end='', flush=True)
        p_no+=p_no_digit
        play(600)
    elif p_no_digit=='\r':
        print()
        if isvalid(p_no):
            print("Valid!")
            play(800)
        else:
            print('Invalid!')
            play(400)
        break
