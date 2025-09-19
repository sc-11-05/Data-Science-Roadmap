def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    ans = []

    for prob in problems:
        parts = prob.split()
    
        num1, operator, num2 = parts
        
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit()  or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 2

        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width-1))
        dashes.append('-'*width)

        if show_answers:
            if operator == "+":
                result = str(int(num1) + int(num2))
            if operator == "-":
                result = str(int(num1) - int(num2))
            ans.append(result.rjust(width))

    answer_problems = (
        '    '.join(first_line)  + '\n' + 
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    if show_answers:
        answer_problems += '\n' + '    '.join(ans)

    return answer_problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')


