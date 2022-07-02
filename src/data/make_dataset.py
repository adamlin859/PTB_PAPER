import pandas as pd



def get_data(location, file_name):
    path = location + file_name
    data = pd.read_csv(path)
    data.rename(columns={"StudyID":"STUDYID"}, inplace=True)
    return data