print('Welcome to The Bank!')
balance = 0

while True:
  print("\nHere are the possible operations:")
  print("1 - deposit money")
  print("2 - withdraw money")
  print("3 - check balance")
  print("4 - exit")

  try:
    option = int(input("\nWhat would you like to do?\nEnter the operation number please: "))
    print()
    if option == 4:
      print('You have chosen to finish. Goodbye!')
      break
    elif option < 1 or option > 4:
      print('\nInvalid number! Please enter a number between 1 and 4, based on the operations provided!')
      continue
    elif option == 1:
      print('You have selected to deposit money!')
      try:
        deposit = int(input('Please write the amount of deposit: '))
        print(f'You have added {deposit}EUR to the balance.\nIs there anything else you want to do today?')
        balance += deposit
      except:
        print('Invalid character! Please use whole numbers to write the deposit amount!')
        continue
    elif option == 2:
      print('You have selected to withdraw money!')
      try:
        withdrawal = int(input('Please write the amount to withdraw: '))
        if balance >= withdrawal:
          print(f'You have withdrawn {withdrawal}EUR from the bank account.\nIs there anything else you want to do today?')
          balance -= withdrawal
        else:
          print(f'Insufficient funds! You have {balance}EUR in the account.')
          continue  
      except:
        print('Invalid character! Please use whole numbers to write the withdrawal amount!')
        continue
    elif option == 3:
      print('You have selected to check balance!')
      print(f'You have {balance}EUR in the bank account.\nIs there anything else you want to do today?')
      continue
  except:
    print('\nInvalid character! Please enter a number between 1 and 4, based on the operations provided!') 
    continue 

  
