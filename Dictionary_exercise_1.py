#Creating Dictionaries for room number, instructor, and meeting time
dict_roomnum = {'CS101':3004,
                'CS102':4501,
                'CS103':6755,
                'NT110':1244,
                'CM241':1411}

dict_instr =   {'CS101':'Haynes',
                'CS102':'Alvarado',
                'CS103':'Rich',
                'NT110':'Burke',
                'CM241':'Lee'}

dict_meettime = {'CS101': "8:00 a.m.",
                'CS102': "9:00 a.m.",
                'CS103': "10:00 a.m.",
                'NT110': "11:00 a.m.",
                'CM241': "1:00 p.m."}

#checks to see if course number exists and user input
correct_key = False
while correct_key == False:
    input_coursenum = input("Enter in a course number: ")

    for keys in dict_roomnum:
        if input_coursenum == keys:
            correct_key = True
            
    if correct_key == False:
        print("that course doesn't exist please try again")
#combining dict info and outputting
output = ""
output = str(dict_roomnum[input_coursenum]) + " " + dict_instr[input_coursenum] + " " + dict_meettime[input_coursenum]
print(output)