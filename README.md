# Credit_Card_Financial_Dashboard
# Table of content
- [Project Description](#Project-Description)
- [Dataset Description](#Dataset-Description)
- [Key Learning Skills](#Key-Learning-Skills)
- [Data Source](#Data-Source )
- [Tech Stack](#Tech-Stack)
- [Key Performance Indicators](#Key-Performance-Indicators)
  - [Calculated Measured KPIs](#Calculated-Measured-KPIs)
    - [Hiring Measures](#Hiring-Measures)
    - [Promotion Measures](#Promotion-Measures)
    - [Performance and Turnover Measures](#Performance-and-Turnover_Measures)
- [Insights and Recommendation ](#Insights-and-Recommendation)
- [Dashboard](#Dashboard)
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


