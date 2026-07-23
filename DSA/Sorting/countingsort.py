def CountingSort(num):
    n = len(num)
    mx =max(num)
    
    freq = [0]*(mx+1)
    
    for i in num:
        freq[i]+=1
        
        num = []
        
        for i in range (0,mx+1):
            while freq[i]>0:
                num.append(i)
                freq[i]-=1