store =[("shirt", "20.00"), ("pants", "30.00")]


to_euros = lambda data: (data[0], float(data[1])*0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

    
