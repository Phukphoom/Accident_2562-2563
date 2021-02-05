import csv
import statistics
import pandas as pd
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
    
    ## Result
    print("===========================================================\n")

    print("จำนวนอุบัติเหตุทั้งหมด : {} ครั้ง".format(accident_num))
    print("จำนวนผู้บาดเจ็บทั้งหมด : {} คน".format(sum(patient_num_list)))
    print("จำนวนผู้เสียชีวิตทั้งหมด : {} คน".format(sum(dead_num_list)))

    print("\n-----------------------------------------------------------\n")

    print("(median) มัธยฐาน จำนวนผู้บาดเจ็บในอุบัติเหตุ : {} คน ".format(statistics.median(patient_num_list)))
    print("(mode) ฐานนิยม จำนวนผู้บาดเจ็บในอุบัติเหตุ : {} คน ".format(statistics.mode(patient_num_list)))
    print("(mean) ค่าเฉลี่ย จำนวนผู้บาดเจ็บในอุบัติเหตุ : {:.2f} คน ".format(statistics.mean(patient_num_list)))
    print("(SD) ส่วนเบี่ยงเบนมาตรฐาน จำนวนผู้บาดเจ็บในอุบัติเหตุ : {:.2f}".format(statistics.stdev(patient_num_list)))

    print()
 
    print("(median) มัธยฐาน จำนวนผู้เสียชีวิตในอุบัติเหตุ : {} คน".format(statistics.median(dead_num_list)))
    print("(mode) ฐานนิยม จำนวนผู้เสียชีวิตในอุบัติเหตุ : {} คน".format(statistics.mode(dead_num_list)))
    print("(mean) ค่าเฉลี่ย จำนวนผู้เสียชีวิตในอุบัติเหตุ : {:.2f} คน".format(statistics.mean(dead_num_list)))
    print("(SD) ส่วนเบี่ยงเบนมาตรฐาน จำนวนผู้เสียชีวิตในอุบัติเหตุ : {:.2f}".format(statistics.stdev(dead_num_list)))

    print("\n===========================================================")

    ## Histogram
    plt.hist(patient_num_list,bins=range(max(patient_num_list)))
    plt.title("Histogram เเสดงความถี่ของจำนวนผู้บาดเจ็บในการเกิดอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("จำนวนครั้งที่เกิดอุบัติเหตุ (ครั้ง)")
    plt.show()
    plt.hist(dead_num_list,bins=range(max(dead_num_list)))
    plt.title("Histogram เเสดงความถี่ของจำนวนผู้เสียชีวิตในการเกิดอุบัติเหตุ")
    plt.xlabel("จำนวนผู้เสียชีวิตในอุบัติเหตุ (คน)")
    plt.ylabel("จำนวนครั้งที่เกิดอุบัติเหตุ (ครั้ง)")
    plt.show()

    ## XY Scatter Plot
    plt.scatter(patient_num_list,dead_num_list,color='red',alpha=0.3)
    plt.title("กราฟเเสดงความสัมพันธ์ของจำนวนผู้บาดเจ็บกับจำนวนผู้เสียชีวิตในอุบัติเหตุ")
    plt.xlabel("จำนวนผู้บาดเจ็บในอุบัติเหตุ (คน)")
    plt.ylabel("จำนวนผู้เสียชีวิตในอุบัติเหตุ (คน)")
    plt.grid()
    plt.show()