score = 0

print("=====Python Quiz Game =====")
print()

print("Q1.Who developed python?")
print("a. James Gosling")
print("b.Guido van Rossum")
print("c.DENNIS Ritchie")

answer = input("Enter your answer (a/b/c):")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your Score:", score)


print()

print("Q2.Which keyword is used to create a function in Python?")
print("a. function")
print("b.def")
print("c.fun")

answer = input("Enter your answer(a/b/c):")

if answer.lower() == "b":
    print("Correct!")
    score += 1

else:
    print("Wrong!")


    print()
    print("Final Score:", score, "/2")

    print()
    
    print("Q3.Which symbol is used for comments in Python?")
    print("a. //")
    print("b.#")
    print("c. /*")

    answer = input("Enter your answer(a/b/c): ")

    if answer.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")



print()
print("Final Score:", score, "/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good Job!")
elif score == 1:
    print("Keep Learning!")
else:
    print("Practice More!")
    
