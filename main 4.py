"""D-Bug's reverse scammer2000"""

# ask for their name
name = input("Hi! What's your name?\n")


# ask how they are doing
doing = name + '?' 
print(doing, end='')
ask = input(" Nice to meet you. How are you doing?\n")

# Fake receiving a typo.
# The typo will be 6 characters long and should follow this format:
# 123123
# 1 - the character x ascii positions after 'a', where x is the length of their previous response.
# 2 - the character y ascii positions before 'z', where y is the length of their name.
# 3 - the ascii character that has the decimal code z + 97,
#     where z is the absolute value of the difference between the length of their previous response
#     and their name


one = chr(len(ask) + 97)
two = chr(122 - len(name))
three = chr(abs(len(ask) - len(name)) + 97)

onetwothree = one + two + three + one + two + three

typo1 = input('My phone did not receive your last message correctly. ')
print(f'What does "{onetwothree}" mean?')

# pretend you received another typo
# The typo will be 5 of the same character, where the character is the ascii character with a decimal code
# equal to the sum of (1) the length of their previous response and (2) 32.
typo2_character = chr(len(typo1) + 32) * 5
print(f'"{typo2_character}"? What? My battery seems to be dying rather quickly. We\'ll have to continue this tomorrow.')
