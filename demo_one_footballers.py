class footballers: #super_class
    profession = "Footballers" #Class variable or static variable

    def __init__(self, name, age, position, country, club):
        self.name = name # Instance Variables
        self.age = age
        self.position = position
        self.country = country
        self.club = club

    def player_data(self):
        print(f"Profession:{footballers.profession}\nName: {self.name}\nAge:{self.age}\nPosition:{self.position}\nCountry:{self.country}\nClub:{self.club}")


class career_stats(footballers): #career_stats is footballers inheritance
    def __init__(self, name, age, position, country, club, match_played, goals_scored):
        super().__init__(name, age, position, country, club)
        self.match_played = match_played
        self.goals_scored = goals_scored
    
    def avg_goal_per_match(self): #Average Goals
        return round(self.goals_scored/self.match_played, 2)

    def player_records(self):
        super().player_data()
        print(f"Match Played:{self.match_played}\nGoals Scored:{self.goals_scored}\nGoals Per Match:{self.avg_goal_per_match()}\n") 



messi = career_stats("Lionel Messi", 37, "CF", "Argentina", "Inter Miami", 904, 735)

ronaldo = career_stats("Cristiano Ronaldo", 39, "CF", "Portugal", "Al-Nasser", 1230, 895)

suarez = career_stats("Luis Suarez", 37, "CF", "Uruguay", "Inter Miami",630,480)

neymar = career_stats("Neymar Jr.", 32, "CF", "Brazil", "Al Hilal SFC", 763, 476 ) #New Player Added

messi.player_records()
ronaldo.player_records()
suarez.player_records()
neymar.player_records()
