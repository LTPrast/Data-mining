
import pandas as pd

df = pd.read_csv('ODI-2022.csv', sep=";")
olddf= pd.read_csv('ODI-2022.csv', sep=";")
df.head()


#clean this monstrocity

df.rename(columns={'Tijdstempel':'Timestamp', 'What programme are you in?':'Programme',
       'Have you taken a course on machine learning?':'ML exp.',
       'Have you taken a course on information retrieval?':'IR exp.',
       'Have you taken a course on statistics?':'Stats exp.',
       'Have you taken a course on databases?':'DB exp.', 'What is your gender?':'Gender',
       'Chocolate makes you.....':'Chocolate', 'When is your birthday (date)?':'DOB',
       'Number of neighbors sitting around you?':'Neighbors', 'Did you stand up?':'Standup',
       'What is your stress level (0-100)?':'Stress',
       'You can get 100 euros if you win a local DM competition, or we don’t hold any competitions and I give everyone some money (not the same amount!). How much do you think you would deserve then? ':'money',
       'Give a random number':'rn', 'Time you went to be Yesterday':'sleeptime',
       'What makes a good day for you (1)?':'good day 1',
       'What makes a good day for you (2)?':'good day 2'})
#Clean the programme column


df['What programme are you in?'].unique()  #get distinct value in the program column



df.loc[df['What programme are you in?'].str.contains('bio', case=False), 'What programme are you in?'] = 'Biomedical/informatics'

df.loc[df['What programme are you in?'].str.contains('artificial', case=False), 'What programme are you in?'] = 'Artificial Intelligence'
df.loc[df['What programme are you in?'].str.contains('AI', case=True), 'What programme are you in?'] = 'Artificial Intelligence'

df.loc[df['What programme are you in?'].str.contains('computational', case=False), 'What programme are you in?'] = 'Computational Science'
df.loc[df['What programme are you in?'].str.contains('CLS', case=True), 'What programme are you in?'] = 'Computational Science'

df.loc[df['What programme are you in?'].str.contains('computer', case=False), 'What programme are you in?'] = 'Computer Science'
df.loc[df['What programme are you in?'].str.contains('CS', case=True), 'What programme are you in?'] = 'Computer Science'

df.loc[df['What programme are you in?'].str.contains('econometrics|e&or|eor', case=False), 'What programme are you in?'] = 'Econometrics'


df.loc[df['What programme are you in?'].str.contains('finance|fin', case=False), 'What programme are you in?'] = 'Finance'

df.loc[df['What programme are you in?'].str.contains('qrm|quant', case=False), 'What programme are you in?'] = 'QRM'

df.loc[df['What programme are you in?'].str.contains('business', case=False), 'What programme are you in?'] = 'Business Analytics'
df.loc[df['What programme are you in?'].str.contains('BA', case=True), 'What programme are you in?'] = 'Business Analytics'


df.loc[df['What programme are you in?'].str.contains('ds|data science', case=False), 'What programme are you in?'] = 'Data Science'

df.loc[~df['What programme are you in?'].str.contains('artificial|comput|econometrics|finance|qrm|business|bio|data science|human', case=False), 'What programme are you in?'] = 'Other'


#Clean the ML column

df.loc[df['Have you taken a course on machine learning?'].str.contains('yes', case=False), 'Have you taken a course on machine learning?'] = '1'
df.loc[~df['Have you taken a course on machine learning?'].str.contains('unknown|1', case=False), 'Have you taken a course on machine learning?'] ='0'
df.loc[df['Have you taken a course on machine learning?'].str.contains('unknown', case=False), 'Have you taken a course on machine learning?'] =None


#Clean the IR column

df.loc[df['Have you taken a course on information retrieval?'].str.contains('unknown', case=False), 'Have you taken a course on information retrieval?'] = None

#Clean the stats column

df.loc[df['Have you taken a course on statistics?'].str.contains('mu', case=False), 'Have you taken a course on statistics?'] = '0'
df.loc[df['Have you taken a course on statistics?'].str.contains('sigma', case=False), 'Have you taken a course on statistics?'] = '1'
df.loc[~df['Have you taken a course on statistics?'].str.contains('0|1', case=False), 'Have you taken a course on statistics?'] = None


#Clean the stats column

df.loc[df['Have you taken a course on databases?'].str.contains('nee', case=False), 'Have you taken a course on databases?'] = '0'
df.loc[df['Have you taken a course on databases?'].str.contains('ja', case=False), 'Have you taken a course on databases?'] = '1'
df.loc[~df['Have you taken a course on databases?'].str.contains('1|0', case=False), 'Have you taken a course on databases?'] = None

#Clean the neighbours column

df.loc[ df['Number of neighbors sitting around you?'].str.contains('a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|q|r|s|t|u|v|w|x|y|z|>|<', case=False) , 'Number of neighbors sitting around you?'] = '0'

df['Number of neighbors sitting around you?'] = df['Number of neighbors sitting around you?'].apply(lambda x: int(x) if int(x)>=0 else 0)



#Clean the standup column

df.loc[df['Did you stand up?'].str.contains('yes', case=False), 'Did you stand up?'] = '1'
df.loc[~df['Did you stand up?'].str.contains('unknown|1', case=False), 'Did you stand up?'] ='0'
df.loc[df['Did you stand up?'].str.contains('unknown', case=False), 'Did you stand up?'] =None


#Clean the stress column

df.loc[ df['What is your stress level (0-100)?'].str.contains('-|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|q|r|s|t|u|v|w|x|y|z', case=False) , 'What is your stress level (0-100)?'] = '42.42'

df['What is your stress level (0-100)?'] = df['What is your stress level (0-100)?'].apply(lambda x: float(x) if float(x)>=0 else 0)

df['What is your stress level (0-100)?'] = df['What is your stress level (0-100)?'].apply(lambda x: float(x) if float(x)<=100 else 100)
df['What is your stress level (0-100)?'] = df['What is your stress level (0-100)?'].apply(lambda x: None if x==42.42 else x)


#C lean birthday

#df.loc[~df['When is your birthday (date)?'].str.contains('9|8|7|6|5|4|3|2|1|0', case=False), 'When is your birthday (date)?'] = '01-01-2000'

df.loc[df['When is your birthday (date)?'].str.contains('a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|q|r|s|t|u|v|w|x|y|z', case=False), 'When is your birthday (date)?'] = '01-01-2100'
df.loc[~df['When is your birthday (date)?'].str.contains('/|-|.'), 'When is your birthday (date)?'] = '01-01-2100'

df['When is your birthday (date)?'] = df['When is your birthday (date)?'].apply(lambda x: x if len(x)>9 else '01-01-2100')

df.loc[df['When is your birthday (date)?'].str.contains('1057', case=False), 'When is your birthday (date)?'] = '01-01-2100'
df.loc[df['When is your birthday (date)?'].str.contains('01-01-2100', case=False), 'When is your birthday (date)?'] = None


df['When is your birthday (date)?'] = pd.to_datetime(df['When is your birthday (date)?'])



col_name = 'You can get 100 euros if you win a local DM competition, or we don’t hold any competitions and I give everyone some money (not the same amount!). How much do you think you would deserve then? '

df[col_name] = df[col_name].apply(lambda x: "invalid" if str(x) == 'nan' else x)






df.loc[df[col_name].str.contains(',|€|-|/|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|q|r|s|t|u|v|w|x|y|z', case=False), col_name] = 'invalid'

import math
df[col_name] = df[col_name].apply(lambda x: None if x =='invalid' else int(math.floor(float(x))))


df['When is your birthday (date)?'] = df['When is your birthday (date)?'].dt.date



df.agg(
    {
       "Have you taken a course on statistics?": ["min", "max", "median","mean", "skew"],
            "What is your stress level (0-100)?": ["min", "max", "median", "mean","skew"],
        }
    )

df["What is your gender?"].value_counts()
df['What programme are you in?'].value_counts()

df[["What is your gender?", "What is your stress level (0-100)?"]].groupby("What is your gender?").mean()

df[['What programme are you in?', "What is your stress level (0-100)?"]].groupby('What programme are you in?').mean()

df[['What programme are you in?', "You can get 100 euros if you win a local DM competition, or we don’t hold any competitions and I give everyone some money (not the same amount!). How much do you think you would deserve then? "]].groupby('What programme are you in?').median()




df[['Have you taken a course on machine learning?', "What is your stress level (0-100)?"]].groupby('Have you taken a course on machine learning?').mean()

df.groupby(['Have you taken a course on machine learning?','Have you taken a course on databases?','Have you taken a course on information retrieval?', 'Have you taken a course on statistics?'])["What is your stress level (0-100)?"].mean()


