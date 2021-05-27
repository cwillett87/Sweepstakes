from contestant import Contestant
import random
import user_interface


class Sweepstake:

    def __init__(self, name):
        self.name = name
        self.contestants = {}
        self.pre_registered_contestants()

    def pre_registered_contestants(self):
        self.contestants[1] = Contestant('Chris', 'Willett', '@gmail.com', 1)
        self.contestants[2] = Contestant('Corey', 'Jordan', '@gmail.com', 2)
        self.contestants[3] = Contestant('Leighton', 'Schmidt', '@gmail.com', 3)
        self.contestants[4] = Contestant('Ricky', 'Bobby', '@gmail.com', 4)

    def register_contestant(self):
        user_interface.registration()
        reg_number = input(user_interface.contestant_registration_number())
        first_name = input(user_interface.contestant_first_name())
        last_name = input(user_interface.contestant_last_name())
        email = input(user_interface.contestant_email())
        self.contestants[reg_number] = Contestant(first_name, last_name, email, reg_number)
        # dependency injection works no matter what or how many contestants are registered
    def registration(self):
        user_interface.last_registration_number_used(self.contestants)
        self.register_contestant()
        will_proceed = True
        while will_proceed:
            user_option = user_interface.register_another_contestant()
            if user_option == 1:  #if yes continue to register
                user_interface.last_registration_number_used(self.contestants)
                self.register_contestant()
            elif user_option == 2:
                user_interface.show_contestants(self.contestants)
                break
            else:
                will_proceed = False

    def pick_winner(self):
        #randomly pick winner and return contestant
        contestants = list(self.contestants.items())
        winner = random.choice(contestants)
        contestant = list(winner)
        self.print_contestant_info(contestant)
        return winner

    def print_contestant_info(self, contestant): # dependency injection works no matter which manager is used
        #def print method in user interface and method here
        user_interface.show_winner_info(contestant)
