quiz=[{"Question":"Who Is The Richest Person In The World?","Options":["a.Jeff Bezos","b.Elon Musk","c.Bill Gates","d.Bernarld Aurnalt"],"correct_ans":"d"},
      {"Question":"Who Is the current CEO Of Apple?","Options":["a.Jeff Williams","b.Arthur Levison","c.Tim Cook","d.Lee Jae Yong"],"correct_ans":"c"},
      {"Question":"Who is record Holder In IPL For most runs scored?","Options":["a.GT","b.SRH","c.KKR","d.CSK"],"correct_ans":"b"},
      {"Question":"Who is the coach of The present India Team?","Options":["a.Rahul Dravid","b.Ravi Shastri","c.Gautam Gambhir","d.VVS Laxman"],"correct_ans":"c"},
      {"Question":"Which country has the Highest GDP","Options":["a.China","b.Japan","c.Germany","d.United States"],"correct_ans":"d"}]
def Quiz():
    score=0
    for i in quiz:
        print(i["Question"])
        for option in i["Options"]:
            print(option)
        a=input("What is the correct answer?:")
        if a==i["correct_ans"]:
            print("Your answer is correct.")
            score+=1
        else:
            print("Your answer is wrong IDIOT","The corect answer is",i["correct_ans"])
    print("Your score is",score,"out of 5")

Quiz()