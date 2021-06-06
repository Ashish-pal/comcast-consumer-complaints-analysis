#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\ashish\\Documents\\Python DS project\\comcast telecom consumer complaints\\Comcast_telecom_complaints_data.csv')

df.describe()

df.describe(include = 'all')

df.head()

df.info()

df.isnull().sum()

df = df.drop(['Ticket #','Time'],axis=1)

df.head()

df['Date_month_year'] = df['Date_month_year'].apply(pd.to_datetime)

df.info()

df = df.set_index('Date_month_year')

df.head()

df.groupby(pd.Grouper(freq='M')).size().plot()
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Monthly Trend Chart')

df['Date'].value_counts()[:15]

df.groupby(pd.Grouper(freq='D')).size().plot()
plt.xlabel('Daily Basis')
plt.ylabel('Frequency')
plt.title('Daily Trend Chart')

df = df.sort_values(by='Date')
plt.figure(figsize=(10,8))
df['Date'].value_counts().plot()
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title('Daily Trend Chart')

df['Customer Complaint'].value_counts()


df['Customer Complaint'].value_counts()[:15]

df['Customer Complaint'].value_counts()[:15].plot.bar()

df['Customer Complaint'].value_counts().plot.bar()

df['Customer Complaint'].unique()

internet_issue1 = df[df['Customer Complaint'].str.contains('network')].count()
#print(internet_issue1)

internet_issue2 = df[df['Customer Complaint'].str.contains('speed')].count()

internet_issue3 = df[df['Customer Complaint'].str.contains('data')].count()

internet_issue4 = df[df['Customer Complaint'].str.contains('internet')].count()

billing_issue1 = df[df['Customer Complaint'].str.contains('billing')].count()

billing_issue2 = df[df['Customer Complaint'].str.contains('charges')].count()

billing_issue3 = df[df['Customer Complaint'].str.contains('bill')].count()

service_issue1 = df[df['Customer Complaint'].str.contains('service')].count()

service_issue2 = df[df['Customer Complaint'].str.contains('customer')].count()

total_issue_internet = internet_issue1 + internet_issue2 + internet_issue3 + internet_issue4
print(total_issue_internet)

total_billing_issues = billing_issue1 + billing_issue2 + billing_issue3
print(total_billing_issues)

total_service_issues = service_issue1 + service_issue2
print(total_service_issues)

df.shape

other_issues = 2224 - (total_billing_issues + total_service_issues + total_issue_internet)

print(other_issues)

df['newStatus']= ['Open' if Status=='Open' or Status=='Pending' else 'Closed' for Status in df['Status']]

df.head(15)

df.sample(15)

df.groupby(['State']).size().sort_values(ascending=False)[:10]

state_complain = df.groupby(['State','newStatus']).size().unstack()

print(state_complain)

state_complain.plot.bar(figsize=(10,10),stacked=True)

df.newStatus.value_counts()

unresolved_data = df.groupby(['State','newStatus']).size().unstack().fillna(0).sort_values(by='Open',ascending=False)
print(unresolved_data)

unresolved_data['unresolved_cmp_prct']=unresolved_data['Open']/unresolved_data['Open'].sum()*100

print(unresolved_data)

unresolved_data.plot()

unresolved_data.plot.bar(figsize=(10,10),stacked=True)

resolved_data = df.groupby(['Received Via','newStatus']).size().unstack().fillna(0)

resolved_data['resolved'] = resolved_data['Closed']/resolved_data['Closed'].sum()*100
print(resolved_data)

resolved_data.plot()

resolved_data.plot.bar(figsize=(10,10),stacked=True)

resolved_data.plot(kind='bar',figsize=(10,10))




