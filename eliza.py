import re
import platform
from dictionary.ResponseGenerator import ResponseGenerator

# Color for terminal messages
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
END_COLOR = "\033[0m"

#if ("windows" in platform.system().lower()):
#	RED = BLUE = GREEN = END_COLOR = ""

# Styling
WIDTH_SPACE = "       "

# Constants
EXIT = "exit"
BYE = "bye"
REOPENED = "1"

# Define the types of sentences ELIZA can understand
hello = re.compile(r"^(Hell(o)+|H(i)+|He(y)+).*$", re.IGNORECASE)
helloRes = ""
with open("opened.eliza", "a+") as f:
	f.seek(0) # we position a+ stream at the start of file
	content = f.readline()
	helloRes = "Hello! Good to see you again.\n" + WIDTH_SPACE + "How are you feeling today?"
	if (content != REOPENED):
		helloRes = "Hello! How are you feeling today?"
		f.write(REOPENED)

notFeelingIt = re.compile(r"not ((feeling )?(it|good|happy|amazing|great))", re.IGNORECASE)
notFeelingItRes = "Why are you not feeling {}?"	

badFeeling = re.compile(r"(bad|worse|disgusting|disgusted)", re.IGNORECASE)
badFeelingRes = "Why are you feeling {}?"
	
elaborateFurther = re.compile(r"((Because |Because of my |Because my |My )).* (ex|husband|wife|boyfriend|girlfriend|partner|lover|date|(best )?friend(s?)|dad|father|mom|mother|brother|sister|bro|sis|cousin)( (is)|(does not|doesnt|doesn't|is not able to|isnt able to|isnt able to))?", re.IGNORECASE)
elaborateFurtherRes	= "In what way did your {} make you feel bad?"

furtherElaboration = re.compile(r"(he|she|they) (((got me|made me) (mad|angry)))", re.IGNORECASE)
oFurtherElaboration = re.compile(r"(he|she|it|the|they).* (makes me|made me|did|are|is|are doing|is doing|are behaving|is behaving)", re.IGNORECASE)
furtherElaborationRes = "There might have been a misunderstanding between you.\n" + WIDTH_SPACE + "You should clear your mind and talk to them again later" 
	
depressedSad = re.compile(r"(I'm |im |I am |feel )(depressed|sad)", re.IGNORECASE)
depressedSadRes = "I'm sorry you feel {}. I'm here for you.\n" + WIDTH_SPACE + "Is there anything you want to tell me?"

unhappy = re.compile(r"(I'm |im |I am |feel )(still |so |really )?(unhappy)", re.IGNORECASE)
unhappyRes = "Do you think coming here will help you not to be {}?"

unsure = re.compile(r"(((I do not|I don't|I dont|I) (think|believe|feel certain|feel sure|feel confident|feel like))|(I am not sure|I am unsure|I'm not sure|I'm unsure))( that)? I( will(( not)? be able to)?| can| am able to|'ll|ll) (endure|go through|get through|solve)", re.IGNORECASE)
unsureRes = "I am sure you will {} your problems.\n" + WIDTH_SPACE + "It is okay to feel this way when you are stressed or if you recently had a loss.\n" + WIDTH_SPACE + "Does taking a walk and relaxing sound like a good idea?"

problems = re.compile(r"(I (have|encountered) (a |A |an ))(problem|issue)", re.IGNORECASE)
problemsRes = "Can you tell me more about the {}?"

agree = re.compile(r"(I agree)|(agreed)|(we agree)", re.IGNORECASE)
agreeRes = "I'm glad we agree!"

thankYou = re.compile(r"(Thank you)|(Thanks)|(Thank)", re.IGNORECASE)
thankYouRes = "You're welcome!"

yes = re.compile(r"^((Yes+(!+)?)( it does+(!+)?)?)$", re.IGNORECASE)
yesRes = "Wonderful!"

# List of regex and responses (third parameter indicates which groups should replace the '{}' in order)
responseGenerators = []
responseGenerators.append(ResponseGenerator(notFeelingItRes, notFeelingIt, [3]))
responseGenerators.append(ResponseGenerator(furtherElaborationRes, furtherElaboration, []))
responseGenerators.append(ResponseGenerator(furtherElaborationRes, oFurtherElaboration, []))
responseGenerators.append(ResponseGenerator(badFeelingRes, badFeeling, [1]))
responseGenerators.append(ResponseGenerator(elaborateFurtherRes, elaborateFurther, [3]))
responseGenerators.append(ResponseGenerator(depressedSadRes, depressedSad, [2]))
responseGenerators.append(ResponseGenerator(unhappyRes, unhappy, [3]))
responseGenerators.append(ResponseGenerator(unsureRes, unsure, [10]))
responseGenerators.append(ResponseGenerator(problemsRes, problems, [4]))
responseGenerators.append(ResponseGenerator(agreeRes, agree, []))
responseGenerators.append(ResponseGenerator(thankYouRes, thankYou, []))
responseGenerators.append(ResponseGenerator(yesRes, yes, []))
responseGenerators.append(ResponseGenerator(helloRes, hello, []))

print(f"""
      
███████╗██╗░░░░░██╗███████╗░█████╗░
██╔════╝██║░░░░░██║╚════██║██╔══██╗
█████╗░░██║░░░░░██║░░███╔═╝███████║
██╔══╝░░██║░░░░░██║██╔══╝░░██╔══██║
███████╗███████╗██║███████╗██║░░██║
╚══════╝╚══════╝╚═╝╚══════╝╚═╝░░╚═╝
      """)
print(f"A simple chatbot using {BLUE}regex{END_COLOR} for {BLUE}Theory of Calculation{END_COLOR} course, University of Macedonia.\n\n\n\n")


message = str(input(f"{BLUE}You:{END_COLOR}   "))
while (message.lower() != EXIT and message.lower() != BYE):
    isMatched = False
    for generator in responseGenerators:
        if (generator.matches(message) and not isMatched):
            response = generator.generateResponse()
            print(f"{GREEN}ELIZA:{END_COLOR} {response}")
            isMatched = True
            break
            
    if (not isMatched):
        print(f"{RED}ELIZA:{END_COLOR} I don't think I understood that correctly...")
    
    message = str(input(f"{BLUE}You:{END_COLOR}   "))

print(f"{GREEN}ELIZA:{END_COLOR} Looking forward to talking to you again.\n" + WIDTH_SPACE + "Have a nice day. Bye!")
