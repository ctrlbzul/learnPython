class MenuItem:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def detail(self):
		return f"{self.name:<14}" + " : $" + f"{str(self.price):>2}"

	def total_price(self, count):
		total_price = self.price * count

		# get 10% discount if count is more or equal 3
		if count >= 3:
			total_price *= 0.9
		# round total_price to the nearest whole number and return it
		return round(total_price)