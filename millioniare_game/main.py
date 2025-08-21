questions =[
    ["Who is the president of the United States?","Donald J Trump","Mark Carney","Barack Obama","George W. Bush", 1],
    ["What is the capital of the United Kingdom?","London","Edinburgh","Cardiff","Belfast", 1],
    ["What is the capital of France?","Berlin","Madrid","Paris","Rome", 2],
    ["What is the largest mammal?","Elephant","Blue Whale","Giraffe","Great White Shark", 1],
    ["What is the chemical symbol for water?","H2O","CO2","O        2","NaCl", 1],
    ["What is the capital of Japan?","Tokyo","Kyoto","Osaka","H iroshima", 1]
]
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    #check whether the answer is correct
    answer = int(input("please enter your answer. 1 for a, 2 for b, 3 for c, 4 for d"))
    if(question[5]== a):
        print("Correct Answer, Bingo!!!!")
    else:
        print(f"Wrong Answer, the correct answer is {question[5]}")  
        break  


