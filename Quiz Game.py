print('Hello')
print("Welcome to my football quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != 'yes':
    quit()

print("Okay Let's Play!:)")

answer = input("Who is considered to be the greatest QB ever? ")
if answer.lower() == 'tom brady':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer = input("Who is the starting RB for the New York Jets? ")
if answer.lower() == 'breece hall':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer = input("How many receiving yards did Justin Jefferson have for the 2023 season? ")
if answer == '1809':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer = input("What is the QB for the Kansas City Chiefs? ")
if answer == 'patrick mahomes':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer = input("Which team in the AFC east finished their season on a 6 game losing streak? ")
if answer.lower() == 'new york jets':
    print('Correct!')
    score += 1
else:
    print('Wrong')

print("You got " + str(score) + " questions correct!")
