from sys import exit
from random import randint
from textwrap import dedent

#global variables tha create fail conditions based on choices
tired = 0
hopelessness = 0
antisocial = 0

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):
    global tired
    global hopelessness
    global antisocial

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            
            if tired >= 3:
                print("You are too tired to continue. Better luck next time.")
                exit(0)
            elif hopelessness >= 3:
                print("You are too hopeless to be around children. You lose.")
                exit(0)
            elif antisocial >= 3:
                print("You are too antisocial to work with others. Work on your personality.")
                exit(0)                
            else:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Fired(Scene):
    quips = [
        "In the words of our president: 'You're Fired!'",
        "Fired! Hope you didn't need that money for anything",
        "You let the children win. Meaning you lose. And you're fired.",
        "You, my friend, are fired. But don't be depressed. This job sucks anyways",
        "Thos who can't do, teach. Those who can't teach . . . are fired."
    ]

    def enter(self):
        print(Fired.quips[randint(0, len(self.quips)-1)])
        exit(1)

class WakeUp(Scene):
    
    def enter(self):
        global tired
        global antisocial        
        print(dedent("""
            Your alarm rings breaking the near perfect silence of 5
            AM. Startled out of a nice dream about your kitten farm
            you remember that today is Monday. Ahead of you is another
            day of teaching at Elsik High School.

            The Sunday Night Blues kept you from falling asleep and 
            you had one too many beers while watching stupid TV last
            night. An extra 15 minutes of sleep would make it marginally easier 
            to face the day, but it will mean forgoing your morning shower.  
            """))
        action = input ("Do you 'shower' or 'snooze' the alarm?")

        if action == "shower":
            print(dedent("""
                The water is slow to warm up and you miss the comfort of your
                cozy bed. This is an ungodly hour when no one should have to be
                awake, much less functional. Standing underneath the unsatisfying
                spray of the showerhead you think about all the way that life
                could have gone differently. Then, the existential crisis passes
                and you get dressed for work.
                """))
            tired += 1
            input("Press any key to continue")
            return "drive_in"
        elif action == "snooze":
            print(dedent("""
                You hit the snooze button and are back asleep in an instant.
                Unfortunately the dream of kittens is gone and you have fitful
                nightmares about unruly students and unreasonable administrators.
                Before long the alarm rings again and you tear yourself from bed.
                You dress in 30 seconds, grab leftovers from the fridge and are 
                on your way.
                """))
            antisocial += 1
            input("Press any key to continue")
            return "drive_in"
        else:
            print("Please choose to 'shower' or 'snooze'.")
            return 'wake_up'

class DriveIn(Scene):
    
    def enter(self):
        global tired
        print(dedent("""
            You get into the beater that you are nowhere near paying
            off. As you drive the monotonous route past billboards for
            chicken restaurants and weave shops the traffic seems to flow
            at a steady pace.
            """))
        input("Press any key to continue")
        if (tired > 0):
            print(dedent("""
                You yawn so loudly that you nearly cause a traffic 
                accident as the other drivers mistake you for an African
                lion.
            """))
            action = input("Do you stop for coffee?")

            if action == "yes":
                print("You stop at a local dumbStarbucks.")

                roll = randint(0, 2)

                if roll == 0:
                    print(dedent("""
                        Unfortunately the lines are longer than a James Cameron movie")
                        Though the caffeine takes the edge off of you sleepiness,
                        there is no way that you will make it to work on time.
                        """))
                    return "fired"
                else:
                    print(dedent("""
                        There are no other customers in the coffee shop. A
                        few minutes later you have a cup of warm liquid-happiness
                        in hand. You resume you drive to your place of employment.
                        MMM coffee.
                        """))
                    tired -= 1
                    input("Press any key to continue")
                    return "first_period"
            elif action == "no":
                print("Too scared to risk it, you continue the trek to the school.")
                tired += 1
                return 'first_period'
            else:
                print ("Please type 'yes' or 'no'.")
                return 'drive_in'
        else:
            return 'first_period'


class FirstPeriod(Scene):

    def enter(self):
        global hopelessness        
        print(dedent("""
            You make it to school and prepare your amazing, life-
            changing lesson. Before you know it, the bell rings and
            pimply, bleary-eyed high school students begin to file into
            your room. As you stand there and great them most of them 
            only respond with a monosyllabic grunt. You wonder, not for
            the first time, if they even know how to speak aside from
            texting.

            Partially through your lesson you notice a student doing
            just that. You have to decide whether to address the issue.
            """))

        action = input(dedent("""
                    Do you 'stop the lesson' and confront the texter 
                    or 'ignore' and continue the lesson?")
                    """))

        if action == "stop the lesson":
            print(dedent("""
                You pause mid sentence in the middle of the lecture.
                The few students that are paying attention look up to 
                see what is about to happen. The texter, of course, does
                not notice and continues to text without even trying to hide
                it.

                Only when you are standing right next to the student does
                he see you. He looks up without putting his phone away. Do you:
                make a 'joke' and remind the student to put the phone away
                or 'threaten' to write a referral?
                """))
            approach = input("> ")

            if approach == 'joke':
                print(dedent("""
                    The class laughs at your amazing humor, and the student
                    reluctantly puts his phone back in his pocket. You know
                    that the phone will come out again as soon as he believes
                    that you are not paying attention, but for the moment you
                    are victorious. Don't let it go to your head.
                    """))
                input("Press any key to continue")                
                return "second_period"
            elif approach == 'threaten':
                print(dedent("""
                    Infuriated by this blatant dismissal of class rules,
                    you grab a referral from your desk and shove it into the 
                    students face. Without missing a beat, he switches to the camera
                    app on his cellphone and starts videoing you. 'My teacher
                    started going crazy and cussing me out! Look at this!' The 
                    more you deny it, the worse it starts to look. After class he
                    uploads it to youtube and soon it is all over the school. The
                    principal calls you into her office early the next morning.
                    Turns out the student's mother is on the school board and she
                    100% believes his version of events.
                    """))
                return 'fired'
            else:
                print("That was not an option, try again.")
                return("first_period")
        elif action == "ignore":
            print(dedent("""
                In the great scheme of things, what does one student on 
                their phone matter? What does any of this matter? Why are 
                we here? What is the purpose of life? If God exists, why are
                people starving in Africa . . .

                The rest of your lecture fizzles out as you find yourself distracted
                by your thoughts.
                """))
            hopelessness += 1
            input("Press any key to continue")            
            return 'second_period'
        else:
            print("Sorry, I didn't catch that. Please try again.")
            return 'first_period'


class SecondPeriod(Scene):
    def enter(self):
        print(dedent("""
            One class down, only six periods to go! On second thought
            maybe better not to keep track of time. You look at the clock
            and let out a huge yawn as you realize that it is still long
            before civilized people are stirring from their beds.

            The students seem to be in a similar frame of mind. Partially
            through your lecture, you notice someone sleeping in the front row.
            (Jeez, you thought that this was an interesting topic when you
            were planning last night. What does it take to impress these kids
            anyways.) If it was in the back row you could just ignore it,
            but since it is right underneathe your nose you have no plausible 
            deniability.

            What do you do?
            """))
        action = input("'ignore' or 'approach' the student")

        if action == 'ignore':
            print(dedent("""
                I literally just said that you can't ignore it.
                You aren't a very good listener are you. Fine, then.
                The principal walks in for a random walk-through and sees
                the sleeping student. She asks why there is a student sleeping
                in the front row. Then she fires you.
                """))
            return 'fired'
        elif action == 'approach':
            print(dedent("""
                As you approach the unconcious student, you remember
                that this student has a strange condition where he only responds
                to input that is repeated a specific number of times. Is that 
                even a thing? Kids these days. Why can't they be normal.

                You will have to remember the number of times to shake the
                student before the principal walks in and sees him sleeping.
                Somehow you have a feeling that you will only have four chances.
                You also have a feeling that it is 10 or less. You have a lot
                of feelings. Maybe you are on your period.
                """))

            magic_num = randint(2, 10)
            guess = input("How many times do you shake the student?")
            counter = 0

            while (int(guess) != magic_num): #and counter < 3
                print("You shake the student, but nothing happens")
                counter += 1
                guess = input("How many times do you shake the student?")

            if (int(guess) == magic_num):
                print(dedent("""
                    The student snaps awake like a 5-year-old on Christmas
                    morning. You keep an eye on him as you continue your lesson
                    but it appears that the urge to sleep has passed.
                    """))
                input("Press any key to continue")            
                return 'third_period'
            else:
                print(dedent("""
                    The principal walks in for a random walk-through and sees
                    the sleeping student. She asks why there is a student sleeping
                    in the front row. Then she fires you.
                    """))
                return 'fired'
        else:
            print("Didn't catch that")
            return 'second_period'


class ThirdPeriod(Scene):
    def enter(self):
        global tired
        global hopelessness
        global antisocial    
        print(dedent("""
            The bell rings and students rush from the class like their
            lives depend on it. You take a deep breath. It is your off
            period and for the next 50 minutes you have peace and quiet
            to grade, prepare for your next lesson, or nap.

            Or you thought you did. You check your email and see 
            that the team leader has scheduled an extra meeting to 
            match TEKS to test questions. This is the type of thing
            that could be quickly accomplished if everyone divided and
            conquered, but now a meeting has been called to waste everyone's
            time.
            """))
        action = input("Do you 'attend' the meeting or 'pretend' you didn't see the email?")

        if action == 'attend':
            print(dedent("""
                You do a poor job hiding your annoyance as you walk to the
                meeting room. But it probably pays off to be a team player
                in the long run. You keep one eye on the clock as your life
                slowly ticks by. By the end of the period you find yourself
                a litte more exhausted than before with almost nothing to show
                for the 50 minutes.
                """))
            tired += 1
            hopelessness += 1
            input("Press any key to continue")                        
            return "fourth_period"
        elif action == 'pretend':
            print(dedent("""
                You close the email, lock the door, turn off the lights, and
                lean back in your desk chair. Let the other fools waste their
                time, you are looking out for number one. Before long you
                find your mind drifting. You catch about 30 minutes of Z's
                before the bell rings signalling the end of the period wakes 
                you up.
                """))
            tired -= 1
            antisocial += 1
            input("Press any key to continue")                        
            return "fourth_period"
        else:
            print("Sorry, didn't catch that")
            return "third_period"


class FourthPeriod(Scene):
    def enter(self):
        print(dedent("""
            Your largest class of the day files in. By this point
            even the slackers have made it to school and most of the
            they aren't sleepy any more. Wish you could say the same.
            Things won't be quite as easy from now on.

            Knowing that, you wonder if you should change up your lesson
            somewhat.
            """))
        action = input("Do you change your lesson? 'yes' or 'no'")

        if action == 'yes':
            print(dedent("""
                You decide that since the lesson didn't really go over
                well in the first two periods you will make a few adjustments.
                """))
            topic = input("What topic do you teach the students about instead?")
            group = input("Perfect. What group size do you have them work in?")
            product = input("Got it. What do you have the students make?")
            print("You change the lesson on the fly.")
            print(f"You teach students about {topic}. Then they work in groups of {group} to create a {product}.")
            print("The lesson seems to be a big hit and you make it safely to lunch")
            input("Press any key to continue")                        
            return 'lunch'
        elif action == 'no':
            (print(dedent("""
                Why put in any extra effort. These kids wouldn't appreciate
                it anyways. You launch into the same 30 minute lecture that 
                you've been giving all day. Students are talking and generally
                messing around while you are trying to teach. You ignore it
                as you are past caring today. Unfortunately half-way through
                a fight breaks out when someone throws a punch at someone else.
                Students record it on there cellphones, and by the time the 
                hall monitor gets there to break it up there are bruises and
                bloody noses. Somehow you know that this is going to end up being
                your fault. 
                """)))
            return 'fired'
        else:
            print("yes or no?")
            return("fourth_period")


class Lunch(Scene):
    def enter(self):
        print("It is now time for lunch.")
        lunch = input("What did you pack for lunch?")
        if lunch == "nothing":
            print(dedent("""
                You forgot to pack your lunch. Unfortunately you have a
                rare condition where you need to eat at least every 4 hours
                or you will pass out and die.

                You pass out and die.
                """))
            return "fired"
        else:
            print(f"You eat the {lunch}. Tasty!")
            input("Press any key to continue.")                        
            return 'fifth_period'

class FifthPeriod(Scene):
    def enter(self):
        global antisocial
        global hopelessness
        print(dedent("""
            The bell rings and your fifth period files in. You have lasted
            to the second half of the day. Hopefully things will go nice and
            easy now, especially since you changed your lesson around and
            ate that delicious lunch. You take roll and begin to explain
            the activity to you class . . .

            BRRRRRIIIIINGGG BRRRRIIINNG BRRRRRRRRRIIIIIINNNG!!
            """))
        input("Press any key to continue.")
        print(dedent("""
            The fire alarm explodes in your ears and the students cheer.
            You grab the sign, wait for the students to file out and lock
            the door. When you reach the field your class lines up. Some
            of them are missing but you don't pretend to care. Next to you
            is another teacher from you department. She is a notorious gossip
            and you know that if you talk to her she will have something
            to complain about.
            """))
        action = input("Do you 'talk' to the teacher or 'ignore' her?")
        if action == 'talk':
            print(dedent("""
                On second thought, complaining is fun! She launches into a
                lengthy and circuitous narrative about a helicopter parent
                and you provide a sympathetic series of monosyllabic responses
                at appropriate intervals. It's not much of an interaction, but
                you feel a little less distant from other adults by the time the
                drill is over. On the otherhand, you are more depressed about
                the job as you remember a similar parent who was giving you
                trouble last week.
                """))
            antisocial -= 1
            hopelessness += 1
            input("Press any key to continue.")            
            return 'sixth_period'
        elif action == 'ignore':
            print(dedent("""
                You avoid eye contact and pretend to take roll for your students.
                Not that you have anything in particular against the other teacher,
                you just aren't in the mood to talk to anyone negative right now.
                You make a mental grocery list until the drill is over. Feeling a
                little less depressed, but more withdrawn, you head back up to the 
                classroom.
                """))
            antisocial += 1
            hopelessness -= 1
            input("Press any key to continue.")
            return 'sixth_period'        
        else:
            print("I didn't catch that.")
            return('fifth_period')
class SixthPeriod(Scene):
    def enter(self):
        print(dedent("""
            The rest of fifth period you struggle to make back the time
            lost in the fire drill. The class ends, students leave, and
            you stand at your door to greet your next class. Two minutes
            before the bell rings, your heart drops.

            Walking down the hallway is the principal with a tablet under
            her arm. You totally forgot that this week was the window for
            your annual observation. Hopefully the lesson changes that you
            made earlier will please the principal!
            """))
        input("Press any key to continue.")
        print(dedent("""
            She sits in the back of the room next to a group of unruly
            athletes who are never on task. They seem to be unaware that
            the principal, you know the person in charge of the entire school
            is sitting right next to them. You consider faking a reason to
            talk to the ringleader in the hall and bribing him. Or you could
            just ignore it pray that they behave better today.
            """))
        action = input("What do you do? 'pray' or 'talk' to the student?")
        if action == 'pray':
            print(dedent("""
                You take a moment to pray to Koalemos that the students behave
                well today. Unfortunately, Koalemos is the god of stupidity and
                you are stupid too. The boys are particularly rowdy today and
                continually talk over you, act out, and eventally one of them 
                sets fire to the carpet while trying to light a bong.

                The observation does not go well and the pricipal asks to see 
                you after school.
                """))
            return 'fired'
        elif action == 'talk':
            print(dedent("""
                Your career is too important to leave in the hands of random teenage
                assholes. Pretending to have a question about his assignment (which
                he didn't turn in), you lure the worst of the class clowns into the 
                hallway.

                What do you offer the student to entice better behavior?
                """))
            offer = input("'A' on the missing assignment or let him 'skip'?")
            if offer == 'A':
                print(dedent("""
                    You offer the student a free 100 on the paper he didn't turn in
                    if he will play along and pretend to be a good student. He agrees,
                    and for the most part keeps the bargin. His friends follow suit.
                    The lesson goes pretty well and you think that you most likely passed
                    the observation though the pricipal didn't seem to love the changes
                    that you made to the lesson.
                    """))
                input("Press any key to continue.")
                return 'seventh_period'
            elif offer == 'skip':
                print(dedent("""
                    You decide that it is too risky to keep that student in the class.
                    Also, on principle, you don't like giving out free grades. You tell
                    the student that you will mark him present for the class and he can
                    go whereever he likes for the period. He shrugs his shoulders and says
                    "whatever ******" before heading down the hall.

                    The lesson goes smoothly, but when you are finished the pricipal asks
                    where the student went at the beginning of the class. You make something
                    up but you don't think she buys it.
                    """))
                input("Press any key to continue.")
                return 'fired'
            else:
                print("Try one of the options I gave you")
                return 'sixth_period'        
        else:
            print("Sorry I didn't catch that.")
            return 'sixth_period'


class SeventhPeriod(Scene):
    def enter(self):
        print(dedent("""
            Finally it is time for the class that you hate the most.
            7th period. A worse collection of students could not have 
            been assembled if the counselors got together and worked on
            it on purpose. And maybe they did. You don't know what counselors
            do all day.
            """))
        input("Press any key to continue.")       
        print(dedent("""
            This bunch never does any homework but you have a suspiscion
            that instead they spend their nights dreaming up new ways to 
            make your life a living hell. Either that or it is the only 
            natural talent that any of them have. You use the same rule 
            you have at the bar during this period: never drink anything
            that you haven't had your eye on.
            """))
        input("Press any key to continue.")
        print(dedent("""
            But freedom is only 50 minutes away.  All that you have to do
            is get through the 50 minutes without murdering them and you 
            will have successfully completed the day. 

            Can you do it?
            """))
        input("Press any key to continue.")
        
        counter = 50
        action = input(f"{counter} minutes left. Do you murder them?")
        while counter > 5 and action == 'no':
            counter -= 5
            action = input(f"{counter} minutes left. Do you murder them?")
        
        if action != 'no':
            print("Well, that's understandable, but you will probably go to prison.")
            return 'fired'
        else:
            print(dedent("""
                With saint-like restraint you make it the entire 50 minutes with
                no murders! The bell rings, the students leave, and you feel a
                deep sense of relief and well-being.
                """))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("You made it through the day with out being fired. You won!")
        return 'finished'

class Map(object):

    scenes = {
        'wake_up': WakeUp(),
        'drive_in': DriveIn(),
        'first_period': FirstPeriod(),
        'second_period': SecondPeriod(),
        'third_period': ThirdPeriod(),
        'fourth_period': FourthPeriod(),
        'lunch': Lunch(),
        'fifth_period': FifthPeriod(),
        'sixth_period': SixthPeriod(),
        'seventh_period': SeventhPeriod(),
        'fired': Fired(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('wake_up')
a_game = Engine(a_map)
a_game.play()