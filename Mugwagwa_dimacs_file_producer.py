#My name is Charles Mugwagwa. This is an implimentation of a program that produces a dimics file for solving a sudoku problem.
inputFile = open('input_file.txt','r')
outputFile = open('dimacs.txt','w')
outputFile.write("p cnf 729 8855 \n")

for x in range(1,10,1): 
    for y in range(1,10,1):
        alist = []
        for z in range(1,10,1):
            S_xyz = (81*(x-1))+(9*(y-1))+z            
            alist.append(S_xyz)              
        sentence = ""
        for variable in alist:
            sentence = sentence+str(variable)+" "        
        sentence = sentence+" 0"+'\n'        
        outputFile.write(sentence)        
for y in range(1,10,1):
    for z in range(1,10,1):        
        for x in range(1,9,1):
            for i in range(x+1,10,1):
                S_xyz = 81*(x-1)+9*(y-1)+z
                S_iyz = 81*(i-1)+9*(y-1)+z                
                sentence = "-"+str(S_xyz)+" "+"-"+str(S_iyz)+" 0"+"\n"
                outputFile.write(sentence)                
for x in range(1,10,1): 
    for z in range(1,10,1):
        for y in range(1,9,1):
            for i in range(y+1,10,1):
                S_xyz = 81*(x-1)+9*(y-1)+z               
                S_xiz = 81*(x-1)+9*(i-1)+z               
                sentence = "-"+str(S_xyz)+" "+"-"+str(S_xiz)+" 0"+"\n"                
                outputFile.write(sentence)                
for z in range(1,10,1):
    for i in range(0,3,1):
        for j in range(0,3,1):
            for x in range(1,4,1):
                for y in range(1,4,1):
                    for k in range(y+1,4,1):                        
                        S__3i_x_3j_y_z = 81*(((3*i)+x)-1)+9*(((3*j)+y)-1)+z
                        S__3i_z_3j_k_z = 81*(((3*i)+x)-1)+9*(((3*j)+k)-1)+z
                        sentence = "-"+str(S__3i_x_3j_y_z)+" "+"-"+str(S__3i_z_3j_k_z)+" 0"+"\n"
                        outputFile.write(sentence)                        
for z in range(1,10,1):
    for i in range(0,3,1):
        for j in range(0,3,1):
            for x in range(1,4,1):
                for y in range(1,4,1):
                    for k in range(x+1,4,1):
                        for l in range(1,4,1):
                            S__3i_x_3j_y_z = 81*(((3*i)+x)-1)+9*(((3*j)+y)-1)+z
                            S__3i_k_3j_l_z = 81*(((3*i)+k)-1)+9*(((3*j)+l)-1)+z
                            sentence = "-"+str(S__3i_x_3j_y_z)+" "+"-"+str(S__3i_k_3j_l_z)+" 0"+"\n"
                            outputFile.write(sentence)                            
line = inputFile.readline().strip().split() 
row = 0
listStart = 0
while line != []: #Processing pre-assigned entries
    column = 0    
    for token in line:
        column += 1
        listStart = ((81*(row)) +((column-1)*9))+1        
        alist = []
        if token != "x": #pre-assigned value. 
            num = listStart+ (int(token)-1)
            sentence = str(num)+" 0"+"\n"
            outputFile.write(sentence)
    row +=1    
    line = inputFile.readline().strip().split()
outputFile.close()
inputFile.close()
print("End of the program. The 'dimacs.txt' file has been produced!") 