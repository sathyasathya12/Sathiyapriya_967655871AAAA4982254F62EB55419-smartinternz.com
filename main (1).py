class BankAccount:
  def

__init_(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.__account balance += amount
      #self__account_balance=self__account_balance+amount
     print("Deposited${}.New balance:${}".format(amount,self.__account_balance))
   else:
       print("Invalid deposit amount")
  def withdraw(self,amount):
     if amount>0 and amount <=
  self.__account_balance:
      self,_account_balance-=amount
      #self._account_balance = self._account_balance-amount
       print("withdraw${}.New balance:${}".format(amount,self.__account_balance)
     else:
         print("Invalid withdraw amount or insufficient balance.")
  def display_balance(self):
      print("Account balance for {} (Account#{}):$".format(self._account_holder_name,self._account_number,self.__account-balance))
    #create an instance of the BankAccount class
account =
BankAccount(account_number="123456789",account_holder_name="sathya",initial_balance=5000.0)
    #Test deposit and withdraw funtionality
account.display_balance()
account.deposit(100)
account.withdraw(200.0)
account.display_balance()
