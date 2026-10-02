from quiz import run_quiz
from science import science_questions
from sport import sport_questions
from movie import movie_questions
print("QUIZ MENU")
print("1. Science")
print("2. Sport")
print("3. Movies")
choice = input("Choose a category (1-3): ")
if choice == "1":
   score = run_quiz(science_questions)
elif choice == "2":
   score = run_quiz(sport_questions)
elif choice == "3":
   score = run_quiz(movie_questions)
else:
   print("Invalid choice!")