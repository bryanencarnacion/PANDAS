import pandas as pd
cars = pd.read_csv('cars.csv')
car = pd.DataFrame(cars, index=[0,1,2,3,4,5,27,28,29,30,31])