print("Welcome to My Quiz!")

playing = input("Do You Want To Play? ")

if playing != "yes":
    quit()
print('''Okay! Lets play (:)
There are about 9 questions''')
score = 0

# QUESTION 1
question_quiz = "1. What does CPU stand for? "
correct_answer = ("central processing unit").lower()
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')
else:
    print("Incorrect!")

# QUESTION 2
question_quiz = ("2. What does SU stand for? ")
correct_answer = ("system unit").lower()
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

# QUESTION 3
question_quiz = "3. What does PO stand for? "
correct_answer = ("peter obi").lower
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')  

else:
    print("Incorrect!")

# QUESTION 4
question_quiz = "4. What does WHO stand for? "
correct_answer = ("world health organization").lower
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

# QUESTION 5
question_quiz = "5. What does PC stand for? "
correct_answer = ("personal computer").lower
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

# QUESTION 6
question_quiz = "6. Define pie with a number? "
correct_answer = str(3.142)
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

# QUESTION 7
question_quiz = "7. What does GI stand for? "
correct_answer = ("graphic interface").lower
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

# QUESTION 8
question_quiz = "8. Complete the word, SYS? "
correct_answer = ("system").lower
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

# QUESTION 9
question_quiz = ("9. What does I/O stand for? ")
correct_answer = ("input/output").lower
answer = input(question_quiz)
if answer == correct_answer:
    score += 1
    print('Correct!')

else:
    print("Incorrect!")

print("You got " + str(score) + " Questions Correctly!!!")
print("With a " + str((score/9) * 100) + "%. ")


