"""
initialize variable
while condition:
    statement
    increment

escape character
================
\t tab 
\n new line
\" quotation
\\ backslash
\b backspace    
"""


i=1
while i<=100:
    if i%2!=0:
        print(i,end="\t")
    # i=i+1 ctrl+c /
    i+=1# compound assignment operator