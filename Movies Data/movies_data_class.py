import json
from helper import Movie, Actor
PATH = r'C:\Users\user\Desktop\mini-projects\Movies Data\imdb_top_999.json'

with open(PATH, "r") as f:
    data = json.load(f)

TO_DELETE = ["No_of_Votes", "Overview", "Meta_score"]

for kino in data.keys():
    for k in TO_DELETE:
        del data[kino][k]

    data[kino]["Name"] = kino

print(data)


movie_name = input("Enter movie name: ")
movie = Movie(data[movie_name])

print(movie.get_actor_names())
print(movie.get_time())
print(movie.description())

actor = Actor(data)
actor_name = input("Enter actor name: ")
print(actor.about_actor(actor_name))
print(actor.film_numbers(actor_name))
print(actor.average_rating(actor_name))
print(actor.popular_genre(actor_name))
print(actor.director_name(actor_name))
print(actor.most_frequent_actor(actor_name))
print(actor.description(actor_name))

