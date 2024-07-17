# Credit_Card_Financial_Dashboard
# Table of content
- [Project Description](#Project-Description)
- [Dataset Description](#Dataset-Description)
- [DAX Queries](#DAX-Queries)
    - [Calculated column](#Calculated-column)
    - [Calulated measures](#Calulated-measures)
- [Dashboard Description](#Dashboard-Description)
- [Insights and Recommendation ](#Insights-and-Recommendation)
- [Tech Stack](#Tech-Stack)
- [Key Learning Skills](#Key-Learning-Skills)
- [Conclusion](#Conclusion)



---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Project Description
The purpose of this project is to analyze the dataset and create a weekly transaction, customer - credit card dashboard that provides insight into performance measures and trends for better desicion making.

Stakeholders can utilize the provided insights and recommendations to make potential changes that can result in possible revenue growth.

# Dataset Description
The dataset belongs to a US based credit card company enclosing the data from January 2023 to December 2023.
### Credit Card Data ([`credit_card.csv`](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/credit_card.csv))

| Column Name            | Data Type | Description                              |
|------------------------|-----------|------------------------------------------|
| Client_Num           | int       | Unique identifier for the client         |
| Card_Category        | str       | Category of the credit card              |
| Annual_Fees          | int       | Annual fees for the credit card          |
| Activation_30_Days   | int       | Activation status within 30 days (0/1)   |
| Customer_Acq_Cost    | int       | Customer acquisition cost                |
| Week_Start_Date      | str       | Start date of the week                   |
| Week_Num             | int       | Week number                              |
| Qtr                  | str       | Quarter of the year                      |
| current_year         | int       | Current year                             |
| Credit_Limit         | float     | Credit limit of the card                 |
| Total_Revolving_Bal  | int       | Total revolving balance                  |
| Total_Trans_Amt      | int       | Total transaction amount                 |
| Total_Trans_Vol      | int       | Total transaction volume                 |
| Avg_Utilization_Ratio| float     | Average utilization ratio                |
| Use                  | str       | Use of the card (e.g., Chip, Swipe)      |
| Chip                 | str       | Type of chip used                        |
| Exp Type             | str       | Expense type (e.g., Travel, Grocery)     |
| Interest_Earned      | float     | Interest earned                          |
| Delinquent_Acc       | int       | Number of delinquent accounts            |
                              

### Customer Data ([`customer.csv`](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/customer.csv))
| Column Name                 | Data Type | Description                              |
|-----------------------------|-----------|------------------------------------------|
| Client_Num                  | int       | Unique identifier for the client         |
| Customer_Age                | int       | Age of the customer                      |
| Gender                      | str       | Gender of the customer                   |
| Dependent_Count             | int       | Number of dependents                     |
| Education_Level             | str       | Education level of the customer          |
| Marital_Status              | str       | Marital status                           |
| state_cd                    | str       | State code                               |
| Zipcode                     | int       | Zip code                                 |
| Car_Owner                   | str       | Car ownership status                     |
| House_Owner                 | str       | House ownership status                   |
| Personal_loan               | str       | Personal loan status                     |
| contact                     | str       | Contact type (e.g., cellular, unknown)   |
| Customer_Job                | str       | Job of the customer                      |
| Income                      | int       | Income of the customer                   |
| Cust_Satisfaction_Score     | int       | Customer satisfaction score              |

---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tech Stack
![Microsoft Excel Badge](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=Microsoft%20Excel&labelColor=black) ![Microsoft Power BI Badge](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=Power%20BI&labelColor=black) ![DAX](https://img.shields.io/badge/DAX-F2C811?style=for-the-badge&logo=Power%20BI&labelColor=black) ![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=PostgreSQL&labelColor=black) ![Python Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=Python&labelColor=black&color=4584b6) ![Static Badge](https://img.shields.io/badge/Visual_Studio_Code-black?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=0078d7&labelColor=black&color=0078d7)

---------------------------------------------------------------------------------------------------------------------------------------------------------------


# DAX Queries
## Calculated column
- ### Age group
Age_Group = `SWITCH(TRUE(),
'public customer'[Customer_Age] < 30, "20-30",
'public customer'[Customer_Age] >= 30 && 'public customer'[Customer_Age] < 40, "30-40",
'public customer'[Customer_Age] >= 40 && 'public customer'[Customer_Age] < 50, "40-50",
'public customer'[Customer_Age] >= 50 && 'public customer'[Customer_Age] < 60, "50-60",
'public customer'[Customer_Age] >= 60, "60+",
"unknown"
)`
### Income group 
Income_Range = `SWITCH(
    TRUE(),
    'public customer'[Income] < 35000, "Low",
    'public customer'[Income] >= 35000 && 'public customer'[Income] < 70000, "Medium",
    'public customer'[Income] >= 70000, "High",
    "Unknown"
)`
## Calulated measures
- ### Credit card measures table
  1. Total Revenue = `SUM('public credit_card'[Annual_Fees])+SUM('public credit_card'[Interest_Earned])` 
  2. current week revenue = `CALCULATE(SUM('public credit_card'[Revenue]),FILTER(ALL('public credit_card'),'public credit_card'[week_num2] = MAX('public credit_card'[week_num2])))`
  3. previous week revenue = `CALCULATE(SUM('public credit_card'[Revenue]),FILTER(ALL('public credit_card'),'public credit_card'[week_num2] = MAX('public credit_card'[week_num2])-1))`
  4. wow_revenue = `DIVIDE(([current_week_revenue]-[previous_week_revenue]),[previous_week_revenue])`
- ### Customer measures table
- 1. average utilization rate = `AVERAGE('public credit_card'[Avg_Utilization_Ratio])`
  2. CustomerAcqCost = `SUM('public credit_card'[Customer_Acq_Cost])`
  3. DeliquentAccRate = `DIVIDE(SUM('public credit_card'[Delinquent_Acc]),COUNT('public customer'[Client_Num]))`
  4. RevenuePerCustomer = `DIVIDE([Total_Revenue],COUNT('public customer'[Client_Num]))`
- ### Transaction per card table
  1. BlueCard = `CALCULATE(SUM('public credit_card'[Total_Trans_Amt]),'public credit_card'[Card_Category] = "Blue")`
  2. %BlueCard = `DIVIDE([BlueCard],[TotalTransAmount])`
> [!IMPORTANT]
> Similarly, sum of transaction for other cards can also be calculated.
- ### Revenue per card table
  1. BlueRevenue = `CALCULATE(SUM('public credit_card'[Revenue]), 'public credit_card'[Card_Category] = "Blue")`
> [!IMPORTANT]
> Similarly, sum of revenue for other cards can also be calculated.

# Dashboard Description
# Key Learning Skills
- Data import
