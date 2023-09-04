import sys
print(sys.executable)
import pickle
with open("./model/hpc.pkl",'rb') as file:
    model = pickle.load(file)
print(model.predict([[43467,5,1,1000,5000,2,1,1,4,7,500,500,2010,2023,574237,500,1500,5,10]]))

