p = 1
while p < 8:
    print ("{} + {} = {}".format(p, p, (p+p)))
    p += 1

a = 1
while a < 8:
    print ("%d + %d = %d" % (a, a, (a*a)))
    a += 1

p = 1
o = 1
while p < 15 and o < 15:
    print("%i / %i = %i" % (p, o, (p/o)))
    p+=1
    o+=1

lang  = ["Python", "Java", "JavaScript", "R", "VBA", "C#", "C++", "Julia","HTML", "CSS", "C", "Go"] 
x = 0
while x < len(lang):
    print(lang[x])
    x += 2
#declarar os itens de uma lista pulando de 2 em 2

a = 1
b = 1
while a < 5:
    while b < 5:
        print: print ("{} + {} = {}".format(a, b, (a+b)))
        a+= 1
        b+= 1