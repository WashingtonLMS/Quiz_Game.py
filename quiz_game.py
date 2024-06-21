print('Welcome to my computer quiz!')

playing = input('do you want to play? ').upper()

if playing != 'YES':
    quit()

print("Okay! Let's play: ")
score = 0

answer = input('What does CPU stand for? ').upper()
if answer == 'CENTRAL PROCESSING UNIT':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does GPU stand for? ').upper()
if answer == 'GRAPHICS PROCESSING UNIT':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does RAM stand for? ').upper()
if answer == 'RANDOM ACESS MEMORY':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does PSU stand for ? ').upper()
if answer == 'POWER SUPPLY':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {(score/4)*100}% questions correct!')

