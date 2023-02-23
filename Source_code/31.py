def calc_total_price(apple_weight, APPLE_PRICE):
	return apple_weight * APPLE_PRICE

def calc_return(total_price, money_given):
	if money_given < total_price:
		return -1
	
	return money_given - total_price

def print_return_info(total):
	# 500 200 100 50 20 10 1
	pass

def main():
	APPLE_PRICE = 21 # k VND
	apple_weight = input("Enter weight of apples: ")
	money_given = input("Total money customer give you: ")

	apple_weight = float(apple_weight)
	money_given = float(money_given)

	total_price = calc_total_price(apple_weight, APPLE_PRICE)
	money_return = calc_return(total_price, money_given)
	
	if money_return == -1:
		print("Not enough cash")
	else:
		print("You need to return to customer: " + str(money_return))

main()