import string
import sys
import random
import getpass
import redis
from questions import questions
from User import User

REDIS_PREFIX = 'onboarding_game.'

def save_record(currentScore, high_score, nickname, redis):
    if currentScore > high_score:
        redis.set(REDIS_PREFIX + nickname, currentScore)
        print "It's your new record! well done!"

def main():
    currentScore = 0
    r = redis.StrictRedis(host="pandora-redis.oxbpoj.0001.use1.cache.amazonaws.com", port=6379, db=0)

    nickname = getpass.getuser()
    high_score = r.get(REDIS_PREFIX + nickname)
    if high_score == None:
        r.set(REDIS_PREFIX + nickname , 0)

    print('\33[94m' + '****** Hello ' + nickname + ', welcome to Logz.io trivia game!!! ******')
    print("Would you like to play? (Y/n)")
    response = sys.stdin.readline().strip()
    if response != "Y":
        exit()
    else:
        # print redisHandler.get("onboarding_game.yotam")
        user = User(nickname, highestScore, currentScore)
        random.shuffle(questions)
        for question in questions:
            currentScore += question.ask()
            print "Your score is " + currentScore + "!"
            print("Continue? (ENTER/n)")
            response = sys.stdin.readline().strip()
            if response == "n":
                print "Your final score is " + currentScore + "!"
                save_record(currentScore, high_score, nickname, redis)
                exit()


if __name__ == "__main__":
    main()

