print("="*23)
print("Basic Chatbot (Jarvis)")
print("="*23)

print("\nAsk me any of these 5 questions from Jarvis : \n")

print('''
      Question 01 : Hi
      Question 02 : How are you?
      Question 03 : What is your name?
      Question 04 : Can you save me?
      Question 05 : Bye
''')

a = "hi"
b = "how are you?"
c = "what is your name?"
d = "can you save me?"
e = "bye"

p = "Hello!"
q = "Fine,Thanks!"
r = "I am Jarvis, an AI"
s = "Sure , my pleasure"
t = "GoodBye!"

x = "Sorry, I didn't get that!"

def chatbot() :

        if user == a :
            print(f"Jarvis : {p}\n")
        elif user == b :
            print(f"Jarvis : {q}\n")
        elif user == c :
            print(f"Jarvis : {r}\n")
        elif user == d :
            print(f"Jarvis : {s}\n")
        elif user == e :
            print(f"Jarvis : {t}")
        else :
            print(f"Jarvis : {x}\n")
        
while True :
    user = input("You : ")
    chatbot()

    if user == e :
        print("Thanks for playing with me")
        break