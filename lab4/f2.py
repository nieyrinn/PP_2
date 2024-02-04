movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def is_high_rated(movie):
    return movie["imdb"] > 5.5

def get_high_rated_movies(movies):
    return [movie for movie in movies if is_high_rated(movie)]

def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def calculate_average_rating(movies):
    if not movies:
        return 0.0
    total_ratings = sum(movie["imdb"] for movie in movies)
    return total_ratings / len(movies)

def calculate_average_rating_by_category(movies, category):
    category_movies = get_movies_by_category(movies, category)
    return calculate_average_rating(category_movies)

print(is_high_rated(movies[0]))  # True

print(get_high_rated_movies(movies))

print(get_movies_by_category(movies, "Romance"))

print(calculate_average_rating(movies))

print(calculate_average_rating_by_category(movies, "Romance"))
