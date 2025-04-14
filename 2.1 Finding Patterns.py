# let's find a phone no in a string
data={
    'name':'John',
    'cell-no':'0300-0000000',
    'cnic-no':'333-33-3333333-3'
}
for a,b in data.items():
    if len(b) == 12:
        if b[4] == '-':
            print(f'Phone no: {b}')
        else:
            print('Error 404: Not Found!')
'''
For a fact we know that a phone number is 12 in length with a '-' ( a PAK phone_no)
'''

