testcase=int(input())
for i in range(testcase):
    st=input()
    s=st.count('SUVOJIT')
    st=st.replace('SUVOJIT',',')
    c=st.count('SUVO')
    print("SUVO =",str(c)+", " +"SUVOJIT = "+str(s))
