import re
import platform
from dictionary.ResponseGenerator import ResponseGenerator

# Color for terminal messages
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
END_COLOR = "\033[0m"

if ("windows" in platform.system().lower()):
	RED = BLUE = GREEN = END_COLOR = ""

# Styling
WIDTH_SPACE = "       "

# Constants
EXIT = "exit"

# Define the types of sentences ELIZA can understand
depressedSad = re.compile(r"(I'm |im |I am |feel )(depressed|sad)", re.IGNORECASE)
depressedSadTemplate = "I'm sorry you feel {}. Is there anything you want to tell me?"

unhappy = re.compile(r"(I'm |im |I am |feel )(unhappy)", re.IGNORECASE)
unhappyTemplate = "Do you think coming here will help you not to be {}?"

unsure = re.compile(r"(((I do not|I don't|I dont) (think|believe|feel certain|feel sure|feel confident))|(I am not sure|I am unsure|I'm not sure|I'm unsure) (that)? I (will(be able to)?|can|am able to)) (endure|go through|get through|solve)", re.IGNORECASE)
unsureTemplate = "I am sure you will {} your problems.\n" + WIDTH_SPACE + "It is okay to feel this way when you are stressed or if you recently had a loss.\n" + WIDTH_SPACE + "Does taking a walk and relaxing sound like a good idea?"

problems = re.compile(r"(I (have|encountered) (a |A |an ))(problem|issue)", re.IGNORECASE)
problemsTemplate = "Can you tell me more about the {}?"

yes = re.compile(r"yes", re.IGNORECASE)
yesTemplate = "I'm glad we agree!"

# List of regex and responses (third parameter indicates which groups should replace the '{}')
responseGenerators = []
responseGenerators.append(ResponseGenerator(depressedSadTemplate, depressedSad, [2]))
responseGenerators.append(ResponseGenerator(unhappyTemplate, unhappy, [2]))
responseGenerators.append(ResponseGenerator(unsureTemplate, unsure, [9]))
responseGenerators.append(ResponseGenerator(problemsTemplate, problems, [4]))
responseGenerators.append(ResponseGenerator(yesTemplate, yes, []))

print(f"""
      
███████╗██╗░░░░░██╗███████╗░█████╗░
██╔════╝██║░░░░░██║╚════██║██╔══██╗
█████╗░░██║░░░░░██║░░███╔═╝███████║
██╔══╝░░██║░░░░░██║██╔══╝░░██╔══██║
███████╗███████╗██║███████╗██║░░██║
╚══════╝╚══════╝╚═╝╚══════╝╚═╝░░╚═╝
      """)
print(f"A simple chatbot using {BLUE}regex{END_COLOR} for {BLUE}Theory of Calculation{END_COLOR} course, University of Macedonia.\n\n\n\n")


message = str(input("You: "))
while (message.lower() != EXIT):
    isMatched = False
    for generator in responseGenerators:
        if (generator.matches(message) and not isMatched):
            response = generator.generateResponse()
            print(f"{GREEN}ELIZA:{END_COLOR} {response}")
            isMatched = True
            
    if (not isMatched):
        print(f"{RED}ELIZA:{END_COLOR} I don't think I understood that correctly...")
    
    message = str(input("You: "))

print(f"{GREEN}ELIZA:{END_COLOR} Have a nice day. Bye!")
