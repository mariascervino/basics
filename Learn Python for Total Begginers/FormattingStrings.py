name = "Anisha"
grade = "A+"
print("The student's name is {} and the grade is {}".format(name, grade))

#  a palavra reservada .format serve para inserir quais parâmetros deverão ser inseridos nas chaves.

animals = ["lions", "zebras", "monkeys"]
safari = "I saw {}, {} and {}!"

print (safari.format(animals[0], animals[1].capitalize(), animals[2].upper()))
# or just
print (safari.format(*animals))

# as palavras reservadas .capitalize() e .upper() servem para mudar o jeito como as palavras sao escritas.

num = "200"
print (eval(num) + 10)

# The eval() method parses the expression passed to this method and runs python expression (code)
# within the program

num2 = [10, 20, 30]
print(eval("{} + {} + {}".format(*num2)))

num3 = [2, 5, 10, 20]
print(eval("{} + {} + {} + {}".format(*num3)))
print(eval("{2} + {2} + {3} + {3}".format(*num3)))

# It is possible to print how many values in the list you want, just indicanting what they are.
# In the example I printed the values 10 (number 2 in the list) and 20 (number 3 in the list twice).

print("%d * %d = %d" % (3, 5, (10/2)))
print("%d * %d = %f" % (3, 5, (5/3)))
print("%d * %d = %.2f" % (3, 5, (5/3)))
# eu posso arredondar meu float number para ele ficar mais enxuto, apenas indicando quantas casas
# depois da virgula eu quero (%.2f = duas casas depois da virgula)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

word = "awesome"
print("The length of the word {} is {}".format(word, len(word)))
print("The word {} in uppercase it's readen {}".format(word, word.upper()))

p1 = "Python"
p2 = "older"
print(f"""This is a docstring that uses {p1} 3.6 and can't be used for {p2} versions of {p1}""")
