class Cards:
	"""
	Function and methods about cards
	"""

	matrix = [["Aces", [1, 11], "A"],
			  ["Two", 2, "2"],
			  ["Three", 3, "3"],
			  ["Four", 4, "4"],
			  ["Five", 5, "5"],
			  ["Six", 6, "6"],
			  ["Seven", 7, "7"],
			  ["Eight", 8, "8"],
			  ["Nine", 9, "9"],
			  ["Ten", 10, "10"],
			  ["Valet", 10, "J"],
			  ["Queen", 10, "Q"],
			  ["King", 10, "K"]]

	@staticmethod
	def show_card(card):
		"""
		to print a card representation
		:return a card representation
		"""
		result = []

		for x in card:

			if x[0] == "Ten":
				result.append(["- - - -", "|     |", f"| {x[2]}  |", "|     |", "- - - -"])
			else:
				result.append(["- - - -", "|     |", f"|  {x[2]}  |", "|     |", "- - - -"])

		return result
