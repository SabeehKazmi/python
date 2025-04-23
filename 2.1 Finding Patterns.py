# # let's find a phone no in a string
# data={
#     'name':'John',
#     'cell-no':'0300-0000000',
#     'cnic-no':'333-33-3333333-3'
# }
# for a,b in data.items():
#     if len(b) == 12:
#         if b[4] == '-':
#             print(f'Phone no: {b}')
#         else:
#             print('Error 404: Not Found!')
'''
For a fact we know that a phone number is 12 in length with a '-' ( a PAK phone_no)
'''
# print('Enter your phone number here: ')
# pno=input()
# if len(pno) == 12 or len(pno) == 11:
#     if pno[4] == '-':
#         print(pno)
#     else:
#         pno=pno[0]+pno[1]+pno[2]+pno[3]+'-'+pno[4]+pno[5]+pno[6]+pno[7]+pno[8]+pno[9]+pno[10]
#         print(pno)
# else:
#     print('Wrong input!')
# # this is the first version of the program i wrote, now let's refine it further

'''
Ver. 2.0
'''
# print('Enter your phone number (Note the accepted formates are;\nxxxx-xxxxxxx\n+92xxx-xxxxxxx\n+92xxxxxxxxxx\nxxxxxxxxxxx): ')
# pno = input()
# if len(pno) >10:
#     if pno[0] == '+':
#         pno = pno[3:]
#         if pno[4] == '-':
#             print(pno)
#         else:
#             pno = '0'+pno[:3]+'-'+pno[3:10]
#             print(pno)
#     else:
#         if pno[4] == '-':
#             print(pno)
#         else:
#             pno = '0'+pno[:3]+'-'+pno[3:10]
#             print(pno)
# else:
#     print('Please try again!')
# # it still contains logical errors and not refined. 

'''
Ver. 3.0 (final-release)
'''
'''
Logic
> check length
> check +92 or other
> if +92 check length again
> check all digits or pno[6] is '-'
> if pno6 is '-'
> correct and print
> if 03 check length again
> check all digita or pno[4] is '-'
> if pno4 is '-'
> correct and print
'''
print('Enter:')
pno=input()
if len(pno) > 9:
    if pno[0:3] == '+92':
        if len(pno) == 12 or len(pno) == 13 or len(pno) == 14:
            if pno[1:11].isdigit():
                pno = '0'+pno[3:6]+'-'+pno[6:]
                print(pno)
            elif pno[6] == '-':
                print(pno)
            else:
                print('Error 401!')
        else:
            print('Error 402!')
    elif pno[0:2] == '03':
        if len(pno) == 10 or len(pno) == 11:
            if pno.isdigit():
                pno = pno[:4]+'-'+pno[4:]
                print(pno)
            elif pno[3] == '-':
                print(pno)
            else:
                print('Error 403!')
        else:
            print(pno)
    else:
        print('Error 404!')
else:
    print('Error 405\nNot Found!')

