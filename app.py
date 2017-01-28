""" Create a movies webpage """
from fresh_tomatoes import open_movies_page
from movie import Movie

# Movie definitions
BIG_LEBOWSKI = Movie(
    'The Big Lebowski',
    # pylint: disable=line-too-long
    'https://images-na.ssl-images-amazon.com/images/M/MV5BZTFjMjBiYzItNzU5YS00MjdiLWJkOTktNDQ3MTE3ZjY2YTY5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,665,1000_AL_.jpg',
    # pylint: enable=line-too-long
    'https://www.youtube.com/watch?v=cd-go0oBF4Y'
)


NO_COUNTRY = Movie(
    'No Country For Old Men',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_.jpg',#pylint: disable=line-too-long
    'https://www.youtube.com/watch?v=qnwNuG1ayno'
)


SNATCH = Movie(
    'Snatch',
    # pylint: disable=line-too-long
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX684_AL_.jpg',
    # pylint: enable=line-too-long
    'https://www.youtube.com/watch?v=ni4tEtuTccc'
)


THE_ORPHANAGE = Movie(
    'The Orphanage',
    # pylint: disable=line-too-long
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3MjE0NzQzMV5BMl5BanBnXkFtZTYwMzI0ODc4._V1_.jpg',
    # pylint: enable=line-too-long
    'https://www.youtube.com/watch?v=nUZQgqxIZ6s'
)


FIGHT_CLUB = Movie(
    'Fight Club',
    # pylint: disable=line-too-long
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMzc1YmU2ZjEtYWIwMC00ZjM3LWI0NTctMDVlNGQ3YmYwMzE5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY999_CR0,0,704,999_AL_.jpg',
    # pylint: enable=line-too-long
    'https://www.youtube.com/watch?v=SUXWAEX2jlg'
)


LOCK_STOCK = Movie(
    'Lock, Stock and Two Smoking Barrels',
    # pylint: disable=line-too-long
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
    # pylint: enable=line-too-long
    'https://www.youtube.com/watch?v=WoZ2kTlwKTk'
)
# END movie definitions

# put each movie in a list then call open_movies_page to create/open the webpage
MOVIES = [BIG_LEBOWSKI, NO_COUNTRY, SNATCH, THE_ORPHANAGE, FIGHT_CLUB, LOCK_STOCK]
open_movies_page(MOVIES)
