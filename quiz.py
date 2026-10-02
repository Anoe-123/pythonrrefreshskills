def run_quiz(questions):
   score = 0
   for question, answer in questions.items():
       user_answer = input(question + " ")
       if user_answer.lower() == answer.lower():
           print("Correct!")
           score += 1
       else:
           print("Wrong!")
   print("Final Score:", score, "/ 5")
   return score