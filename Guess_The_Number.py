from random import randint
x = randint(1, 9)
print('''
      GUESS WHAT NUMBER BETWEEN 1-9
      IF you cant guess in three turns
      YOUR OUT!!
      If you like to quit, type 'quit'
      '''
      )
found_answer = False
count = 0
while found_answer == False:
    y = ''
    y = input('YOUR GUESS: ')    
    if y == 'quit':
        print('You have quit the game')
        found_answer = True        
    elif int(y[0]) == x:
        found_answer = True
        print('''CONGRATS YOU FOUND IT!!!''')
    else:
        count += 1
        total = 3 - count
        total = str(total)
        if count == 3:
            print('YOU LOSE')
            x = str(x)
            print('The number was ' + x)
            found_answer = True
        else:
            print('You have ' + total + ' turn(s) left')