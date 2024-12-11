import random
#Variables
rougeScore = 0.5
text = ""
count = 0

def randomScore(input_text):
    #Give random value to rougeScore
    global rougeScore
    rougeScore = round(random.random(), 2)
    #Count for copy text
    global count
    count = round(rougeScore * 10)
    #Copy text
    global text
    text = input_text * count
    #Return values
    return rougeScore, text, count