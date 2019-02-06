import random
class Death(object):

    def story_line(self):
        quotes = [
            "You dead",
            "So dead",
            "Very dead"
        ]
        print(random.choice(quotes))


run = Death()
run.story_line()