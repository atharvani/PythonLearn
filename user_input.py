#program to accept Use input

user_nm = input('Enter your name: ')
print('Welcome', user_nm +'!')


#calculate pay

hrs = input('Enter number of hours : ')
rate = input('Enter hourly rate : ')
pay = float(hrs) *  float(rate)
print('Your pay is :', '$' + str(pay))


#using operators

width = 17
height = 12.0
expression1 = width//2 # int part of the answer is returned
expression2 = width/2.0
expression3 = height/3
expression4  = 1 + 2 * 5

print('width//2', expression1)
print('width/2.0', expression2)
print('height/3', expression3)
print('1+2*5', expression4)


# temperature conversion

c_temp = input('Enter the temperature in Celcius : ')
f_temp = 1.8 * float(c_temp) + 32
print ('The temperature is : ', f_temp,'F')
