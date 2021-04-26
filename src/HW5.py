import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

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

    dead_num_list = np.array(dead_num_list)
    patient_num_list = np.array(patient_num_list)

    ## Linear Regression Solve
    (slope, intercept, r_value, p_value, std_err) = scipy.stats.linregress(patient_num_list, dead_num_list)

    ## XY Scatter Plot
    plt.scatter(patient_num_list,dead_num_list,color='red',alpha=0.3)
    plt.plot(patient_num_list, slope*patient_num_list + intercept)
    plt.title("กราฟเเสดงความสัมพันธ์ของจำนวนผู้บาดเจ็บกับจำนวนผู้เสียชีวิตในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("จำนวนผู้เสียชีวิตในอุบัติเหตุ (คน)")
    plt.grid()
    plt.show()

    print("=====================================================================================\n")
    print("สมการ Linear Regression : Y = ({}*X) + {}".format(slope,intercept))
    print("ค่าสัมประสิทธิ์สหสัมพันธ์ (r) : {}".format(r_value))
    print("ค่าคลาดเคลื่อนมาตรฐาน : {}".format(std_err))
    print("\n=====================================================================================")