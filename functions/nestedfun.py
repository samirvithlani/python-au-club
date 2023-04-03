def getData():    
    print("Data")
    
    def getMoreData():
        print("More Data")
        return 2000
    
    # x = getMoreData()
    # return x
    return getMoreData()
    
p  = getData()
print(p)
        