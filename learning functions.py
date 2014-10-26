def l(prompt):
	typed = input(prompt)
	num = int(typed)
	return num
a = l('Enter a number')
b = l('Enter another number that you want so it is to the power of your first number')
print('your number cubed =', a ** b)
ans = a ** b


def count_digit(d, num):
    sum = 0
    for i in str(num):
        if i == d:
            sum = sum + 1
    return sum


for j in range(0, 10):
    count = count_digit(str(j), ans)
    print('The number of ',j, ' in that number are:', count)




def digits(num):
    text = str(num)
    return len(text)

print('The number of digits are', digits(ans))

def even(num):
    return (num % 2 == 0)

evens = 0
odds = 0
for k in range(0, 10):
    count = count_digit(str(k), ans)
    if even(k):
        evens = evens + count
    else:
        odds = odds + count

print('There are ', evens, ' even and ', odds, ' odd numbers in the number you asked for!')
    
#sevens = count_digit('7', a ** b)
#eights = count_digit('8', a ** b)


#print('Test should be 3, is = ', test)

#print('The number of sevens in that number are:', sevens)
#print('The number of eights in that number are:', eights)
      
        
