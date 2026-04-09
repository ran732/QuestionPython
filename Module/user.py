user_dict ={
    'ranjeet':'1234567',
    'rama':'1234',
    'eleven':'123456',
    'rangoku':'1234567',
    'eranyeager':'1234567890'
}
def login(uname,pwd):
    if uname in user_dict and user_dict[uname]==pwd:
        return True
    else:
        return False