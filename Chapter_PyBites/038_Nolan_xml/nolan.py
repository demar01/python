import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501

#https://stackoverflow.com/questions/47876079/how-to-tell-flake8-to-ignore-comments noqa E501 will tell flake to ignore comments


def get_tree():
    """You probably want to use ET.fromstring"""
    return ET.fromstring(xmlstring) #<Element 'root' at 0x10b1ef9f0>

#[child for child in get_tree()]
#[child.attrib for child in get_tree()] this is a dictionary

#This will return a list of movie tittles
def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    return [child.attrib["title"] for child in get_tree()]

#To get the running times
def _get_runtime(element):
    return int(element.attrib["runtime"].split()[0])

# not need to do this [int(element.attrib["runtime"].split()[0]) for element in get_tree()] bc element/child will be passe in the next function 

def get_movie_longest_runtime():
    """Call get_tree again and return the movie title for the movie with the longest
       runtime in minutes, for latter consider adding a _get_runtime helper"""
    longest_movie = max([child for child in get_tree()],
                        key=_get_runtime) #this will return <Element 'movie' at 0x10b1efdb0>. 
    return longest_movie.attrib["title"] #We need to access title attribute to actually get title 


#Another interesting example
#https://github.com/terryjbates/data_wrangling_in_yolodb/blob/master/lesson_6/users.py

