def arithmetic_arranger(problems,returnAll=False):
  numProbs = len(problems)
  probDict = {"top":[],"op":[],"bot":[],"width":[]}
  arranged_problems = None

  # Test for number of problems
  if numProbs > 5:
    arranged_problems = "Error: Too many problems."
  else:
    for i in range(numProbs):
      tmp = problems[i].split()
      probDict["top"].append(tmp[0])
      probDict["op"].append(tmp[1])
      probDict["bot"].append(tmp[2])
      probDict["width"].append(max(len(tmp[0]),len(tmp[2]))+2)
    
    # Test for correct operators
    if all([c == '+' or c == '-' for c in probDict["op"]]) == False:
      arranged_problems = "Error: Operator must be '+' or '-'."

    # Test for only digits
    elif all([b.isdigit() for b in probDict["top"]]) == False or \
      all([a.isdigit() for a  in probDict["bot"]]) == False:
      arranged_problems = "Error: Numbers must only contain digits."

    # Test for max number of digits
    elif any(len(num) > 4 for num in probDict["top"]) or \
      any(len(numb) > 4 for numb in probDict["bot"]):
      arranged_problems = "Error: Numbers cannot be more than four digits."

    # Format the problems
    else:
      top = ''
      bot = ''
      dash = ''
      ans = ''
      for j in range(numProbs):
        top += str(' ' * (probDict["width"][j]-len(probDict["top"][j]))) + probDict["top"][j] + '    '
        bot += probDict["op"][j] + str(' ' * (probDict["width"][j]-len(probDict["bot"][j])-1)) \
          + probDict["bot"][j] + '    '
        dash += str('-' * probDict["width"][j]) + '    '
        tmpAns = str(eval(problems[j]))
        ans += str(' ' * (probDict["width"][j]-len(tmpAns))) + tmpAns + '    '
      if returnAll:
        arranged_problems = top.rstrip() + '\n' + bot.rstrip() + '\n' + dash.rstrip() + '\n' + ans.rstrip()
      else:
        arranged_problems = str(top.rstrip() + '\n' + bot.rstrip() + '\n' + dash.rstrip())
  return arranged_problems