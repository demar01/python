from datetime import date
import os
from pathlib import Path
import pickle
from typing import Sequence, NamedTuple
from urllib.request import urlretrieve

#create a file with pathlib
TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / 'input.pkl'
PICKLE_OUTFILE = TMP / 'output.pkl'
#PICKLE_INFILE is a PosixPath object, with methods such as PICKLE_INFILE.cwd(), PICKLE_INFILE.exists(), PICKLE_INFILE.as_posix()

class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


def download_pickle_file():
    """download a pickle file we created with a
       list of namedtuples
    """
    urlretrieve(f'{S3}/bite317.pkl', PICKLE_INFILE)


def deserialize(pkl_file: Path = PICKLE_INFILE) -> Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    #open a file with pathlib
    with pkl_file.open('rb') as f:
        return pickle.load(f)

def serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = None) -> None:
    """Save the data passed in to the pickle file passed in"""
    if data is None:
        data = deserialize()

    with pkl_file.open('wb') as f:
        pickle.dump(data, f)


# download_pickle_file()
# print(deserialize())