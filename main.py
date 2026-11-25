"""Creat a text file containing sentences and build a word counter for it."""

def word_count(text):
    
    words = text.split()  #split each words.
    return len(words)     #return the length to the main function.

def main():
    
    with open("notes.txt","r") as file:
        content = file.read()
        
    total_words = word_count(content)
    print(total_words)
    
    
main()