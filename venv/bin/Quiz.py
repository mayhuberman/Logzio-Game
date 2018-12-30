import string
import sys
import random
import getpass
import redis
from questions import questions
from User import User

REDIS_PREFIX = 'onboarding_game.'


def save_record(currentScore, high_score, nickname, redis):
    if int(currentScore) > int(high_score):
        redis.set(REDIS_PREFIX + nickname, currentScore)
        print str(currentScore) + " - It's your new record! well done!"


def main():
    currentScore = 0
    r = redis.StrictRedis(host="pandora-redis.oxbpoj.0001.use1.cache.amazonaws.com", port=6379, db=0)

    nickname = getpass.getuser()
    high_score = r.get(REDIS_PREFIX + nickname)
    if high_score == None:
        r.set(REDIS_PREFIX + nickname, 0)
    else:
        print "your highest score: " + str(high_score)

    print('\33[94m' + '****** Hello ' + nickname + ', welcome to Logz.io trivia game!!! ******')
    print("Would you like to play? (Y/n)")
    response = sys.stdin.readline().strip()
    if response != "Y":
        exit()
    else:
        # user = User(nickname, highestScore, currentScore)
        random.shuffle(questions)
        for question in questions:
            print currentScore
            currentScore += question.ask()
            print currentScore

            print "Your score is " + str(currentScore) + "!"
            print("Continue? (ENTER/n)")
            response = sys.stdin.readline().strip()
            if response == "n":
                print "Your final score is " + str(currentScore) + "!"
                save_record(currentScore, high_score, nickname, r)
                exit()
        save_record(currentScore, high_score, nickname, r)


if __name__ == "__main__":
    main()

