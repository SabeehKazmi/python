# dictonary 
_sample = {'cats':'fezi','dogs':'tom'}
# print(_sample['cats'])

# a complex dictonary
degree = {
    'title':'software engineering',
    'specialization':'cybersecurity',
    'programming subjects':['c#', 'Python','SQL'],
    'cgpa':'3.29'
}
#print(degree['programming subjects'])

#nested directories
nest_dir = {
    'classes':['programming','database','networking','security'],
    'security':{
        'subjects':['database sec','network sec','DevSecOp'],
        'ranking':'3.29'
    }
}
# print(nest_dir['security']['subjects']) # to print subjects within security

# # to print subjects one by one or processing them:
# for a in nest_dir['security']['subjects']:
#     if a == 'database sec':
#         print('You studied database, wow!')

# # values(), keys(), and items() methods in directory
# # values() only print values
# for a in nest_dir.values():
#     print(a)
# # keys() only print keys
# for a in nest_dir.keys():
#     print(a)
# # items() all items with keys and values
# for a in nest_dir.items():
#     print(a)
# print(list(nest_dir.items())) # prints a true list | takes the values from the dir pass it to a lsit and print the list

# to assign keys and values seprately
for a, b in nest_dir.items():
    print('Key: ' + a + ' Values: ' + str(b))
print('\n' * 5)
    # but here's an issue if there's a nested dir, its keys will also be printed as values
    # henace we do the following to prevent this
for key, val in nest_dir.items():
    print('Key: ' + key)
    # we use isinstance()
    if isinstance(val, dict):
        for sub_key, sub_val in val.items():
            print('Sub_Key: ' + sub_key + '\t Sub_Value: ' + str(sub_val))
    else:
        print(' Value: ' + str(val))
print('\n' * 5)

# checking if a key or value exists in a dir
# first way to do so via get() method
if 'programming' in nest_dir.get('classes', []): #check for values in a known key, only if we know the key
    print('found!')
# second way to do so | if we don't even the key in which the value resides
for a, b in nest_dir.items():
    if isinstance(b, list) and 'programming' in b:
        print('found in ' + a)
    elif isinstance(b, dict):
        for c, d in b.items():
            if isinstance(d, list) and 'programming' in d:
                print('found in ' + c)
print('\n' * 5)

# the setdefault() method to add values
# the general way to do so
if 'student' in nest_dir.keys():
    print('already exist!')
else:
    nest_dir['student'] = 'hassan'
    print(nest_dir)
# thorugh setdefault() method
nest_dir.setdefault('student','hassan')

# however, to override a value:
nest_dir.setdefault('student','ali') # it doesn't override and still returns 'hassan'
nest_dir['student'] = 'ali'
print('\n' * 5)
print(nest_dir)