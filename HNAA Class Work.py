name = input('What is your name? :')
loan = input('How much loan do you want? :')
time = input('When will you pay back? :')
if int(loan,0) <= 2000:
            print(f'{name}, you qualify for a loan of ghc{loan}')
            print(f'to pay back a total of {(int(loan,0)*0.2) + int(loan,0)} in {time}month')
else:
    print(f'{name}, you do not qualify for a loan')