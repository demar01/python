import json

# See test_ombd movies() function. This function retrieves and generates a json (list of PosixPath with json files). We use get_movie_data to serialize Json

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies_list = []
    for f in files:
        with open(f) as fp:
            movies_list.append(json.load(fp))
    return movies_list

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return [m['Title'] for m in movies_list if "Comedy" in m["Genre"].split(", ")]

#transform this for loop into a lambda function to get title of movie with more nominations
#[ int(m["Awards"].split(" & ")[-1].replace(" nominations.", "")) for m in movies_list]

def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    return max(movies,
               key=lambda m: int(m["Awards"].split(" & ")[-1].replace(" nominations.", ""))
               )["Title"]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies,
               key=lambda m: int(m["Runtime"].replace(" min", ""))
               )["Title"]