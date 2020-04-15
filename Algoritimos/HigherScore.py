# pedir para o usuario inserir quantos alunos a sala possui, o nome e a nota de cada um deles e indicar
# quem teve o melhor aproveitamento
students = int(input("How many students does the class have? "))
highScore = 0
studentHighScore = ""
countLoop = 0
while (countLoop < students):
    nameStu = str(input("What is the student's name? "))
    gradeStu = float(input("What was the student's grade? "))
    countLoop = countLoop + 1
    if(gradeStu >= highScore):
        studentHighScore = nameStu 
        highScore = gradeStu
print(studentHighScore, "got the higher score, which was", highScore)