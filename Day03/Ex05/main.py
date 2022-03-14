# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combo_str = (name1 + name2)
combo_str = combo_str.lower()

t = combo_str.count("t")
r = combo_str.count("r")
u = combo_str.count("u")
e = combo_str.count("e")

true = t + r + u + e

l = combo_str.count("l")
o = combo_str.count("o")
v = combo_str.count("v")
e = combo_str.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score = int(love_score)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")