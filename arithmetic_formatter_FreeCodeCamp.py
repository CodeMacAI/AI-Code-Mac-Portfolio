def arithmetic_arranger(problems, show_answers=False):
    # Check if too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_lines = [[], [], [], []]  # [top, bottom, dashes, answers]
    for problem in problems:
        # Split problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if numbers contain only digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check max four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width based on longest number
        width = max(len(num1), len(num2)) + 2
        line1 = num1.rjust(width)
        line2 = operator + " " + num2.rjust(width - 2)
        line3 = "-" * width

        # Calculate answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:  # operator == '-'
                answer = str(int(num1) - int(num2))
            line4 = answer.rjust(width)
        else:
            line4 = ""

        # Append to respective lines
        arranged_lines[0].append(line1)
        arranged_lines[1].append(line2)
        arranged_lines[2].append(line3)
        arranged_lines[3].append(line4)

    # Join lines for each problem set
    result = []
    for i in range(3 + show_answers):  # 3 lines without answer, 4 with answer
        line = "    ".join(arranged_lines[i])
        if line:
            result.append(line)
    return "\n".join(result).rstrip()

# Test print (remove or adjust for submission)
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')