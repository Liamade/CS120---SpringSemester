# -*- coding: utf-8 -*-
"""
Liam Callahan
Madlib
January 12 2024
"""
"""
Kitchen Object - "Please enter a Kitchen object:"
Adjective1 - "Please enter an adjective:"
Adjective2 - "Please enter a second adjective:"
Noun1 - "Please enter a noun:"
Noun2 - "Please enter a second noun:"
Vocal_Tone - "Please enter a vocal tone:"
Verb - "Please enter a verb:"

Output
I'm a little <kitchen_object>
<adjective1> and <adjective2>.
Here is my <noun1>, 
Here is my <noun2>. 
When I get all steamed up 
Hear me <vocal_tone>
Tip me over 
And <verb> me out!
"""

kitchen_object = input("Please enter a Kitchen Object:")
adjective1 = input("Please enter an adjective:")
adjective2 = input("Please enter a second adjective:")
noun1 = input("Please enter a noun:")
noun2 = input("Please enter a second noun:")
vocal_tone = input("Please enter a vocal tone:")
verb = input("please enter a verb:")

output = f"""
I'm a little {kitchen_object}
{adjective1} and {adjective2}.
Here is my {noun1}, 
Here is my {noun2}. 
When I get all steamed up 
Hear me {vocal_tone}
Tip me over 
And {verb} me out!
"""

print(output)
