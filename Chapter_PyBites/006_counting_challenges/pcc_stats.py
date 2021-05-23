from collections import Counter, namedtuple
import os 
import re 
import urllib.request

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()


Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.
    
    Lowercase these directory names and return them as a generator.
    
    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>
    
    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True
    
    => Here you would return 03/mridubhatnagar (lowercased!)
    followed by 03/aleksandarknezevic
    """
    with open(tempfile, "r") as f:
        for line in f:
            #to do nothing with the lines that end with false, just continue. 
            if line.endswith(",False\n"):
                continue
            yield line


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()
    for file in gen_files():
        challenge, user = re.search(r"(.*?)/(.*?),", file).groups()
        if user in IGNORE:
            continue
    users[user] += 1
    popular_challenges[challenge] += 1
    return Stats(users.most_common(1)[0][0],*popular_challenges.most_common(1))
    #return Stats(users.most_common(1)[0][0], popular_challenges.most_common(1)[0]) #manual unpacking will also work