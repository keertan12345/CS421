# Creating a Collection, Movie, Song, and People class
class Collection:
    def __init__(self, movies):
        self.movies = movies
        
    def __repr__(self):
        return 'Collection(movies=%s)' % (self.movies)
        
    def __str__(self):
        return 'Collection(movies=%s)' % (self.movies)

class Movie:
    def __init__(self, title, songs, people):
        self.title = title
        self.songs = songs
        self.people = people
        
    def __repr__(self):
        return 'Movie(title=%s, songs=%s, people=%s)' % (self.title, self.songs, self.people)
        
    def __str__(self):
        return 'Movie(title=%s, songs=%s, people=%s)' % (self.title, self.songs, self.people)
    
class Song:
    def __init__(self, name, singer, movie):
        self.name = name
        self.singer = singer
        self.movie = movie
        
    def __repr__(self):
        return 'Song(name=%s, singer=%s, movie=%s)' % (self.name, self.singer, self.movie)
        
    def __str__(self):
        return 'Song(name=%s)' % (self.name)

class People:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie
  
    def __repr__(self):  
       return 'People(name=%s, movie=%s)' % (self.name, self.movie)
    
    def __str__(self):  
       return 'People(name=%s)' % (self.name)
       
# Creating elements for Toy Story 4
person_1 = People("Tom Hanks", "Toy Story 4")
person_2 = People("Tim Allen", "Toy Story 4")
person_3 = People("Keanu Reeves", "Toy Story 4")

Toy_story_cast = [person_1, person_2, person_3]

song_1 = Song("You've Got a Friend in Me", "shichao liu", "Toy Story 4")
song_2 = Song("Operation Pull Toy", "Randy Newman", "Toy Story 4")

Toy_story_songs = [song_1, song_2]

Toy_story = Movie("Toy Story 4", Toy_story_songs, Toy_story_cast)


# Creating elements for Soul by Pixar
person_4 = People("Daveed Diggs", "Soul")
person_5 = People("Jamie Foxx", "Soul")
person_6 = People("Tina Fey", "Soul")

Soul_cast = [person_4, person_5, person_6]

song_3 = ("Let Your Soul Glow", "Jon Batiste", "Soul")
song_4 = ("Lost Soul", "Trent Reznor", "Soul")

Soul_songs = [song_3, song_4]

Soul = Movie("Soul", Soul_songs, Soul_cast)

# Creating a list for movies
Movie_list = [Toy_story, Soul]

Movie_collection = Collection(Movie_list)
print(Movie_collection)
