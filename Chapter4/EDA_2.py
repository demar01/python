
import os
import pandas as pd
import numpy as np
import opendatasets as od


od.download('stackoverflow-developer-survey-2020')
os.listdir('stackoverflow-developer-survey-2020')
survey_raw_df = pd.read_csv('stackoverflow-developer-survey-2020/survey_results_public.csv')
#print(survey_raw_df.columns)
#print(survey_raw_df.shape)
print(survey_raw_df.describe())
print(survey_raw_df.info())
# The dataset contains over 64461 responses to 60 questions 

schema_fname = 'stackoverflow-developer-survey-2020/survey_results_schema.csv'
schema_raw = pd.read_csv(schema_fname, index_col='Column').QuestionText
#We can load it as Pandas Series with Column as the index and the QuestionText as the value.

selected_columns = [
    # Demographics
    'Country',
    'Age',
    'Gender',
    'EdLevel',
    'UndergradMajor',
    # Programming experience
    'Hobbyist',
    'Age1stCode',
    'YearsCode',
    'YearsCodePro',
    'LanguageWorkedWith',
    'LanguageDesireNextYear',
    'NEWLearn',
    'NEWStuck',
    # Employment
    'Employment',
    'DevType',
    'WorkWeekHrs',
    'JobSat',
    'JobFactors',
    'NEWOvertime',
    'NEWEdImpt'
]
print(len(selected_columns))


survey_df = survey_raw_df[selected_columns].copy()
schema = schema_raw[selected_columns]

survey_df['Age1stCode'] = pd.to_numeric(survey_df.Age1stCode, errors='coerce')
survey_df['YearsCode'] = pd.to_numeric(survey_df.YearsCode, errors='coerce')
survey_df['YearsCodePro'] = pd.to_numeric(survey_df.YearsCodePro, errors='coerce')

survey_df.drop(survey_df[survey_df.Age < 10].index, inplace=True)
survey_df.drop(survey_df[survey_df.Age > 100].index, inplace=True)
survey_df.drop(survey_df[survey_df.WorkWeekHrs > 140].index, inplace=True)
print(survey_df['Gender'].value_counts())
