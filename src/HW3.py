import csv
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'kanit'

csv_path = "../datasets/ubatiehtuthaangthnn.csv"

with open(csv_path, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    dead_num_list = []
    patient_num_list = []

    accident_num = 0
    for row in csv_reader:

        if accident_num != 0:
            vechicle, dead_num, patient_num = row[10], int(row[15]), int(row[16])

            dead_num_list.append(dead_num)
            patient_num_list.append(patient_num)

        accident_num += 1

    ## Data ##
    dead_num_list = np.array(sorted(dead_num_list))
    patient_num_list = np.array(sorted(patient_num_list))

    ## Probability Density Function ##
    pdf_dead = norm.pdf(dead_num_list,np.mean(dead_num_list),np.std(dead_num_list))
    plt.plot(dead_num_list,pdf_dead,'-o')
    plt.title("กราฟ Probability Density Function จำนวนผู้เสียชีวิตในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้เสียชีวิตในอุบัติเหตุ (คน)")
    plt.ylabel("Density")
    plt.grid()
    plt.show()

    pdf_patient = norm.pdf(patient_num_list,np.mean(patient_num_list),np.std(patient_num_list))
    plt.plot(patient_num_list,pdf_patient,'-o')
    plt.title("กราฟ Probability Density Function จำนวนผู้บาดเจ็บในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("Density")
    plt.grid()
    plt.show()

    ## Cumulative Probability Function ##
    cdf_dead = norm.cdf(dead_num_list,np.mean(dead_num_list),np.std(dead_num_list))
    plt.plot(dead_num_list,cdf_dead,'-o')
    plt.title("กราฟ Cumulative Probability Function จำนวนผู้เสียชีวิตในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้เสียชีวิตในอุบัติเหตุ (คน)")
    plt.ylabel("Probability")
    plt.grid()
    plt.show()

    cdf_patient = norm.cdf(patient_num_list,np.mean(patient_num_list),np.std(patient_num_list))
    plt.plot(patient_num_list,cdf_patient,'-o')
    plt.title("กราฟ Cumulative Probability Function จำนวนผู้บาดเจ็บในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("Probability")
    plt.grid()
    plt.show()