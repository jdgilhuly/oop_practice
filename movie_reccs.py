# build a movie reccomendation system
# users
    # rate movies
    # get reccs

# recommendation system
    # return reccs
    # get reccs for users

# design movies



class User:
    # Iteracts with Rec System and Creates Recommendation Scores
    pass

class RecommendationSystem:
    pass

import enum
class Genre(enum.Enum):
    HORROR = 1
    COMEDY = 2
    THRILLER = 3
    # ... add more

class Movie:
    # instance of movie with relevant info
    def __init__(self, movie_name, movie_actors, movie_genre):
        self.movie_name = movie_name
        self.movie_actors = movie_actors
        self.movie_genre = movie_genre

    def get_movie_name(self):
        return self.movie_name




class Feed:
    # Returns Ordered Recommendations
    pass

class Recommendation(Movie):
    # Takes in Movie and has recommendation score attached
    pass