# Build Chatbots with Python

# Looping Coffee Chatbot

# When in doubt, drink more coffee!

# In the previous Coffee Chatbot project, you learned to build a Python chatbot 
# for ordering one cup of coffee by leveraging recursive functions, 
# user inputs, and print statements. The solution code from that project is
#  carried over here. Now, it’s time to take this chatbot to the next level
#  by adding loops!

# Loops allow us to perform some action repeatedly – such as placing an order 
# for multiple drinks – without needing to write an excess amount of code.

# Let’s get started!

from x_utils_looping_coffee_chatbot import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = "y"
  drinks = []

  while order_drink == "y":
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)

    while True:
      order_drink = input("Would you like to order another drink? (y/n) \n> ")

      if order_drink in ["y", "n"]:
        break
    print(" Okay, so we have:")

    for drink in drinks:
      print("-", drink)
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  while True:
    res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next zime! \n>")
    if res == "a":
      return "peppermint mocha"
    elif res == "b":
      return "mocha"
    print_message()


coffee_bot()
