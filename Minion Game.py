def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    vowels="AEIOU"
    length=len(string)
    for i in range(length):
        if(string[i] in vowels):
            kevin+=length-i
        else:
            stuart+=length-i
            
    if(stuart>kevin):
        print(f"Stuart {stuart}")
    elif(kevin>stuart):
        print(f"Kevin {kevin}")
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)
