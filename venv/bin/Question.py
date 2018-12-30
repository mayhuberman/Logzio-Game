import sys


class Question(object):

    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def ask(self):
        print self.question + "?"
        for n, option in enumerate(self.options):
            print "%d) %s" % (n + 1, option)

        response = int(sys.stdin.readline().strip())  # answers are integers
        if response == self.answer:
            print "CORRECT"
            return 10
        else:
            print "WRONG"
            return 0

