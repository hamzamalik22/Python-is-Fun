import random as rd

msg = input("Enter msg : ")
lmsg = msg.split(" ")

choice = input('Enter "code" for Coding & "decode" for Decoding : ').lower()
# Encoding Part

if (choice == "code"):
  encode_word = []
  for i in lmsg:
    if (len(i) >= 3):
      r_char = [rd.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)]
      random_char = ''.join(r_char)
      new_word = random_char + i[1:] + i[:1] + random_char
      encode_word.append(new_word)
    else:
      new_word = i[::-1]
      encode_word.append(new_word)

  coded_word = " ".join(encode_word)
  print(coded_word)

# Decoding Part
elif (choice == "decode"):
  decode_word = []
  for i in lmsg:
    if (len(i) >= 3):
      random_remove = i[3:-3]
      new_word = random_remove[-1] + random_remove[:-1]
      decode_word.append(new_word)
    else:
      new_word = i[::-1]
      decode_word.append(new_word)

  decoded_word = " ".join(decode_word)
  print(decoded_word)

else:
  print("Enter Valid Option : \"code\" or \"decode\"")