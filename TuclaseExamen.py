class TuclaseExamen():
    '''
    define propiedades de clase 
    para utilizarlas en el metodo principla
    '''
    #declaracion de variables

    #declaracion de constructor
    def __init__(self):
        pass

    #declaracion de metodos de clase
    def arithmetic_arranger(self,problems, displayMode=False):
        start = True
        side_space = "    "
        line1 = line2 = line3 = line4 = ""
        # Too many Problem exception
        try:
            if len(problems) > 5:
                raise BaseException
        except:
            return "Error: Too many problems."
        for prob in problems:
            # Separacion de la lista mediante strings 
            separated_problem = prob.split()
            # storing number 1
            number1 = separated_problem[0]
            # Storing signo del operador
            operador = separated_problem[1]
            # storing number 2
            number2 = separated_problem[2]
            exp = exception_handling(number1, number2, operador)
            if exp != "":
                return exp
            no1 = int(number1)
            no2 = int(number2)
            # Espacio obtenido del maximo no. requiriente de espacios.
            space = max(len(number1), len(number2))
            # Primera funcion
            if start == True:
                line1 += number1.rjust(space + 2)
                line2 += operador + ' ' + number2.rjust(space)
                line3 += '-' * (space + 2)
                if displayMode == True:
                    if operador == '+':
                        line4 += str(no1 + no2).rjust(space + 2)
                    else:
                        line4 += str(no1 - no2).rjust(space + 2)
                start = False
            # Segunda funcion
            else:
                line1 += number1.rjust(space + 6)
                line2 += operador.rjust(5) + ' ' + number2.rjust(space)
                line3 += side_space + '-' * (space + 2)
                if displayMode == True:
                    if operador == '+':
                        line4 += side_space + str(no1 + no2).rjust(space + 2)
                    else:
                        line4 += side_space + str(no1 - no2).rjust(space + 2)
        # displayMode es cerdadero pegarle la linea 4
        if displayMode == True:
            return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
        return line1 + '\n' + line2 + '\n' + line3
        
# Exception Handling function
def exception_handling(number1, number2, operador):
    # Excepcion de solo digitos
    try:
        int(number1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."
    # Mas de 4 digitos en una cifra
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    # Excepcion del operador sonde solo puede ser + | -
    try:
        if operador != '+' and operador != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""