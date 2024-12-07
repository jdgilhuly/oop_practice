# build a movie reccomendation system
# users
    # rate movies
    # get reccs

# recommendation system
    # return reccs
    # get reccs for users

# design movies

import heapq


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

    def get_movie_genre(self):
        return self.movie_genre

    def get_movie_name(self):
        return self.movie_name

    def get_movie_actors(self):
        return self.movie_actors


class Recommendation(Movie):
    # Takes in Movie and has recommendation score attached
    def __init__(self, rating, name, actors, genre):
        super().__init__(name, actors, genre)
        self.rating = [rating]

    def get_movie_rating(self):
        return sum(self.rating) // len(self.rating)

    def add_movie_rating(self, new_rating):
        self.rating.append(new_rating)
        return sum(self.rating) // len(self.rating)


class RecommendationSystem:
    def __init__(self, movies):
        self.recommendations = self.__get_most_recent_recc(movies)

    def __get_most_recent_recc(self, movies):
        recs = []
        for movie in movies:
            heapq.heappush(recs, (-movie.get_movie_rating(), movie))
        return recs

    def return_reccomendation(self):
        return self.recommendations


class Feed:
    def __init__(self):
        self.rec_system = RecommendationSystem([])

    def show_reccs(self):
        print(self.rec_system.return_reccomendation())

    
