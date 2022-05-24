import plotly.figure_factory as ff
import pandas as pd 
import csv
import statistics

df = pd.read_csv("StudentsPerformance.csv")

math_score = df["math score"]

#Mean for height and Weight
math_mean = statistics.mean(math_score)

#Median for height and weight

math_median = statistics.median(math_score)

#Mode for height and weight

math_mode = statistics.mode(math_score)

#Printing mean, median and mode to validate
print("Mean, Median and Mode of Math Score is {}, {} and {} respectively".format(math_mean, math_median, math_mode))

#Standard deviation for height and weight

math_std_deviation = statistics.stdev(math_score)

#1, 2 and 3 Standard Deviations for height

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

#1, 2 and 3 Standard Deviations for weight


#Percentage of data within 1, 2 and 3 Standard Deviations for Height

math_list_of_data_within_1_std_deviation = [result for result in math_score if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_score if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_score if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

#Printing data for height and weight (Standard Deviation)


print("{}% of data for math score lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_score)))
print("{}% of data for math score lies within 2 standard deviation".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_score)))
print("{}% of data for math score lies within 3 standard deviation".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_score)))
