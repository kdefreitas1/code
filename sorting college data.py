# file from assignment; its purpose is to find what college type has the highest average salary
import pandas as pd

data = pd.read_csv (r"college data.csv")
pd.set_option("display.max_columns", None)
data.dropna(inplace=True) # ignores all schools with incomplete info

# function averages out all salaries (probably could be done better but function was needed to complete given assignment)
def mean_all_salaries(one,two,three,four,five,six):
    return data[[one,two,three,four,five,six]].mean(axis=1)

# creates new column with all the salareis averaged for every school
data["Mean All Salaries"] = mean_all_salaries("Starting Median Salary","Mid-Career Median Salary","Mid-Career 10th Percentile Salary","Mid-Career 25th Percentile Salary","Mid-Career 75th Percentile Salary","Mid-Career 90th Percentile Salary")

# groups all school types together to average out and find which type has highest average salary 
print(round(data.groupby("School Type")["Mean All Salaries"].mean()))

# results
print()
print("From the results Ivy League schools are the ones with the highest average salary.")
