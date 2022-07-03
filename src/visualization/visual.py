import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os 
import sys 
from src.data.make_dataset import *

BASE_PATH = "../data/raw/"

# get patient id dictionary
def patient_number_heatmap():
    files = os.listdir(BASE_PATH)
    patient_id_dict = {}
    for f in files:
        data = get_data(BASE_PATH, f)    
        patient_id_dict[f] = data.STUDYID.unique()
    return patient_id_dict

# get the matrix for heatmap
def get_confusion_matrix(patient_id_dict):
    csv_files = patient_id_dict.keys()
    n = len(csv_files)

    patient_heatmap = np.zeros((n, n))
    for i, v in enumerate(csv_files):
        for j, k in enumerate(csv_files):
            s1 = set(patient_id_dict[v])
            s2 = set(patient_id_dict[k])

            patient_heatmap[i][j] = len(s1.intersection(s2))
            if len(s1.intersection(s2)) == 0:
                print(v, k)
    return patient_heatmap

# save the heatmap to the report 
def plot_patient_number_heatmap():
    feature_list = pd.read_csv("../data/features/feature_list_v2.csv") 
    feature_list = [x.lower() for x in (feature_list.File + ".csv").unique()]
    patient_id_dict = patient_number_heatmap(feature_list)
    
    h = get_confusion_matrix(patient_id_dict)
    sns.heatmap(h, xticklabels=patient_id_dict.keys(), yticklabels=patient_id_dict.keys())
    fig = plt.gcf()
    plt.tight_layout()
    fig.set_size_inches(15, 15)
    fig.savefig('../reports/figures/patient_id_heatmap.png', dpi=300)


