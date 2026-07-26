except:
    t=sys.exc_info()
    print(t[0])   
finally:   
    f.close()