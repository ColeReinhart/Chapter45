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
            BadOpt.steal()
        
        elif choice == "3":
            BadOpt.bribe()


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

    def steal(self):
        print("You trudge off past the kid.")
        print("The whole room is asleep, since they don't have the strength to stay awake.")
        print("Once you get close to the door and the kid screams to wake up everyone to stop you.")
        print("He is stealing the food! he screamed")
        print("In panic, you run to open the door and leave.")
        print("When you open the door zombies heard the scream and surrounded the building.")
        print("Before you can leave you area swarmed by the zombies and the whole shelter is infected.")
        print("YOU HAVE DIED")
        print("Play Again?")
        choice = input("> ")
        if choice == "yes":
            do.start()
        else:
            exit(0)

    def bribe(self):
        print("The kid looks at you confused.")
        print("But like everyone here he is starving.")
        print("You give him some rations and he runs off")
        print("You make your way to the door, holding whats left of the rations.")
        print("You want to take Julie with, but you know she would not condone you actions.")
        print("So you head towards the door, rations over your back in a sack.")
        print("As soon as you open the door, the guard wakes up.")
        print("You notice and hurry out the door.")
        print("You close the door and run")
        print("You can't see due to the nighttime darkness and lack of electricity for the street lights.")
        print("Where do you run?")
        print("1. Grocery store")
        print("2. Your old home")

        choice = input("> ")

        if choice == "1":
            good.store()
        elif choice == "2":
            BadOpt.home()


    def home(self):
        print("You break away from the shelter.")
        print("You would rather die out here than in there anyway.")
        print("You want to see your home, you miss it.")
        print("As a 20 year old college student, you feel like you haven't spent enough time there.")
        print("So you go back there one last time.")
        print("You sneak past some zombies with out being noticed and 20 minutes later you are faced with you fron door step.")
        print("Nervous. You walk inside.")
        print("Blood smeared on the walls, but other than the mess from obvious struggle, it's just as you left it.")
        print("The day everything went down was the day you came home from school for break.")
        print("You remember opening the door to your parents packing frantically.")
        print("FLASHBACK")
        print("Mom? Dad? Whats going on!")
        print("Pack your things were leaving!")
        print("Mom! what is happening?")
        print("ARGHH!")
        print("Dad what's going on back there?!")
        print("Your brother bit me! He's infected, Shit!")
        print("Infected? Mom what does he mean!")
        print("WE NEED TO GO! NOW")
        print("END FLASHBACK")
        print("You see the corpses of your mother and father....")
        print("You hear banging on your brothers door and growling...")
        print("Brother?")
        print("The door breaks open and he attacks you.")
        print("You do not have any items to protect yourself and he gets a bite on you.")
        print("Your vision fades as you wish you made better life choices.")
        print("YOU HAVE DIED!")
        print("Play Again?")

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
        print("Julie tells you to be safe and that she is too ill to accompany you.")
        print("The front door guard wishes you luck and hands you a glock 9mm handgun and a clip with 8 bullets.")
        print("Sorry but that all we have left, were really depending on you.")
        print("You are on your way.")
        print("When you open the door and exit the safe house, the sun blinds you a bit.")
        print("Disoriented, you start walking, listening for zombie growls.")
        print("You regain you eyesight but it has been a while since you ran so you balence is a little off.")
        print("After about 3 minutes of walking past broken and empty houses, you spot the undead approaching you.")
        print("There is 3 Zombies. They haven't spotted you.... yet. Time to act.")
        print("1. Take cover behind a bush, hope that they can't smell your scent.")
        print("2. Open fire on the zombies")
        print("3. Run away")

        choice = input("> ")

        if choice == "1":
            cover
        elif choice == "2":
            shoot
        elif choice == "3":
            run

    def store(self):
        print("It's dark outside, Which means you are as hard to see as the zombies.")
        print("Based on this logic you decide to head to the grocery store.")
        print("You see some zombies walking toward your direction.")
        print("There is 3 Zombies. They haven't spotted you.... yet. Time to act.")
        print("1. Take cover behind a bush, hope that they can't smell your scent.")
        print("2. Fight them")
        print("3. Run away")


BadOpt = bad()
Good = good()

do = SafeHouse()

do.start()