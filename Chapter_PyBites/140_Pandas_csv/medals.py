import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    df = pd.read_csv(data)
    # df.shape (31165, 9)
    gr = df.groupby(by=["Gender", "Athlete"]).count() #[22767 rows x 7 columns] 
    m, w = gr.loc["Men"]["Medal"], gr.loc["Women"]["Medal"] #it would not work the other way around
    return {
        m.idxmax(): m.max(),
        w.idxmax(): w.max()
    }
    #{'PHELPS, Michael': 22, 'LATYNINA, Larisa': 18}