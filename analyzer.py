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

# TODO: method is working, but it is going to be a problem for big data set, i need to look for a better way to reduce complexity
def top_10_certified_fresh(movie_list):
    movie_list_refactored = refactor_movies(movie_list)
    certified = [m for m in movie_list_refactored if m["certified_fresh"]]
    sorted_movies = sorted(certified, key=lambda m: m["rating"], reverse=True)
    return sorted_movies[:10]

if __name__ == '__main__':
    top_10_movies = top_10_certified_fresh(
        movie_list=[
            [1, 9.0, "Interstellar", True],
            [2, 8.5, "Fast and the Furious", True],
            [7, 10.5, "Fast and the Furious V5", True],
            [3, 17.2, "The Matrix", False],
            [4, 9.5, "Inception", True],
        ]
    )
    print(top_10_movies)