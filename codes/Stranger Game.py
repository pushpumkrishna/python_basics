#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(""""
Welcome to the game: Surviving the Stranger !!!
You have met a stranger in the jungle. Choose your options to stay alive.
Do you want to 
1). Talk to him
2). Do not talk and leave
3). Stare at him
""")

option = input("> ")

if (option == '1'):
  print("""He's staring at you right now. Either he's angry or not interested. 
  What do you want to do now?

  1). Talk to him
  2). Look back angrily.
  3). Attack him.
  """)
elif (option == '2'):
    print("Stranger got angry and kills you. You lost !")
else:
    print("Stranger got angry and kills you. You lost !")
    
option_2 = input("> ")

if (option_2 == '1'):
  print('Stranger greets you and ask your name. Congrats ! you won.')
elif (option_2 == '2'):
  print('Stranger takes a knife out and kills you.   !')
elif (option_2 == '3'):
  print("Stranger got afraid and attacks you back and kills you")
else:
  print("Invalid choice. Stranger kills you for a stupid choice.")

if (option_2 == '1'):
  print("1. Smile back.")
  print("2. Ask his name and What is he doing here")
  print("3. Just ignore back. ")

option_3 = input("> ")

if (option_3 == 1 or option_3 ==2):
  print("You survives and got a hug from stranger.")
  print("Good Job.")
else:
  print("The strnager is fuming and kills you for being rude.")
  print("You lost !")


# In[ ]:




