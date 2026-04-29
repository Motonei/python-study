# write a program 
# Take the users credit score and annual income as input
# if the credit score is above 700,check if the income is above 50000
credit_score=int(input('Enter your credit score:'))
annual_income=int(input('Enter your annual income:'))
if credit_score>700:
    if annual_income<50-000:
        print('Loan approved')
    else:
        print('Income requirement not met')
else:
  print('Credit score too loe')