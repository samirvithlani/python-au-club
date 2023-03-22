data ={1:"raj",2:"ram",3:"ravi",2:"rakesh"}

data1={}

# for i,j in data.items():
#     if len(j)>3:
#         data1[i]=j

data1 ={i:j for i,j in data.items() if len(j)>3}

print(data1)        
    

