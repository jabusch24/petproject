import urllib.request
from bs4 import BeautifulSoup
import random

def enter_difficulty():
    try:
        return int(input("Choose the length of the word to guess:"))
        
    except ValueError:
        print("Please type in an integer between 3 and 12!")
        return enter_difficulty()

def get_words(difficulty):
    offline = None
    try:
        url = "https://wordfinder.yourdictionary.com/letter-words/"+str(difficulty)+"/" 
        response = urllib.request.urlopen(url)
        webContent = response.read()
        soup = BeautifulSoup(webContent, "html.parser")

        i = 0
        words = {}
        for element in soup.find_all('tr'):
            if len(element.a.get('href')) == 25 + difficulty and len(element.a.get_text()) == difficulty: 
                tds = element.find_all('td')
                words[i] = {"word": tds[0].get_text(), "scrabble": tds[1].get_text(), "wordswithfriends": tds[2].get_text()}
                i += 1
    except:
        words = {3: {"word":"vox", "scrabble": 10, "wordswithfriends": 12},
                 4: {"word":"king", "scrabble": 10, "wordswithfriends": 12},
                 5: {"word":"queen", "scrabble": 10, "wordswithfriends": 12},
                 6: {"word":"sweden", "scrabble": 10, "wordswithfriends": 12},
                 7: {"word":"ceiling", "scrabble": 10, "wordswithfriends": 12},
                 8: {"word":"theology", "scrabble": 10, "wordswithfriends": 12},
                 9: {"word":"breakfast", "scrabble": 10, "wordswithfriends": 12},
                 10: {"word":"skyjacking", "scrabble": 10, "wordswithfriends": 12},
                 11: {"word":"lumberjacks", "scrabble": 10, "wordswithfriends": 12},
                 12: {"word":"maximization", "scrabble": 10, "wordswithfriends": 12}
                }
        offline = difficulty
    return (words, offline)

def play_game(words, offline):
    guesses = ""
    turns = 10

    # Randomly determine the secret word based on difficulty level
    if offline == None:
        index = random.randint(0, len(words)-1)
    else:
        index = offline
    word = words[index]["word"]
    print(word)

    while turns > 0:
        dash_word = ""
        failed = 0
        for char in word:
            if char in guesses:
                dash_word += char + " "
            else:
                dash_word += "_ "
                failed += 1

        if failed == 0:
            print("You won. Final word is: ", dash_word)
            return (True, words[index])
        # exit the script
            break
        # print
        print(dash_word)
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")
                return (False, words[index])
            
def game_finish():
    try:
        response = str(input("Do you want to play another round? (y/n)"))
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Please respond only with y or n!")
            return game_finish()
            
    except ValueError:
        print("Please respond only with y or n!")
        return game_finish()
        

def main():
    
    keep_playing = True
    while keep_playing == True:
        
        difficulty = enter_difficulty()
        while difficulty < 3 or difficulty > 12:
            print("Again, your number should be between (and including) 3 and 12!")
            difficulty = enter_difficulty()
        words, offline = get_words(difficulty)

        victory, word = play_game(words, offline)
        if victory == True:
            print("Congrats! You made it! In scrabble you could have gotten",word["scrabble"],"points and", word["wordswithfriends"]," points in words with friends!")
            keep_playing = game_finish()
        else:
            print("Awww, maybe next time! In scrabble you could have gotten",word["scrabble"],"points and", word["wordswithfriends"]," points in words with friends!")
            keep_playing = game_finish()
        
    print("Bye, bye :) ")
    return victory
        
if __name__ == '__main__':
    main()
