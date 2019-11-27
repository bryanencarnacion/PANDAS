import pandas as pd
car = pd.read_csv('cars.csv')
A = car.loc[:4,['mpg','disp','drat','qsec','am','carb']]
B = car[car['Model']=='Mazda RX4']
C = car.loc[car['Model']=='Camaro Z28',['cyl']]
D = car.loc[[1,28,18],['Model','cyl','gear']]