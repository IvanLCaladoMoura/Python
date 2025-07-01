import random

while True:
    print()
    question = input("What's up for today? ")
    
    if question.lower() == 'exit':
        print("Exiting the program...")
        break
    
    random_number = random.randint(1, 12)
    #print(random_number)

    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decid"
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = "Reply hazy, try again."
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now."
    elif random_number == 7:
        answer = "My sources say no."
    elif random_number == 8:
        answer = "Yes."
    elif random_number == 9:
        answer = "Very doubtful."
    elif random_number == 10:
        answer = "Definitely no!"
    elif random_number == 11:
        answer = "Don't be such a pussy!"
    elif random_number == 12:
        answer = "I don't know."
    else:
        answer = "Error"

    print(answer)