# Deixar que o usuario informe as duas notas do aluno, dizer a media dele e se ele esta APROVADO, 
# DE RECUPERACAO OU REPROVADO
num1 = float(input("What was the student's first grade? "))
num2 = float(input("What was the student's second grade? "))

media = ((num1 + num2) / 2)
print("The student's media was " + str (media))

if( media <= 1000 ) and ( media >= 900 ):
    print("The student scored A: APPROVED")
elif( media <= 899 ) and ( media >= 800 ):
    print("The student scored B: APPROVED")
elif( media <= 799) and ( media >= 700 ):
    print("The student scored C: APPROVED")
elif( media <= 699 ) and ( media >= 600 ):
    print("The student scored D: RECOVERY")
elif( media <= 599 ) and ( media >= 500 ):
    print("The student scored E: RECOVERY")
elif( media <= 499 ):
    print("The student scored F: FAILED") 
else:
    print("This score is invalid")
      