class Movie:

    """
    "The Godfather":{"Released_Year":"1972","Runtime":
    "175 min","Genre":"Crime, Drama",
    "IMDB_Rating":9.2,"Overview":
    "An organized crime dynasty's aging patriarch 
    transfers control of his clandestine empire 
    to his reluctant son.",
    "Meta_score":100.0,"Director":"Francis Ford Coppola",
    "Star1":"Marlon Brando","Star2":"Al Pacino","Star3":"James Caan",
    "Star4":"Diane Keaton","No_of_Votes":1620367,
    "Gross":"134,966,411"}
    """

    def __init__(self, data):
        self.data = data


    def get_actor_names(self):
        stars = [self.data['Star1'], self.data['Star2'], self.data['Star3'], self.data['Star4']]
        return stars


    def get_time(self):
        runtime = self.data['Runtime']
        return runtime


    def description(self):
        text = f'Film Director is {self.data['Director']}. It published in {self.data['Released_Year']}. Main stars are {', '.join(self.get_actor_names())}.'
        return text

class Actor:

    def __init__(self, data):
            self.data = data


    def about_actor(self, actor_name):
        films = []
        for name, data in self.data.items():
            movie = Movie(data)
            if actor_name in movie.get_actor_names():
                films.append(name)
        return films


    def film_numbers(self, actor_name):
        count = len(self.about_actor(actor_name))
        return count


    def average_rating(self, actor_name):
        films = self.about_actor(actor_name)
        _sum = 0
        for val in films:
            _sum += self.data[val]["IMDB_Rating"]

        average = _sum / len(films)
        return average


    def popular_genre(self, actor_name):
        genre = {}
        films = self.about_actor(actor_name)

        for val in films:
            if self.data[val]['Genre'] not in genre:
                genre[self.data[val]['Genre']] = 1
            else:
                genre[self.data[val]['Genre']] += 1

        sorted_dict = dict(sorted(genre.items(), key = lambda x: x[1], reverse = True))
        first_key = next(iter(sorted_dict))

        return first_key

    def director_name(self, actor_name):
        count = {}
        films = self.about_actor(actor_name)

        for val in films: 
            director = self.data[val]["Director"]
            if director not in count:
                count[director] = 1
            else:
                count[director] += 1
        sorted_dict = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
        first_key = next(iter(sorted_dict))
        
        return first_key


    def most_frequent_actor(self, actor_name):
        count = {}

        films = self.about_actor(actor_name)

        for film in films:
            movie = Movie(self.data[film])
            for actor in movie.get_actor_names():
                if actor_name == actor:
                    continue

                count[actor] = count.get(actor, 0) + 1

        return max(count, key = count.get)


    def description(self, actor_name):
            count = self.film_numbers(actor_name)

            average = self.average_rating(actor_name)

            text = f'Actor\'s name is {actor_name}. Acted in {count} films. The average rating of the movies is {average}.'

            return text

        
