class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_name(self):
        return self.name

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        percentage = self.get_wins() / ( self.get_wins() + self.get_losses() )
        return percentage
    # TODO: Define print_standing()
    def print_standing(self):
        x = self.get_win_percentage()
        print(f'Win percentage: {x:.2f}')
        if x > 0.5:
             print(f'Congratulations, Team {self.get_name()} has a winning average!')
        else:
            print(f'Team {self.get_name()} has a losing average.')



if __name__ == "__main__":
    team = Team()
   
    user_name = input()
    user_wins = int(input())
    user_losses = int(input())
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()
