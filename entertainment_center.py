import media
import fresh_tomatoes


gone_with_the_wind = media.Movie("Gone with the Wind",
    "A 1939 American epic historical romance film adapted from Margaret Mitchell's 1936 novel Gone with the Wind.",
    "https://upload.wikimedia.org/wikipedia/commons/2/27/Poster_-_Gone_With_the_Wind_01.jpg",
    "https://www.youtube.com/watch?v=0dTsfsr6-X8")

the_matrix = media.Movie("The Matrix",
    'A dystopian future in which reality as perceived by most humans is actually a simulated reality called "the Matrix", created by sentient machines to subdue the human population, while their bodies heat and electrical activity are used as an energy source.',
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")

fight_club = media.Movie("Fight Club",
    'An "everyman" who is discontented with his white-collar job forms a "fight club" with soap maker Tyler Durden and they are joined by men who also want to fight recreationally. ',
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=BdJKm16Co6M")

movies = [gone_with_the_wind, the_matrix, fight_club]
fresh_tomatoes.open_movies_page(movies)