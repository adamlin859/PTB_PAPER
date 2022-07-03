import pandas as pd
import os



def get_data(location, file_name):
    path = os.path.join(location, file_name)
    data = pd.read_csv(path)
    data.rename(columns={"StudyID":"STUDYID"}, inplace=True)
    return data

def get_patient_number_diagram(BASE_PATH):
    patient_num = {}
    pout = get_data(BASE_PATH, "pregnancy_outcomes.csv")
    
    # number of total participant 
    patient_num["Total Participant"] = pout.shape[0]

    # number of patient no pregancy outcome is recorded
    counts = pout[pout.TYPE_CA.isin(["dddSB", "iFTSB", "iPTSB", "sFTSB", "sPTSB"])]
    patient_num["Stillbirths"] = counts.shape[0]

    # number of missing pregnancy outcome information 
    count = pout[pout.TYPE_CA.isin(["dPTLB", "dddLB", "ddddd"])]
    patient_num["Missing outcome"]  = count.shape[0]

    # number of initial study cohort 
    count = pout[pout.TYPE_CA.isin(["dFTLB", "iFTLB", "iPTLB", "sFTLB", "sPTLB"])]
    patient_num["Participants"] = count.shape[0]


    #########################################################################
    # number of preterm births and full term 
    count = pout[pout.TYPE_CA.isin(["iPTLB", "sPTLB"])]
    patient_num["Preterm"] = count.shape[0]

    count = pout[pout.TYPE_CA.isin(["dFTLB", "iFTLB", "sFTLB"])]
    patient_num["Fullterm"] = count.shape[0]

    #########################################################################
    # number of preterm births and full term in placental analytes
    count = pout[pout.TYPE_CA.isin(["iPTLB", "sPTLB"])]
    placental_analytes = get_data(BASE_PATH, "placental_analytes.csv")

    patient_num["Preterm_PA"] = count.STUDYID.isin(placental_analytes.STUDYID).sum()

    count = pout[pout.TYPE_CA.isin(["iPTLB"])]
    placental_analytes = get_data(BASE_PATH, "placental_analytes.csv")

    patient_num["Preterm_iPTLB"] = count.STUDYID.isin(placental_analytes.STUDYID).sum()

    count = pout[pout.TYPE_CA.isin(["sPTLB"])]
    placental_analytes = get_data(BASE_PATH, "placental_analytes.csv")

    patient_num["Preterm_sPTLB"] = count.STUDYID.isin(placental_analytes.STUDYID).sum()


    count = pout[pout.TYPE_CA.isin(["dFTLB", "iFTLB", "sFTLB"])]
    patient_num["Fullterm_PA"] = count.STUDYID.isin(placental_analytes.STUDYID).sum()


    #########################################################################
    # number of iPTLB
    count = pout[pout.TYPE_CA.isin(["iPTLB"])]
    patient_num["iPTLB"] = count.shape[0]

    # number of iPTLB in 6 - 13_6 weeks 
    iPTLB = pout[pout.TYPE_CA.isin(["iPTLB"])]
    iPTLB_visit = iPTLB.GAwksCA.between(6,14, inclusive="left")
    patient_num["iPTLB in 6 - 13_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 16 - 21_6 weeks
    iPTLB_visit = iPTLB.GAwksCA.between(16,22, inclusive="left")
    patient_num["iPTLB in 16 - 21_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 22 - 29_6 weeks
    iPTLB_visit = iPTLB.GAwksCA.between(22, 30, inclusive="left")
    patient_num["iPTLB in 22 - 29_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 22 - 29_6 weeks
    iPTLB_visit = iPTLB.GAwksCA.between(30, 38, inclusive="left")
    patient_num["iPTLB in 30 - 37_6 weeks"] = iPTLB_visit.sum()

    #########################################################################
    # number of iPTLB with Hypertension
    cmd = get_data(BASE_PATH, "cmd.csv")
    iPTLB_HTN = count[count.STUDYID.isin(cmd.STUDYID)]
    patient_num["iPTLB_HTN"] = iPTLB_HTN.shape[0]

     # number of iPTLB in 6 - 13_6 weeks 
    iPTLB = pout[pout.TYPE_CA.isin(["iPTLB"])]
    iPTLB_visit = iPTLB_HTN.GAwksCA.between(6,14, inclusive="left")
    patient_num["iPTLB_HTN in 6 - 13_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 16 - 21_6 weeks
    iPTLB_visit = iPTLB_HTN.GAwksCA.between(16,22, inclusive="left")
    patient_num["iPTLB_HTN in 16 - 21_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 22 - 29_6 weeks
    iPTLB_visit = iPTLB_HTN.GAwksCA.between(22, 30, inclusive="left")
    patient_num["iPTLB_HTN in 22 - 29_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 22 - 29_6 weeks
    iPTLB_visit = iPTLB_HTN.GAwksCA.between(30, 38, inclusive="left")
    patient_num["iPTLB_HTN in 30 - 37_6 weeks"] = iPTLB_visit.sum()

    #########################################################################
    # number of iPTLB with Hypertension
    cmd = get_data(BASE_PATH, "cmd.csv")
    iPTLB_NOHTN = count[~count.STUDYID.isin(cmd.STUDYID)]
    patient_num["iPTLB_NOHTN"] = iPTLB_NOHTN.shape[0]

     # number of iPTLB in 6 - 13_6 weeks 
    iPTLB = pout[pout.TYPE_CA.isin(["iPTLB"])]
    iPTLB_visit = iPTLB_NOHTN.GAwksCA.between(6,14, inclusive="left")
    patient_num["iPTLB_NOHTN in 6 - 13_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 16 - 21_6 weeks
    iPTLB_visit = iPTLB_NOHTN.GAwksCA.between(16,22, inclusive="left")
    patient_num["iPTLB_NOHTN in 16 - 21_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 22 - 29_6 weeks
    iPTLB_visit = iPTLB_NOHTN.GAwksCA.between(22, 30, inclusive="left")
    patient_num["iPTLB_NOHTN in 22 - 29_6 weeks"] = iPTLB_visit.sum()

    # number of iPTLB in 22 - 29_6 weeks
    iPTLB_visit = iPTLB_NOHTN.GAwksCA.between(30, 38, inclusive="left")
    patient_num["iPTLB_NOHTN in 30 - 37_6 weeks"] = iPTLB_visit.sum()

    #########################################################################
    # number of iPTLB
    count = pout[pout.TYPE_CA.isin(["sPTLB"])]
    patient_num["sPTLB"] = count.shape[0]

    # number of sPTLB in 6 - 13_6 weeks 
    sPTLB = pout[pout.TYPE_CA.isin(["sPTLB"])]
    sPTLB_visit = sPTLB.GAwksCA.between(6,14, inclusive="left")
    patient_num["sPTLB in 6 - 13_6 weeks"] = sPTLB_visit.sum()

    # number of sPTLB in 16 - 21_6 weeks
    sPTLB_visit = sPTLB.GAwksCA.between(16,22, inclusive="left")
    patient_num["sPTLB in 16 - 21_6 weeks"] = sPTLB_visit.sum()

    # number of sPTLB in 22 - 29_6 weeks
    sPTLB_visit = sPTLB.GAwksCA.between(22, 30, inclusive="left")
    patient_num["sPTLB in 22 - 29_6 weeks"] = sPTLB_visit.sum()

    # number of sPTLB in 22 - 29_6 weeks
    sPTLB_visit = sPTLB.GAwksCA.between(30, 38, inclusive="left")
    patient_num["sPTLB in 30 - 37_6 weeks"] = sPTLB_visit.sum()

    ########################################################################
    
    print(patient_num)

if __name__ == "__main__":
    get_patient_number_diagram("../data/raw/")
    

    