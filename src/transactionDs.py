class Transaction :
  def __init__(self,date:str,industry:str,group:str,itemCode:str,description:str,quantitySold:int,onHand:str,purchasePrice:float,shelfLife:int,balanceValue:float,supplierCode:int):
        self.date = date
        self.industry = industry
        self.group = group
        self.itemCode = itemCode 
        self.description=description       
        self.quantitySold = quantitySold
        self.onHand = onHand
        self.purchasePrice = purchasePrice
        self.shelfLife = shelfLife
        self.balanceValue = balanceValue
        self.supplierCode = supplierCode
        
  def to_dict(self):
        return {
            'date': self.date,
            'industry': self.industry,
            'group':self.group,
            'itemCode':self.itemCode,
            'description':self.description,
            'quantitySold':self.quantitySold,
            'onHand':self.onHand,
            'purchasePrice':self.purchasePrice,
            'shelfLife':self.shelfLife,
            'balanceValue':self.balanceValue,
            'supplierCode':self.supplierCode
            
        }


                                         
