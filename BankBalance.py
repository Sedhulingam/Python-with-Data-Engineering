class Bank:
 
  def __init__(self , name,actno , bal=500.0):
      self.name=name
      self.actno=actno
      self.balance=bal
 
 
  def getBalance(self):
      print("\nName    = ",self.name)
      print("Actno   = ",self.actno)
      print("Balance = ",self.balance)
 
  def deposit(self,dep):
      self.balance=self.balance+dep
 
  def withdrawl(self, withdraw):
      if self.balance > withdraw:
         self.balance=self.balance-withdraw
      else:
         print("Insufficient funds")
 
 
b1=Bank('Sedhulingam', 12345678, 10000)
b1.getBalance()
b1.deposit(2000)
b1.getBalance()
b1.withdrawl(500)
b1.getBalance()