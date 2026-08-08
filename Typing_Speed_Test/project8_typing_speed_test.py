import time

sentence = "python is a powerful programming language."

print("===== Typing Speed Test =====")
print("\nType this sentence:")
print(sentence)

input("\nPress Enter to Start...")

start_time = time.time()

typed_text = input("\nStart Typing: ")

end_time = time. time()

time_taken = end_time - start_time

print("\nTime Taken:",
round(time_taken, 2), "seconds")

if typed_text ==sentence:
    print("Accuracy: 100%")
else:
    print("Accuracy: Incorrect")

word_count = len(typed_text.split())
wpm = (word_count/ time_taken) * 60

print("Words Typed:", word_count)
print("Typing Speed:", round(wpm, 2),"WPM")

if wpm >= 40:
    print("Excellent Typing Speed!")
elif wpm >= 25:
    print("Good Typing Speed!")
else:
    print("Keep Practicing!")
