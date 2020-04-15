toys = {"robot": "40", "car":"25", "iroman": "12"}
print(toys.values())
print(eval("{} + {} + {}".format(*toys.values())))