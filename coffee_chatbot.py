# Build Chatbots with Python

# Coffee Chatbot

# But first, coffee.

# Whether it’s to get us ready to jump-start our day or to get us through a late-night cram session, 
# many of us need our regular caffeine fix! Ordering coffee is just one example of a process that can 
# be automated with the help of a chatbot.

# You’re given the task of creating a Python chatbot that can help cut the wait time of a normal coffee 
# run by taking customers’ orders in advance. 
# Write your code in the file called script.py and run it by entering python3 script.py in the terminal.

# -----------------------------------------------------------------------------------------------------

# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size("Espresso", "Latte", "Black")
  #print(size)

  drink_type = get_drink_type("Brewed Coffee", "Mocha", "Latte")
  #print(drink_type)

  print("Alright, that's a {} {}!".format(size, drink_type))

  name = input("Can I get your name please? \n> ")
  print("Thanks, {}! Your drink will be ready shortly.".format(name))

  extra_options()

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def order_latte(a, b, c):
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == "a":
    return "latte"
  elif res == "b":
    return "non-fat latte"
  elif res == "c":
    return "soy latte"
  else:
    print_message()
    return order_latte(a, b, c)


def get_size(a, b, c):
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size(a, b, c)

def get_drink_type(a, b, c):
  res = es = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')   
  if res == "a":
    return "Brewed Coffee"
  elif res == "b":
    return "Mocha"
  elif res == "c":
    return order_latte(a, b, c)
  else:
    print_message()
    return get_drink_type(a, b, c)

def extra_options():
  res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')

  if res == 'a':
    print('Okay, no problem! We\'ll get you a plastic cup.')
  elif res == 'b':
    print('Great! We\'ll fill up your reusable cup.')
  else:
    print_message()
    return extra_options()  

# Call coffee_bot()!
coffee_bot()


