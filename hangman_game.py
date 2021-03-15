import random
import numpy as np

def character(t):
    stages = [
    """
        _________
        |       |
        |       |
        |       O
        |      \|/
        |       |
        |      / \ 
        |________
    """,
    """
        _________
        |       |
        |       |
        |       O
        |      \|/
        |       |
        |      / 
        |________
    """,
    """
        _________
        |       |
        |       |
        |       O
        |      \|/
        |       |
        |      
        |________
    """,
    """
        _________
        |       |
        |       |
        |       O
        |      \|
        |       |
        |      
        |________
    """,
    """
        _________
        |       |
        |       |
        |       O
        |       |
        |       |
        |       
        |________
    """,
    """
        _________
        |       |
        |       |
        |       O
        |      
        |       
        |      
        |________
    """,
    """
        _________
        |       |
        |       |
        |       
        |      
        |       
        |      
        |________
    """
    ]
    return(stages[t])


def leaderboard(name,score):
    names,scores = [],[]
    names.append(name)
    scores.append(score)
    with open('names_hangman.txt','a') as f:
        for i in names:
            f.write('{}\n'.format(i))
    with open('scores_hangman.txt','a') as f:
        for i in scores:
            f.write('{}\n'.format(i))

    with open('names_hangman.txt','r') as f:
        names = f.read().splitlines()
    with open('scores_hangman.txt','r') as f:
        scores = f.read().splitlines()

    n = len(scores)
    for i in range(n):
        for j in range(0,n-i-1):
            if scores[j]<scores[j+1]:
               scores[j],scores[j+1] = scores[j+1],scores[j]
               names[j],names[j+1] = names[j+1],names[j]

    print('----------LEADERBOARD----------')
    for i in range(n):
        print('{}. {}\t\t{}'.format(i+1,names[i],scores[i]))
        

print('WELCOME TO HANGMAN')
name = input('Enter your name: ')
score = 0
flag = 0
while flag != -1:
    m=['TITANIC','THE WIZARD OF OZ','STAR WARS','TERMINATOR 2','THE GODFATHER',
        'JURASSIC PARK','HARRY POTTER','JAWS','TRANSFORMERS','PSYCHO']
    #o_word = 'TITANIC'
    my_list = []
    o_word = random.choice(m)
    if o_word
    i = 0
    missing,indices = [],[]
    r =  int(len(word)*0.5)
    while (i < r):
        x = random.randint(0,len(o_word)-1)
        #print(x)
        if word[x] == '_' or word[x] == ' ':
            continue
        if x == 0:
            if word[x+1] == '_':
                continue
        elif x == len(o_word)-1:
            if word[x-1] == '_':
                continue
        elif word[x-1] == '_' or word[x+1] == '_' or word[x] == '_':
            if i < r-2:
                continue
        word = word[:x]+'_'+word[x+1:]
        i+=1
        missing.append(o_word[x])
        indices.append(x)
    print(word)
    #print(missing)
    #print(indices)
    tries = 6
    flag = 0
    print(character(tries))
    while tries>0:
        letter = input('Enter the guessed letter: ').upper()
        if letter in missing:
            for i in range(len(missing)):
                if missing[i] == letter:
                    word = word[:indices[i]]+letter+word[indices[i]+1:]
                    missing[i]=' '
                    score += 20
            print(word)
            if '_' not in word:
                print('WOW!! YOU WON THE GAME')
                flag = 1
                score += 50
                print('Score : {}'.format(score))
                break
        else:
            
            print('Wrong Guess!!')
            tries -= 1
            print(character(tries))
            print(word)
            score -= 5

    if flag == 0 and '_' in word:
        flag = -1
        print('You lose the game')
        print('Original Word: '+o_word)
        print('Score : {}'.format(score))
        leaderboard(name,score)
        y_n = input('Play Again(y/n): ')
        if y_n == 'y':
            flag = 0
            score = 0
