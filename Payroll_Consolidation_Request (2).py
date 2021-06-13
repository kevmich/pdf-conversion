import re
from typing import Collection, NamedTuple
import PyPDF2
import requests
import pdfminer
import pandas as pd
from collections import namedtuple

payroll = namedtuple('payroll', ['emp_id', 'emp_name', 'salary', 'chk_date', 'rate', 'total_hours', 'total_amount'])

#Name regular expression
new_name_re = re.compile(r'(\w*, \w.*? \w.?) (.*)')#a name with . then ,
#Emp Id regular expression
new_id_re = re.compile(r'(.*) (Emp Id) (\w*) (.*)')
#Salery regular expression
new_salary_re = re.compile(r'(.*) (Salary) (\d.*?.\d\d) (.*)')
#Date regular expression
new_date_re = re.compile(r'(.*) (Chk Date) (\d*/\d*/\d*) (.*)')
#Rate regular expression
new_rate_re = re.compile(r'(.*) (Rate) (\d*.\d\d) (.*)')
#Totals regular expression
new_totals_re = re.compile(r'(.*) (Totals) (\d*.\d\d) (\d.*?.\d\d) (.*)')
#Salary and Date reqular Expresssion
#new_salary_date_re = re.compile(r'(Salary) (\d.*?.\d\d) (.*) (Chk Date) (\d*/\d*/\d*)')
#Salary and Date reqular Expresssion
#new_rate_date_re = re.compile(r'(Rate) (\d*?.\d\d) (.*) (Chk Date) (\d*/\d*/\d*)')

#PDF to be read
ap = open(r"Payroll Register for 2019-2020.pdf", 'rb')
#ap = 'Payroll Register for 2019-2020.pdf'

#Storage list god save my laptop
lines = []





#gets page 
#pageObject = pdfReader.getPage(0)
#gets text 
#pageObject.extractText()

#getpage
#pages = pdf.pages
#make page into text
#page = pageObject.extractText()

#read PDF 
pdfReader = PyPDF2.PdfFileReader(ap)

#gets num of pages 
num_pages = pdfReader.numPages

        
#running through pages
for page in range(num_pages):
    
    def listToString(joined_page):
        str = ''
        return str.join(joined_page)

    pageObject = pdfReader.getPage(page)
    page_text = pageObject.extractText()
    joined_page = page_text.s()
    temp = " ".join(page_text.split())
    #print(temp)

     
    #Setting Emp Name
    if new_name_re.match(temp):
        emp_name = new_name_re.search(temp).group(1)
        print("Name\n", emp_name)
        #lines.append(payroll(emp_name))

    #Setting Emp Id
    if new_id_re.match(temp):
        emp_id = new_id_re.match(temp).group(3)
        print("ID\n", emp_id)
        #lines.append(payroll(emp_id))

    #Setting Salary and date
    #elif new_salary_date_re.search(temp) :
    #    salary = new_salary_date_re.match(temp).group(2)
    #    date = new_salary_date_re.match(temp).group(5)
    #    print("Salary\n", salary)

    #Setting Rate and Date
    # elif new_salary_re.match(temp) :
    #     rate = new_rate_date_re.match(temp).group(2)
    #     date = new_rate_date_re.match(temp).group(5)
    #     print("Salary\n", salary)

    #Setting Salary
    if new_salary_re.search(temp):
        salary = new_salary_re.match(temp).group(3)
        print("Salary\n", salary)
        #lines.append(payroll(salary))
               
    #Setting Chk Date
    if new_date_re.search(temp):
        chk_date = new_date_re.search(temp).group(3)
        print("Check Date\n", chk_date)
        #lines.append(payroll(chk_date))

                
    #Setting rate
    if new_rate_re.search(temp):
        rate = new_rate_re.match(temp).group(3)
        print("Rate\n", rate)
        #lines.append(payroll(rate))

    #Setting Totals
    if new_totals_re.search(temp):
        total_hours = new_totals_re.search(temp).group(3)
        total_amount = new_totals_re.search(temp).group(4)
        # print("Total\n", total_hours)
        print(total_amount)
        #lines.append(payroll(total_amount))
        #lines.append(payroll(total_hours))

    for counter in range(num_pages) : 
        if num_pages < counter :       
            payroll(emp_id, emp_name, salary, chk_date, rate, total_hours, total_amount)
            lines.append(payroll)

df = pd.DataFrame(lines)
df.head()


#df['chk_date'] = pd.to_datetime(df['chk_date'])
#df['total_hours'] = df['total_hours'].map(lambda x: float(str(x).replace(',', '')))
#df['total_amount'] = df['total_amount'].map(lambda x: float(str(x).replace(',', '')))

#df.info()

df.to_csv("Payroll Register for 2019-2020.pdf", "Payroll Register for 2019-2020.csv", output_format="csv", pages='all')