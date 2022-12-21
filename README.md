# Analysis_of_Shopping_Cart_Data

## **Index**

- [**Introduction**](#introduction)

<hr>

### Introduction

This project seeks to apply Data Analysis skills to a shopping cart dataset.

<br>

### Dataset Composition

Summary of the data set so far. These are some points we have:

- Customer Order and product data:

  - We have a total of 1000 rows and 22 columns
  - There are no missing values
  - customer_name: 1000 uniqueness variable(s)
  - gender : 8 uniqueness variable(s)
  - home_address : 1000 variable(s) of uniqueness
  - city : 961 variable(s) of uniqueness
  - state : 8 uniqueness variable(s)
  - country : 1 uniqueness variable(s)
  - order_date : 291 uniqueness variable(s)
  - delivery_date : 305 uniqueness variable(s)
  - product_type : 3 uniqueness variable(s)
  - product_name : 28 variable(s) of uniqueness
  - size : 5 uniqueness variable(s)
  - color : 7 uniqueness variable(s)
  - description : 1000 variable(s) of uniqueness

- Sales data:
  - There are no missing values
  - There are no uniqueness values

All data types in this data are Int 64
Next, we will try to do some explorations and visualizations.

<br>

### Data Analysis and Visualization (EDA)

By printing the data it's possible see the correlation value is between -1 and 1. The closer the values are to 1 or -1, the greater the correlation. Exactly 1 or -1 represents perfect correlation. 0 represents no correlation.

**Note:** NaN is expected if the values do not vary. To understand why, take a look at the correlation formula:

$
cor(i,j) = \frac{cov(i,j)}{[stedev(i)stdev(j)]}
$

If the values of variables i or j do not vary, the respective standard deviation will be zero and so will the denominator of the fraction. Therefore, the correlation will be NaN.

<br>

![Matrix](../Analysis_of_Shopping_Cart_Data/Shopping_Card_Analysis/img/matrix_correlation.png)
