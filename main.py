import os
import random

def loadInfo():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs')
    
    questions_f = []
    choices = []
    answers = []
    numOfChoice = []
    numOfAnswer = []
    
    with open(path + "\\NumOfCandA.txt") as file:
        toggle = True
        for line in file:
            if toggle:
                numOfChoice.append(int(line))
            else:
                numOfAnswer.append(int(line))
            toggle = not toggle
    with open(path + "\\Questions.txt") as file:
        for line in file:
            questions_f.append(line)
    with open(path + "\\Choices.txt") as file:
        for line in file:
            choices.append(line)
    with open(path + "\\Answers.txt") as file:
        for line in file:
            answers.append(int(line))
            
    choices_g = []
    choices_f = []
    i = 0
    for choice in choices:
        choices_g.append(choice)
        
        if (len(choices_g) == numOfChoice[i]):
            choices_f.append(choices_g)
            choices_g = []
            i += 1
    
    answers_g = []
    answers_f = []
    i = 0
    for answer in answers:
        answers_g.append(answer)
        
        if (len(answers_g) == numOfAnswer[i]):
            answers_f.append(answers_g)
            answers_g = []
            i += 1
    return questions_f, choices_f, answers_f

def generateQuestion(questions, choices, answers, randomQ, preIndex):
    if randomQ:
        index = random.randint(0, len(questions) - 1)
        
    else:
        index = preIndex + 1
        if index == len(questions):
            index = 0
    
    answers_c = ""
    for answer in answers[index]:
        answers_c += str(answer)
    
    return questions[index], choices[index], int(answers_c), index
    
def printMenu():
    print("=================== Menu ===================")
    print("|                                          |")
    print("|                                          |")
    print("|         Enter 1: Generate a Quiz         |")
    print("|                                          |")    
    print("|              Enter 0: Quit               |")
    print("|                                          |")
    print("|                                          |")    
    print("============================================")

def printQuizMenu():
    print("================ Quiz  Menu ================")
    print("|                                          |")
    print("|                  Enter 1:                |")
    print("|   Generate Quiz Questions Sequentially   |")    
    print("|                                          |")    
    print("|                  Enter 2:                |")
    print("|     Generate Quiz Questions Randomly     |")
    print("|                                          |")    
    print("============================================")

def printQuizQuestion(question, choice, index):
    print("\nQuestion " + str(index) + ": ")
    print(question.strip())
    
    i = 1
    for line in choice:
        print(str(i) + ". " + line.strip())
        i += 1
        
def printQuizResult(answer, userInput):
    if userInput == answer:
        print("You are correct! \n")
    else: 
        print("You are wrong! The correct answer should be: " + str(answer))
    print("\n press Enter to continue... ")

def main(): 
    questions, choices, answers = loadInfo()
    
    while True:
        printMenu()
        userInput = int(input(""))
        #userInput = 1
        
        if userInput == 0:
            break
        elif userInput == 1:
            printQuizMenu()
            userInput = int(input(""))
            #userInput = 2
            
            if userInput == 2:
                randomQ = True
            else:
                randomQ = False
            
            index = 0
            while True:
                question, choice, answer, index = generateQuestion(questions, choices, answers, randomQ, index)
                
                printQuizQuestion(question, choice, (index + 1))
                
                userInput = int(input("Your answer is: (e.g., 123) \n(Enter 0 to quit)"))
                if userInput == 0:
                    break
                
                printQuizResult(answer, userInput)
                
                userInput = input("")
                
if __name__ == '__main__':
    main()