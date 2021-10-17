class Category:
  def __init__(self, cat):
    self.ledger = []
    self.cat = cat
  
  def __str__(self):
    lines = []

    # Title Line
    num_stars = 30 - len(self.cat)
    if num_stars % 2 == 0:
      lines.append("*" * int(num_stars / 2) + self.cat + "*" * int(num_stars / 2) + "\n")
    else:
      lines.append("*" * int((num_stars // 2) + 1) + self.cat + "*" * int(num_stars // 2) + "\n")

    # Items in Ledger
    for item in self.ledger:
      desc = item["description"][:23]
      am = "{:0.2f}".format(item["amount"])
      spaces = int(30 - len(desc) - len(am))
      lines.append(desc + " "*spaces + am + "\n")
    
    # Total
    total = self.get_balance()
    lines.append("Total: " + str("{:0.2f}".format(total)))

    return "".join(lines)

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, cat2):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + cat2.cat)
      cat2.deposit(amount, "Transfer from " + self.cat)
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

def create_spend_chart(categories):
  # Get percentages
  percs = []
  for item in categories:
    withdrawals = [a["amount"] for a in item.ledger if a["amount"] < 0]
    percs.append(abs(sum(withdrawals)))
  percs = [((b / sum(percs))*100 // 10) * 10 for b in percs if sum(percs) > 0]

  # Graph
  lines = ["Percentage spent by category"]

  # Chart y-axis and data points
  for i in range(100, -10, -10):
    # y-axis
    y = (3 - len(str(i))) * " " + str(i) + "|"
    # data points
    data = ""
    for perc in percs:
      if perc >= i:
        data += " o "
      else:
        data += "   "
    lines.append(y + data + " ")
  # Dotted x-axis
  lines.append("    " + (3*len(categories)+1) * "-")
  # Category Labels
  maxlen = max([len(cat.cat) for cat in categories])
  for j in range(maxlen):
    line = ""
    for c in categories:
      if j >= len(c.cat):
        line += "   "
      else:
        line += " " + c.cat[j] + " "
    lines.append("    " + line + " ")
  return "\n".join(lines)