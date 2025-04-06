# in some cases, for better understanding the output, we need to print it pretty
# this is why we will use pprint() and pformat(), use them and observe the output
import pprint
nest_dir = {
    'name':'hassan',
    'class':'software engineering',
    'subjects':['programming','networking','cybersec','database'],
    'gpa':'3.29'
}
pprint.pprint(nest_dir) # observe the output... and you know what's even better than this?

# this
