class BankAccount(object):
  balance = 0
#To add a name to the acct. This will ensure that whatever name is typed when creating a class is atributed to that object.  
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)

#To print the acct balance
  def show_balance(self):
    print ("Balance: $%.2f" % self.balance)
    return 

#Deposit functionality that show balance with two decimals.
  def deposit(self, amount):
    if amount <= 0:
      print ("You entered wrong amount")
      return
    else:
      print ("Deposited amount: $%.2f" % amount)
      self.balance  += amount 
      self.show_balance()

#Withdraw functionality that show balance with two decimals.
  def withdraw(self, amount):
    if amount > self.balance:
      print ("No enough balance in your acct for this withdraw")
      return 
    else:
      print  ("Withdraw amount: $%.2f" %   amount)
      self.balance -= amount
      self.show_balance()
      

my_account = BankAccount("Angela")
print (my_account)

my_account.show_balance()
my_account.deposit(200)
my_account.withdraw(180)

print (my_account)
