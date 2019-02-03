## The game will be based on a zombie apocolyptic world
## The choices you make will affect the outcome and survival
## much like the walking dead but not quite because im still a scrub
## I call this game Zombocolyptic


class SafeHouse(object):

    def start(self):
        print("Its been 5 months since the apocolypse hit Pennsylvania. You managed to make it to a local safe house about 3 months ago.")
        print("You wake up in the safe house. Seeing every starving soul in there, the whole 50 people clenching to life.")
        print("The food stock is low and there isn't much time before the whole place either dies or goes insane.")
        print("Few people have left the safe house in search for food and supplies but none have returned. In this panic, the food is being ratinoned heavily.")
        print("Julie, who you have been traveling with since you saved her life in the early stagesof the outbreak, is growing weak. She has been giving all of her rations to the children in the safe house and has accepted death.")
        print(" She is too good of a person to die, you think. She is your bestfriend in these trying times. You know there is a grocery store about 2 miles north.")
        print("Others have tried to make it there, but none have returned. Staying here will surely mean the end of everyone in the shelter if no one can get supplies.")
        print("You do have access to the food stock though... since you are a trusted member and are tasked with guarding the food, no one could stop you from taking it and leaving.")
        print("There is not much time left before something happens, there isn't enough food for 4 people alone 50... 49. Another person is on there way to meet our creator.")
        print("Time to move.")
        print("1. Take what is left of the rations and leave")
        print("2. Tell everyone you volunteer to try and make it to the store and bring supplies back")
        print("3. Stay and wait for help")

        choice = input("> ")

        if choice == "1":
            BadOpt.scumbag()
        elif choice == "3":
            BadOpt.Starve()
        
        elif choice == "2":
            Good.volunteer()

class bad(object):
    def scumbag(self):
        print("You decide to take the scumbag route and steal the food")
        print("Better than starving you think. But what about Julie?")
        print("Survival of the fittest I suppose.")
        print("You wait till midnight and sneak into the food supply")
        print("As you are opening the locker you see a child about 6 years old")
        print("He looks at you and asks, why are you taking the food?")         
        print("You look at him, in his tore clothes and dirty face")
        print("1. Put the food back")
        print("2. Don't say a word, just take the food and go")
        print("3. Ask the kid if he wants some to keep him quiet")

        choice = input("> ")
        if choice == "1":
            do.start()
        elif choice == "2":     
            steal()

    def Starve(self):
        print("You try to wait out the inevitable.")
        print("One week later. The shelter is not contaminated with an illness.")
        print("Most importantly, Julie passed.")
        print("There is no reason to live, you have no will.")
        print("After a day of crying about Julie's passing you go insane.")
        print("Eventually you become suicidal and open the shelter door and the whole compound is flooded with zombies...")
        print("YOU HAVE DIED")
        print("play again?")
        choice = input("> ")
        if choice == "yes":
            do.start()
        else:
            exit(0)

class good(object):
    def volunteer(self):
        print("You decide to go outside, a place you aren't familiar with anymore.")
        print("You tell the survivors that you are going out to get supplies.")
        print("They tell you its dangerous and you might not come back.")
        print("But it is almost better than starving in here.")
        print("Julie tells you to be safe and ")

BadOpt = bad()
Good = good()

do = SafeHouse()

do.start()