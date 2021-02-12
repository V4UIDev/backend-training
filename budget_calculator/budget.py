class Category:
   

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.00
        self.spent = 0.00

    def deposit(self, amount, description=""):
        moneyMove = {}
        self.balance = (self.balance + float(amount))
        moneyMove.update({"amount": amount})
        moneyMove.update({"description": description})
        self.ledger.append(moneyMove)

    def withdraw(self, amount, description=""):
        if self.balance >= float(amount):
            moneyMove = {}
            self.balance = (self.balance - float(amount))
            self.spent = (self.spent + float(amount))
            amount = ("-" + str(amount))
            amount = float(amount)
            moneyMove.update({"amount": amount})
            moneyMove.update({"description": description})
            self.ledger.append(moneyMove)
            return True
        else: return False

    def transfer(self, amount, destination):
        if self.balance >= float(amount):
            moneyMove = {}
            self.balance = (self.balance - float(amount))
            self.spent = (self.spent + float(amount))
            moneyMove.update({"amount": float("-" + str(amount))})
            moneyMove.update({"description": "Transfer to " + destination.name})
            self.ledger.append(moneyMove)
            moneyMoveDest = {}
            destination.balance = (destination.balance + float(amount))
            moneyMoveDest.update({"amount": int(amount)})
            moneyMoveDest.update({"description": "Transfer from " + self.name})
            destination.ledger.append(moneyMoveDest)
            return True
        else: return False


    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else: return False

    def __str__(self):
        n = 0
        statement = ""
        titleLine = ('{:*^30}'.format(self.name)) + "\n"
        statement = statement + titleLine
        for transfer in self.ledger:
            cutDescription = self.ledger[n].get("description")[:23]
            amount = self.ledger[n].get("amount")
            amount = '{:.2f}'.format(amount)
            transferLine = ('{:<23}'.format(cutDescription)) + ('{:>7}'.format(amount)) + "\n"
            statement = statement + transferLine
            n = n + 1
        statement = statement + "Total: " + str(self.balance)
        return statement







def create_spend_chart(categories):
    n = 0
    total = 0.00
    graph = "Percentage spent by category\n"
    for object in categories:
        total = total + categories[n].spent
        n = n + 1
    n = 0
    categoryGraphValue = []
    for object in categories:
        graphNumber = (categories[n].spent / total) * 100
        graphNumber = int(graphNumber / 10)
        categoryGraphValue.append(graphNumber)
        n = n + 1

    if len(categoryGraphValue) == 1:
        categoryGraphBars = " {0}"
    elif len(categoryGraphValue) == 2:
        categoryGraphBars = " {0}  {1}"
    elif len(categoryGraphValue) == 3:
        categoryGraphBars = " {0}  {1}  {2}"
    elif len(categoryGraphValue) == 4:
        categoryGraphBars = " {0}  {1}  {2}  {3}"
    counter = 10
    while counter > 0:
        graphBars = [" ", " ", " ", " "]
        n = 0
        for value in categoryGraphValue:
            if value >= counter:
                graphBars[n] = "o"
                n = n + 1
            else: n = n + 1
        graph = graph + ('{:>4}'.format(str(counter) + "0|")) + categoryGraphBars.format(*graphBars) + "  \n"
        counter = counter - 1
    while counter > -1:
        graphBars = [" ", " ", " ", " "]
        n = 0
        for value in categoryGraphValue:
            if value >= counter:
                graphBars[n] = "o"
                n = n + 1
            else: n = n + 1
        graph = graph + ('{:>4}'.format(str(counter) + "|")) + categoryGraphBars.format(*graphBars) + "  \n"
        counter = counter - 1
    if len(categoryGraphValue) == 1:
        graph = graph + "    ---\n"
    elif len(categoryGraphValue) == 2:
        graph = graph + "    ------\n"
    elif len(categoryGraphValue) == 3:
        graph = graph + "    ----------\n"
    elif len(categoryGraphValue) == 4:
        graph = graph + "    ------------\n"
    catNameVal = 0
    for name in categories:
        if len(name.name) > catNameVal:
            catNameVal = len(name.name)
    n = 0
    if len(categoryGraphValue) == 1:
        catNameBars = "{0}"
    elif len(categoryGraphValue) == 2:
        catNameBars = "{0}  {1}"
    elif len(categoryGraphValue) == 3:
        catNameBars = "{0}  {1}  {2}"
    elif len(categoryGraphValue) == 4:
        catNameBars = "{0}  {1}  {2}  {3}"
    while n < catNameVal - 1:
        nameBars = [" ", " ", " ", " "]
        j = 0
        for name in categories:
            try:
                if name.name[n] != None:
                    nameBars[j] = name.name[n]
                    j = j + 1
            except:
                j = j + 1
        graph = graph + ("     " + (catNameBars).format(*nameBars) + "  \n")
        n = n + 1
    while n == catNameVal - 1:
        nameBars = [" ", " ", " ", " "]
        j = 0
        for name in categories:
            try:
                if name.name[n] != None:
                    nameBars[j] = name.name[n]
                    j = j + 1
            except:
                j = j + 1
        graph = graph + ("     " + (catNameBars).format(*nameBars) + "  ")
        n = n + 1
    
    return graph