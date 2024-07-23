# Credit_Card_Financial_Dashboard
# Table of content
- [Project Description](#Project-Description)
- [Dataset Description](#Dataset-Description)
- [DAX Queries](#DAX-Queries)
    - [Calculated column](#Calculated-column)
    - [Calulated measures](#Calulated-measures)
- [Dashboard Description](#Dashboard-Description)
- [Insights and Recommendations](#Insights-and-Recommendations)
- [Tech Stack](#Tech-Stack)
- [Key Learning Skills](#Key-Learning-Skills)
- [Your Contribution](#Your-Contribution)



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
- ## [Credit card transaction report](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/1.Credit_Card_Transaction_Report.jpg)
![Credit card transaction report](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/1.Credit_Card_Transaction_Report.jpg)
1. This page has 4 KPIs card visual at the top each repressnting the 4 different card categories, showing the total revenue made by them. The reference values shows the total transaction amount respectively.
2. On bottom left there is a matrix visual which shows the revenue distribution i.e. current, previous week revenue and wow revenue over quarter, month and week. I did conditional formatting on the columns to distinguish the revenue pattern.
3. Bottom left comprises of two visuals:
   - two card visual each showing total revenue and total profit.
   - a pie chart showing transaction amount distribution over expense type to track customer spending habbit.
5. The header also has two elements;
   - top left is the navigation button to navigate to customr report
   - top right has slicer pannel to filter out the result
     ![Slicer pane](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/3.Filter_pane.jpg)
---------------------------------------------------------------------------------------------------------------------------------------------------------------
- ## [Credit card customer report](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/2.Credit_Card_Customer_Report.jpg)
![Credit card customer report](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/2.Credit_Card_Customer_Report.jpg)
1. There are 6 KPIs card vusual showing total transation, avg revenue per customer, total customer acquistion cost, avg utilization ratio, total delinquent account and avg customer satifaction score. It also shows revenue distribution over payment methods.
2. Top right has a decomposition tree showing transaction amount hierarchy by income range, gender and expense type, this visual clearly shows customer spending habbit.
3. on bottom there is heat map which shows revenue by the customer job and age, and it also map visual which has revenue by states.
4. Similar to trasantion report header, customer report header also has a navigation button and slicer pane.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insights and Recommendations 
 ## Insights:
   ### WoW change - Week 53 (31 - December)
 - Revenue increased by **3.3%**
 - Transaction amount increased by **35%**
 - Transaction volume increased by **3.3%**
 - Count of customer increased by **13%** 
### YTD overview
 - **Total Revenue:** Total revenue is **$11 Million**
 - **Total Profit:** Total profit is **$10 Million**
 - **Total Transaction Amount:** Total transaction amt is **$46 Million**
 - **Revenue by category:** Blue card alone brings 85% of the revenue, together with sliver card they contibute to about 95% of the revenue
 - **Revenue distribution:** most of the revenue is made on the first month of every quarter i.e. january, april, july and october
 - **70%** of the cusotmers swipe their cards whereas only 6% of the them uses online method.
 - **buisnessman, white-collar and selfemployed** customer of age between **40 to 60** contributes to 50% of the revenue
 - **TX, CA and NY** contributes to 69% of the revenue
## Recommendations:
1. **Promote Rewards and Benefits:**
   - Enhance marketing efforts to showcase rewards, cashback offers, and exclusive benefits to attract and retain customers.

2. **Quarterly Promotions:**
   - Leverage the trend of increased revenue in the first month of every quarter (January, April, July, and October) by offering special promotions and discounts during these periods.

3. **Targeted Marketing Campaigns:**
   - Focus on middle-aged individuals (40-60) in the business, white-collar, and self-employed sectors.
   - Emphasize the convenience and security of card usage tailored to their financial needs.

4. **Geographic Focus:**
   - Concentrate marketing efforts in TX, CA, and NY, which together contribute to 69% of the revenue.
   - Develop localized campaigns to further penetrate these high-revenue markets.

5. **Enhance Online Transaction Methods:**
   - Encourage the use of online transaction methods, currently at 6%, through incentives and educational campaigns.
   - Improve the online transaction experience to increase adoption rates.

6. **Financial Education and Planning Services:**
   - Offer workshops or online resources to help customers better manage their finances.
   - Focus on the low-income group to improve their financial well-being and increase their card usage.

7. **Personalized Offers and Recommendations:**
   - Use data analytics to provide tailored offers based on customers' transaction history and preferences.

8. **Customer Retention Strategies:**
   - Implement loyalty programs, personalized communications, and proactive customer service to build long-term relationships and reduce churn.
   - Monitor and address the needs of delinquent accounts (6.6%) to improve customer satisfaction.

9. **Improve Customer Satisfaction:**
   - Focus on enhancing the overall customer experience to raise the average satisfaction score from 3.19 out of 5.
   - Gather and act on customer feedback to identify areas for improvement.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tech Stack
![Microsoft Excel Badge](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=Microsoft%20Excel&labelColor=black) ![Microsoft Power BI Badge](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=Power%20BI&labelColor=black) ![DAX](https://img.shields.io/badge/DAX-F2C811?style=for-the-badge&logo=Power%20BI&labelColor=black) ![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=PostgreSQL&labelColor=black) ![Python Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=Python&labelColor=black&color=4584b6) ![Static Badge](https://img.shields.io/badge/Visual_Studio_Code-black?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=0078d7&labelColor=black&color=0078d7)

---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Key Learning Skills
 > Data import
  - Imported data to SQL datbase using python script
> [!TIP]
> Click [HERE](https://github.com/DivyanshNeel/Credit_Card_Financial_Dashboard/blob/main/Importing_Data.py) to get help importing data to your database.
  - Furthermore, imported data from SQL database to Power BI

 > Data Modeling
  - Uing DAX, i created measures and conditional columns

 > Data Analysis and visualization
  - Performed data analysis and then created visual for developing the dashboard

---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Your Contribution
- I am incredibly grateful for your support and admiration of my effort. Please feel free to share any recommendations or ideas you may have with me. I can really benefit from your feedback as I continue to refine and improve future projects.

- I am now looking for an internship or entry-level job, so any help and support you can provide would be greatly appreciated. I promise to be appreciative of any assistance provided.

# By: **Divyansh Neel** on 24/07/2024

