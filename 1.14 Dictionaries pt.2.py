# in some cases, for better understanding the output, we need to print it pretty
# this is why we will use pprint() and pformat(), use them and observe the output
import pprint
nest_dir = {
    'name':'hassan',
    'class':'software engineering',
    'subjects':['programming','networking','cybersec','database'],
    'gpa':'3.29'
}
# pprint.pprint(nest_dir) # observe the output... and you know what's even better than this?

# this
for a, b in nest_dir.items():
    if isinstance(b, list):
        for c in b:
            pprint.pprint(a + ' | ' + str(c))
    else:
        pprint.pprint(a + ' | ' + str(b))
print('\n' * 3)

# what pformat() for?
# same case with pformat
for itm, val in nest_dir.items():
    if isinstance(val, list):
        for sub_val in val:
            pprint.pformat(itm + ' | ' + str(sub_val))
    else:
        pprint.pformat(itm + ' | ' + str(val))
# no output? because pformat() only returns a string and doesn't output something
# we need to insert this all in print() to produce an output
# like this:
for itm, val in nest_dir.items():
    if isinstance(val, list):
        for sub_val in val:
            print(pprint.pformat(itm + ' | ' + str(sub_val)))
    else:
        print(pprint.pformat(itm + ' | ' + str(val)))
# observed something?
# no difference b/w pprint() and pformat() right? because pformat() returns pretty-formatted string that you can store in a file e.g., logs
# in a pretty format | pretty useful, right!

