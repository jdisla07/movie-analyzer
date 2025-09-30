def refactor_movies(movie_list):
    return [
        {
            "id": row[0],
            "rating": row[1],
            "title": row[2],
            "certified_fresh": row[3],
        }
        for row in movie_list
    ]

if __name__ == '__main__':
    refactored_movies = refactor_movies(
        movie_list=[
            [1, 9.0, "Interstellar", True],
            [2, 8.5, "Fast and the Furious", True],
            [3, 7.2, "The Matrix", False],
            [4, 9.5, "Inception", True],
        ]
    )
    print(refactored_movies)