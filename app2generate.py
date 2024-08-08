try:
    num = int(input('Generation number:\n'))
except:
    print('Error')
compete = 0
while num > compete:
    compete=compete+1
    print("st.image(Image.open('"+str(compete)+".png'), width=400)")