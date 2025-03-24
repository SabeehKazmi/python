import time, sys
indent = 0
is_increasing = True
def zigzag(a, b):
    while True:
        print(a*' ', '*****')
        time.sleep(0.2)
        if b:
            a = a + 1
            if a == 8:
                b = False
        else:
            a = a - 1
            if a == 0:
                b = True
try:
    zigzag(indent, is_increasing)
except KeyboardInterrupt:
    print('you pressed it, huh!')
    sys.exit()

# desired output
# *****
#  *****
#   *****
#  *****
# *****
#  *****
# .... continue on until KeyboardInterrupt