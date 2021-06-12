import re
from typing import Collection, NamedTuple
import requests
import pdfplumber
import pandas as pd
from collections import namedtuple

payroll = namedtuple('payroll', 'emp_id emp_name salary chk_date rate total_hours total_amount')

#Name regular expression
new_name_re = re.compile(r'(\w*, \w.*?) (Code)')#a name with . then ,
#Emp Id regular expression
new_id_re = re.compile(r'(Emp Id) (\w*)')
#Salery regular expression
new_salary_re = re.compile(r'^(Salary) (\d.*.\d\d) (.*)')
#Date regular expression
new_date_re = re.compile(r'(.*) (Chk Date) (\d*/\d*/\d*)')
#Rate regular expression
new_rate_re = re.compile(r'^(Rate) (\d*.\d\d)')
#Totals regular expression
new_totals_re = re.compile(r'(Totals) (\d*.\d\d) (\d.*?.\d\d) (.*)')
#Salary and Date reqular Expresssion
new_salary_date_re = re.compile(r'^(Salary) (\d.*?.\d\d)(.*)(Chk Date) (\d*/\d*/\d*)')
#Salary and Date reqular Expresssion
new_rate_date_re = re.compile(r'^(Rate) (\d*?.\d\d) (.*) (Chk Date) (\d*/\d*/\d*)')

#PDF to be read
ap = 'Payroll Register for 2019-2020.pdf'

#Storage list god save my laptop
lines = []

#File reader
with pdfplumber.open(ap) as pdf:
    page = pdf.pages
    #Page reader
    for page in pdf.pages:
        text = page.extract_text()
        
        #Finding the name
        for line in text.split('\n'):
            
            #Setting Emp Name
            if new_name_re.match(line):
                emp_name = new_name_re.search(line).group(1)
                print("Name\n", emp_name)

            #Setting Emp Id
            elif new_id_re.match(line):
                emp_id = new_id_re.match(line).group(2)
                print("ID\n", emp_id)

            #Setting Salary and date
            elif new_salary_date_re.search(line) :
                salary = new_salary_date_re.match(line).group(2)
                date = new_salary_date_re.match(line).group(5)
                print("Salary\n", salary)

            #Setting Rate and Date
            elif new_salary_re.match(line) :
                rate = new_rate_date_re.match(line).group(2)
                date = new_rate_date_re.match(line).group(5)
                print("Salary\n", salary)

            #Setting Salary
            elif new_salary_re.search(line):
                salary = new_salary_re.match(line).group(2)
                print("Salary\n", salary)
               
            #Setting Chk Date
            elif new_date_re.search(line):
                chk_date = new_date_re.search(line).group(3)
                print("Check Date\n", chk_date)

                
            #Setting rate
            elif new_rate_re.search(line):
                rate = new_rate_re.match(line).group(2)
                print("Rate\n", rate)

            #Setting Totals
            elif new_totals_re.search(line):
                total_hours = new_totals_re.search(line).group(2)
                total_amount = new_totals_re.search(line).group(3)
                print("Total\n", total_hours)
                print(total_amount)
                
                #lines.append(payroll(emp_id, emp_name, salary, chk_date, rate, total_hours, total_amount))

#df = pd.DataFrame(lines)
#df.head()


#df['chk_date'] = pd.to_datetime(df['chk_date'])
#df['total_hours'] = df['total_hours'].map(lambda x: float(str(x).replace(',', '')))
#df['total_amount'] = df['total_amount'].map(lambda x: float(str(x).replace(',', '')))

#df.info()

#df.to_csv("Payroll Register for 2019-2020.pdf", "Payroll Register for 2019-2020.csv", output_format="csv", pages='all')