import pandas as pd
from sklearn.metrics import pairwise_distances

class CosineSimilarity():
    def __init__(self,*args, **kwargs):
        self.test = args[0]
        self.train = args[1] 
        self.calculate_cosine()
        
    
    def calculate_cosine(self):
        cosine_sim = 1-pairwise_distances(self.train,self.test, metric="cosine")
        result= pd.DataFrame(cosine_sim)
        rec_index= self.filter(result)
        return rec_index
        
    def filter(self,result):
        result= result.stack()
        result= result.sort_values(ascending=False )
        result= result.iloc[0:7:1]
        rec_index= []
        for (index,value) in result.iteritems():
            rec_index.append(((index[0]+1),value))
        return rec_index
    
if __name__ == '__main__':
    pass
    

    

