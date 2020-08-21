'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    
    #set count to 0
    count = 0
    
    #set base case if the word is less than 2 letters
    if len(word) < 2:
        #then return 0
        return 0

    #if the first 2 letters are equal to th
    if (word[:2] == 'th'):
        #then increment the count by 1
        count += 1
        
    #return the count
    return count + count_th(word[1:])
