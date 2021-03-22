import csv
import math
import numpy as np
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'kanit'

csv_path = "../datasets/ubatiehtuthaangthnn.csv"

def CI_Mean(confidence_level,mean,sd,n):
    z_value = scipy.stats.norm.ppf(1-((1-(confidence_level/100))/2))

    return (mean-(z_value*(sd/math.sqrt(n))),mean+(z_value*(sd/math.sqrt(n))))

with open(csv_path, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    patient_num_list = []

    accident_num = 0
    for row in csv_reader:

        if accident_num != 0:
            vechicle, patient_num = row[10], int(row[16])

            patient_num_list.append(patient_num)

        accident_num += 1

    ## Data ##
    patient_num_list = np.array(sorted(patient_num_list))
    patient_num_mean = np.mean(patient_num_list)
    patient_num_sd = np.std(patient_num_list)

    #Confidence Intreval of Meann: 90%
    confidence_interval = CI_Mean(90,patient_num_mean,patient_num_sd,len(patient_num_list))
    print("\n[Confidence Level 90%] Confidence Interval of Mean : {}".format(confidence_interval))

    pdf_patient = scipy.stats.norm.pdf(patient_num_list,np.mean(patient_num_list),np.std(patient_num_list))
    plt.plot(patient_num_list,pdf_patient,'-o')
    plt.title("กราฟ Probability Density Function จำนวนผู้บาดเจ็บในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("Density")
    plt.plot([confidence_interval[0],confidence_interval[0]],[0,max(pdf_patient)+0.01])
    plt.plot([confidence_interval[1],confidence_interval[1]],[0,max(pdf_patient)+0.01])
    plt.grid()
    plt.show()

    #Confidence Interval of Mean : 95%
    confidence_interval = CI_Mean(95,patient_num_mean,patient_num_sd,len(patient_num_list))
    print("\n[Confidence Level 95%] Confidence Interval of Mean : {}".format(confidence_interval))

    pdf_patient = scipy.stats.norm.pdf(patient_num_list,np.mean(patient_num_list),np.std(patient_num_list))
    plt.plot(patient_num_list,pdf_patient,'-o')
    plt.title("กราฟ Probability Density Function จำนวนผู้บาดเจ็บในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("Density")
    plt.plot([confidence_interval[0],confidence_interval[0]],[0,max(pdf_patient)+0.01])
    plt.plot([confidence_interval[1],confidence_interval[1]],[0,max(pdf_patient)+0.01])
    plt.grid()
    plt.show()

    #Confidence Interval of Mean : 99%
    confidence_interval = CI_Mean(99,patient_num_mean,patient_num_sd,len(patient_num_list))
    print("\n[Confidence Level 99%] Confidence Interval of Mean : {}".format(confidence_interval))

    pdf_patient = scipy.stats.norm.pdf(patient_num_list,np.mean(patient_num_list),np.std(patient_num_list))
    plt.plot(patient_num_list,pdf_patient,'-o')
    plt.title("กราฟ Probability Density Function จำนวนผู้บาดเจ็บในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("Density")
    plt.plot([confidence_interval[0],confidence_interval[0]],[0,max(pdf_patient)+0.01])
    plt.plot([confidence_interval[1],confidence_interval[1]],[0,max(pdf_patient)+0.01])
    plt.grid()
    plt.show()

    

    
