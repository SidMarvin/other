import time
text = "Привет, пользователь."

for i in range(len(text)):
    time.sleep(0.1)
    print(text[i],end='',flush=True)

print("\n")    
    
print("\n")

text1 = "a b c d e f g h i j k l m n o p r s t"
text2 = "b c d e f g h i j k l m n o p r s t u"
text3 = "c d e f g h i j k l m n o p r s t u v"
text4 = "d e f g h i j k l m n o p r s t u v w"
text5 = "e f g h i j k l m n o p r s t u v w x"

for i in range(len(text1)):
    time.sleep(0.01)
    print(text1[i],end='',flush=True)
print("\n") 
for i in range(len(text2)):
    time.sleep(0.01)
    print(text2[i],end='',flush=True)
print("\n")     
for i in range(len(text3)):
    time.sleep(0.01)
    print(text3[i],end='',flush=True)
print("\n")      
for i in range(len(text4)):
    time.sleep(0.01)
    print(text4[i],end='',flush=True)
print("\n")      
for i in range(len(text5)):
    time.sleep(0.01)
    print(text5[i],end='',flush=True)
    
