def fz(n):
    m3=m5=0
    # ch=''
    for i in range(1,n):
        m3+=1
        m5+=1
        ch=''
        if m3==3:
            ch+='fizz'
            m3=0
            
        if m5==5:
            ch+='buzz'
            m5=0
            
        if ch=='':
            print(i)
            
        else:
            print(ch)
    # return ch
fz(100)