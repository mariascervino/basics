prices = ["a", "b", "9", "c", "d", "FOUR", "e", "f", "2.5"]
print(prices[2::3])

sentence = """The bill for the {}, {} and drink came to {}"""
listSentence = ["pizza", "chips", "$15.50"]
print(sentence.format(*listSentence))