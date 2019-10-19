import random
import winsound


loop = True
while loop == True:
    print("\n---------------------------------")
    print("Please choose between 1 or 2 or 3")
    option = str(input("Select number of dice:\n"))

    if option == "1":
        Roll_A = random.sample(range(1,7),1)
        print("\t" + str(Roll_A))
        print ("\t total: "+ str(Roll_A))
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print("Next Turn")
        

    if option == "2":
        Roll_B = random.sample(range(1,7),2)
        print("\t" + str(Roll_B))
        sum_B = int(Roll_B[0])+ int(Roll_B[1])
        print ('\t total: '+ str(sum_B))
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print("Next Turn")
       

    if option == "3":
        Roll_C = random.sample(range(1,7),3)
        print("\t" + str(Roll_C))
        sum3 = int(Roll_C[0])+ int(Roll_C[1])+int(Roll_C[2])
        print("\t total: "+ str(sum3))
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print("Next Turn")
