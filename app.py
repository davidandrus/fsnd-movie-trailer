from fresh_tomatoes import open_movies_page
from movie import Movie


big_lebowski = Movie(
    'The Big Lebowski',
    ('https://images-na.ssl-images-amazon.com/images/M/'
    'MV5BZTFjMjBiYzItNzU5YS00MjdiLWJkOTktNDQ3MTE3ZjY2Y'
    'TY5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,665,1000_AL_.jpg'),
    'https://www.youtube.com/watch?v=cd-go0oBF4Y'
)


no_country = Movie(
    'No Country For Old Men',
    ('https://images-na.ssl-images-amazon.com/images/M'
    '/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_.jpg'),
    'https://www.youtube.com/watch?v=qnwNuG1ayno'
)


snatch = Movie(
    'Snatch',
    ('https://images-na.ssl-images-amazon.com/images/M'
    '/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5'
    'MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX684_AL_.jpg'),
    'https://www.youtube.com/watch?v=ni4tEtuTccc'
)


the_orphanage = Movie(
    'The Orphanage',
    ('https://images-na.ssl-images-amazon.com/images/M/'
    'MV5BMTc3MjE0NzQzMV5BMl5BanBnXkFtZTYwMzI0ODc4._V1_.jpg'),
    'https://www.youtube.com/watch?v=nUZQgqxIZ6s'
)


fight_club = Movie(
    'Fight Club',
    ('https://images-na.ssl-images-amazon.com/images/M/'
    'MV5BMzc1YmU2ZjEtYWIwMC00ZjM3LWI0NTctMDVlNGQ3YmYwMz'
    'E5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY999_CR0,0,704,999_AL_.jpg'),
    'https://www.youtube.com/watch?v=SUXWAEX2jlg'
)


lock_stock = Movie(
    'Lock, Stock and Two Smoking Barrels',
    ('https://images-na.ssl-images-amazon.com/images/M/'
    'MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMm'
    'M4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg'),
    'https://www.youtube.com/watch?v=WoZ2kTlwKTk'
)


movies = [big_lebowski, no_country, snatch, the_orphanage, fight_club, lock_stock]
open_movies_page(movies)
