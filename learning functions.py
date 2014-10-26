def l(prompt):
	typed = input(prompt)
	num = int(typed)
	return num
a = l('Enter a number')
b = l('Enter another number')
print('your first number times your other number =', a * b)
