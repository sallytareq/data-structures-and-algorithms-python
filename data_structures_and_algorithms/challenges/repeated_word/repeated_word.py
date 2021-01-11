import regex as re

def repeated_word(text):
    if type(text) != str:
        return 'Invalid Input'
    
    # set allows for a O(1) search complexity
    checker = set()

    # split at words only to not include special characters 
    full_text = re.split("\W+", text.lower().strip())

    # print(full_text)

    for word in full_text:
        if word in checker:
            # the first duplication is returned 
            return word  
        
        # if not a duplicate add it to the set for the next comparison
        checker.add(word)  
    else:
        return 'No repeats'



if __name__ == "__main__":
    text = "Once upon a time, there was a brave princess who..."
    text1 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    text2 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    x = repeated_word(text)
    print(x)
    y = repeated_word(text1)
    print(y)
    z = repeated_word(text2)
    print(z)