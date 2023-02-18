def arithmetic_arranger(problems, solve=False):

  if (len(problems) > 5):
    return "Error: Too many problems."

  first = ""
  second = ""
  lines = ""
  sumf = ""
  string = ""

  for p in problems:
    firstNum = p.split(" ")[0]
    operator = p.split(" ")[1]
    secondNum = p.split(" ")[2]

    if (not firstNum.isnumeric() or not secondNum.isnumeric()):
      return "Error: Numbers must only contain digits."

    if len(firstNum) > 4 or len(secondNum) > 4:
      return "Error: Numbers cannot be more than four digits."

    if (operator == "/" or operator == "*"):
      return "Error: Operator must be '+' or '-'."

    sum = ""

    if operator == "+":
      sum = str(int(firstNum) + int(secondNum))

    elif operator == "-":
      sum = str(int(firstNum) - int(secondNum))

    length = max(len(firstNum), len(secondNum)) + 2

    top = str(firstNum).rjust(length)
    bottom = str(operator) + str(secondNum).rjust(length - 1)
    line = ""
    ans = str(sum).rjust(length)

    for l in range(length):
      line += "-"

    if p != problems[-1]:
      first += top + " " * 4
      second += bottom + " " * 4
      lines += line + " " * 4
      sumf += ans + " " * 4

    else:
      first += top
      second += bottom
      lines += line
      sumf += ans

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumf
  else:
    string = first + "\n" + second + "\n" + lines

  return string
