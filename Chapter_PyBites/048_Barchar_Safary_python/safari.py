import os 
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

def create_chart():
    with open(SAFARI_LOGS) as f:
        day = ""
        day_result = []
        for line in f.readlines():
            if not day: #this if and elif are neccesary to print to same line 
                day = line[:5]
            elif day != line[:5]:
                if day_result:
                    print(day, "".join(day_result)) #this is really what is going to print it out to screen from the appended result of the previous line   
                day = line[:5]
                day_result = []
            if "DEBUG    - " not in line:
                if "python" in line.lower():
                    last_book = PY_BOOK
                else:
                    last_book = OTHER_BOOK
            elif "- sending to slack channel" in line:
                day_result.append(last_book)
        print(day, "".join(day_result)) #this is neccesary to print last line with dat 02-22

