def calc_total_price(apple_weight, APPLE_PRICE):
	pass

def calc_return(total_price, money_given):
	pass

def main():
	APPLE_PRICE = 21 # k VND
	apple_weight = input("Enter weight of apples: ")
	money_given = input("Total money customer give you: ")

	total_price = calc_total_price(apple_weight, APPLE_PRICE)
	money_return = calc_return(total_price, money_given)

main()