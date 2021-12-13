import pandas as pd
from jproperties import Properties
import statistics as stat
import transactionDs as ts
df_BalanceValueCol = pd.read_csv("C:\\SampleData\\transactional-data-format-csv.csv", low_memory=False,skiprows=0,usecols=['Balance value'])
print(df_BalanceValueCol)
balanceValues = []
for row in df_BalanceValueCol.iterrows():
    balanceValues.append(row.__getitem__(1)['Balance value'])

print(balanceValues)
dataSetMean = stat.mean(balanceValues)
print(dataSetMean)

configs = Properties()
  
with open('config.properties', 'rb') as read_prop:
    configs.load(read_prop)
      
threshold = int(configs.get("threshold")[0])

df = pd.read_csv("C:\\SampleData\\transactional-data-format-csv.csv", low_memory=False)
print(df)
filteredRecord = []
rowInx = 0
for row in df.iterrows():
    if rowInx != 0 :
        _date = row.__getitem__(1)['Date']
        _industry = row.__getitem__(1)['Industry']
        _group = row.__getitem__(1)['Group']
        _itemCode = row.__getitem__(1)['Item code']
        _description = row.__getitem__(1)['Description']
        _quantitySold = row.__getitem__(1)['Quantity Sold']
        _onHand = row.__getitem__(1)['On hand']
        _purchacePrice = row.__getitem__(1)['Purchace price']
        _shelfLife = row.__getitem__(1)['Shelf life']
        _balanceValue = row.__getitem__(1)['Balance value']
        _supplierCode = row.__getitem__(1)['Supplier code'] 
        trn = ts.Transaction(_date,
                             _industry,
                             _group,
                             _itemCode,
                             _description,
                             _quantitySold,
                             _onHand,
                             _purchacePrice,
                             _shelfLife,
                             _balanceValue,
                             _supplierCode)
        if _balanceValue > threshold:
            filteredRecord.append(trn)
    rowInx = rowInx + 1
filteredDf = pd.DataFrame.from_records([s.to_dict() for s in filteredRecord])
print(filteredDf)
filteredDf.to_csv("C:\\SampleData\\BadData.csv",index=False,header=['Date','Industry','Group','Item code','Description','Quantity Sold','On hand','Purchace price','Shelf life','Balance value','Supplier code'])