# manipulating strings
# we are already familiar with \' \n \t \\ etc. but here's a new way 
print(r'C:\users\remnux\python')
# instead of \\ everytime, we will just use 'r' for specifying paths and anything contains \

# triple quotes | in triple quotes any shananigans go like:
print('''
      Hi, Anna!
        As stupid as it sound, your cat is a spy. \ a spy... sp..
      Regards,
      u/man_with_a_mullet
''')

# multiple commenting... yes... finally... I need this.
"""
I remember now, I used in while I was writing some python code for python articles. 
Wow, I forgot, because I was away from coding for two years. To be honest, time pass quick. 
"""

# each string is kinda list and you can slice it...
name = 'man_with_a_mullet'
# print(name[0,12,7,16]) # it will throw an error and we have to;
print(name[0],name[12],name[6],name[15]) # but still it's too much work, what's a workaround?
cunt = [0,12,6,15]
print(''.join([name[i] for i in cunt])) # much better

# you are already familiar with 'in' and 'not in'
'man' in name
# true

