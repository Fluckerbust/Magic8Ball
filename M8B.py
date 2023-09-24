import random

question = "am i doing this right?"
name = input("Enter name:")
answer = ""
random_number = random.randint(1, 15)

print(random_number)



if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
 answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "uhhh what is this and where am I?"
elif random_number == 11:
  answer = "umm... yes?"
elif random_number == 12:
  answer = "idk why are you asking me, I'm just a ball"
elif random_number == 13:
  answer = "probably not dude"
elif random_number == 14:
  answer = "Bro really?"
elif random_number == 15:
  answer = "nah, that questions messed up!"
else:
  answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("you gotta ask something first")
else:
  print("Magic 8-Ball's answer: " + answer)