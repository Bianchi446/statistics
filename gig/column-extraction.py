import pandas as pd 
import numpy as np
import openpyxl

dataset = pd.read_csv("file.csv", header = None)
headerName = ["First Name", "Last Name", "Full Name", "Email", "Title", "City", "Country", "Founded Year", "Company", "Cleaned Company", "Website URL", "Personal Linkedin"]
dataset.columns=headerName

#Filtering by upper case

UpperCase_df = dataset["Company"].str.upper()

# Filtering by special character 

SpecialCharacter_df = dataset["Company"].str.replace('\W', ' ', regex=True)

# Filtering by posfix  -- Using the previous dataFrame


Postfix_df = SpecialCharacter_df.str.replace('Co.', ' ')
Postfix2_df = Postfix_df.str.replace('LLC', ' ')
Postfix3_df = Postfix2_df.str.replace('CORP', ' ')
Postfix4_df = Postfix3_df.str.replace('USA', ' ')
Postfix5_df = Postfix4_df.str.replace('Inc', ' ')
Postfix6_df = Postfix5_df.str.replace('North America', ' ')
Postfix7_df = Postfix6_df.str.replace('Inc.', ' ')
Postfix8_df = Postfix7_df.str.replace('Ltd', ' ' )
Postfix9_df = Postfix8_df.str.replace('NYC', ' ')
Postfix10_df = Postfix9_df.str.replace('Collection', ' ')
Postfix11_df = Postfix10_df.str.replace('Online Clothing Relailer', ' ')
Postfix12_df = Postfix11_df.str.replace('Manufacturing', ' ')
Postfix13_df = Postfix12_df.str.replace(' | ', ' ')
Postfix14_df = Postfix13_df.str.replace('Pvt', ' ')


LowerCase_df = Postfix14_df.str.lower()

Capitalize_df = Postfix14_df.str.title()

# print(UpperCase_df)

#print(dataset.head(40))
# print(SpecialCharacter_df.head(40))
print(Capitalize_df.head(60))



# Creating the excel file 

ExcelFile = Capitalize_df.to_excel("ExcelFile.xlsx")
