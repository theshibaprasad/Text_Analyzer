from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template("index.html")

@app.post('/analyze')
def analyze():
    text = request.form['text']
    text2 = request.form['text2']
    action = request.form['action']
    input = f"Your Input Text:- {text}"
    error= ""
    answer = ""
    if(text):
        if(action == "cntchr"):
        # count number of character
            answer=f"The Number of characters are:- {len(text)}"
        if(action =="cntws"):
        # count number of white spaces
            answer=f"The Number of white spaces are:- {text.count(' ')}"
        if(action =="ctuc"):
        # conver to uppercase
            if(text.isupper()):
                error="Your input Text is already in UPPERCASE"
            else:
                answer=f"The Converted text is:- {text.upper()}"
        if(action =="ctlc"):
        # convert to lowercase
            if(text.islower()):
                error="Your input Text is already in LOWERCASE"
            else:
                answer=f"The Converted text is:- {text.lower()}"
        if(action =="strp"):
        # strip thr text
            answer=f"The Converted text is:- {text.strip()}"
        if(action =="rmsp"):
        # remove spaces
            if(text.count(' ')):
                answer=f"The Converted text is:- { ''.join(text.split())}"
            else:
                error="Please provide spaces in between the strings !"
        if(action =="splt"):
        # split thr text
            answer=f"After spliting, text is:- {text.split()}"
        if(action =="type"):
        # check the type of the string
            if(text.isalpha()):
                answer="Text type:- ALPHABET !"
            elif(text.isdigit() or (text.isnumeric())):
                answer="Text type:- NUMERIC !"
            elif(text.isdigit() or (text.isnumeric() or '.' in text)):
                answer="Text type:- FLOATING !"
            elif(text.isalnum()):
                answer="Text type:- ALPHA-NUMERIC !"
            elif(text.isspace()):
                answer="Text type:- WHITE SPACES !"
            else:
                answer="Text type:- SPECIAL-ALPHA !"
        if(action =="ctpz"):
        # capitalized the text
            if(text==text.capitalize()):
                error="The Input Text is already in CAPITALIZE form"
            else:
                answer=f"The Converted text is:- {text.capitalize()}"
        if(action =="titl"):
        # titlized the text
            if(text==text.title()):
                error="The Input Text is already in TITLE form"
            else:
                answer=f"The Converted text is:- {text.title()}"
        if(action =="swap"):
        # swapcase the text
            answer=f"The Converted text is:- {text.swapcase()}"
        if(action =="stwt"):
        # check starts-with
            if(text2):
                answer=f"Starts with '{text2}' is:- {text.startswith(text2)}"
            else:
                error="ERROR, Provide the Input 'Text-2' !!"
        if(action =="enwt"):
        # check ends-with
            if(text2):
                answer=f"Ends with '{text2}' is:- {text.endswith(text2)}"
            else:
                error="ERROR, Provide the Input 'Text-2' !!"
        if(action =="find"):
        # find the given text
            if(text2):
                answer=f"The starting Index of '{text2}' is:- {text.find(text2)}"
            else:
                error="ERROR, Provide the Input 'Text-2' !!"
        if(action =="repl"):
        # replace the text
            if(text2):
                a,b = map(str, text2.split(','))
                answer=f"The replaced text is:- {text.replace(a.strip(),b.strip())}"
            else:
                error="ERROR, Provide the Input 'Text-2' !!"
    else:
        error="ERROR, Provide the Input Text first"
    
    return render_template("index.html",input = input, output = answer, Error= error)

