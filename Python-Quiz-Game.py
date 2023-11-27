print("Welcome to Jeeto Pakistan")
print()
print("Answer the questions & win grand prize of upto 1 Million pkr")
print()
print('Lets get started')

print('-->Guess Abbreviations of following. \n-->one answer = 2 lac')
print()
que = ["NUST","PCB","UET","PAF","UNESCO"]

answer = ["National University of Sciences and Technology","Pakistan Cricket Board","University of Engineering and Technology","Pakistan Air Force","United Nation Educational,Scientific and Cultural Fund" ]

prize = 0

for q in range(len(que)):
  print(que[q])
  print()
  a=input("Enter your answer :")
  if a.lower() == answer[q].lower():
    prize = prize + 2
    print("Answer is Correct")
  else:
    print("answer is wrong")
    break

print("Your Winning amount is :",prize," lac")
