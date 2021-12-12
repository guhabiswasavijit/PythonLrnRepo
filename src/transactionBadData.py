import pandas as pd
from jproperties import Properties
import statistics as stat
import transactionDs as ts
df = pd.read_csv("C:\\SampleData\\transactional-data-format-csv.csv", low_memory=False,skiprows=0,usecols=['Balance value'])
print(df)
balanceValues = []
for row in df.iterrows():
    balanceValues.append(row.__getitem__(1)['Balance value'])

print(balanceValues)
dataSetMean = stat.mean(balanceValues)
print(dataSetMean)

configs = Properties()
  
with open('config.properties', 'rb') as read_prop:
    configs.load(read_prop)
      
threshold = configs.get("threshold")[0]

df = pd.read_csv("C:\\SampleData\\transactional-data-format-csv.csv", low_memory=False)
filteredRecord = []
rowInx = 0
for row in df.iterrows():
    if rowInx != 0 :
        trn = ts.Transaction(row.__getitem__(1)['Date'],
                             row.__getitem__(1)['Industry'],
                             row.__getitem__(1)['Group'],
                             row.__getitem__(1)['Item code'],
                             row.__getitem__(1)['Description'],
                             row.__getitem__(1)['Quantity Sold'],
                             row.__getitem__(1)['On hand'],
                             row.__getitem__(1)['Purchace price'],
                             row.__getitem__(1)['Shelf life'],
                             row.__getitem__(1)['Balance value'],
                             row.__getitem__(1)['Supplier code'])
        filteredRecord.append(trn)
    rowInx = rowInx + 1
filteredDf = pd.DataFrame(filteredRecord)
print(filteredDf)
filteredDf.to_csv("C:\\SampleData\\BadData.csv")