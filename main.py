import json
import random
import time 
from datetime import datetime, timedelta

class Flashcard:
  def __init__(self, question,answer):
    self.question = question
    self.answer = answer
    self.next_review = datetime.now() 
    self.interval = 1

def load_flashcards(filename):
  try:
    with open(filename, 'r') as f:
      flashcards = json.load(f)
      return [Flashcard(**fc) for fc in flashcards]
  except FileNotFoundError:
    return[]

def save_flashcards(flashcards,filename):
  with open(filename, 'w') as f:
        json.dump([fc.__dict__ for fc in flashcards], f, default=str)

def main():
  filename='flashcards.json'
  flashcards= load_flashcards(filename)
  while True:
      due_flashcards = [fc for fc in flashcards if fc.next_review <= datetime.now()]
      if not due_flashcards:
          print("No flashcards to review right now. Take a break!")
          time.sleep(60)
          continue
      flashcards= random.choice(due_flashcards)
      print(f"question: {flashcards.question}")
      input("press enter to see answer")  
      print(f"answer : {flashcards.answer}")
      correct = input("Did you get it right? (y/n): ").strip().lower()
      if correct == 'y':
          flashcard.interval *= 2
      else:
          flashcard.interval = 1

      flashcard.next_review = datetime.now() + timedelta(days=flashcard.interval)
      save_flashcards(flashcards, filename)
      print(f"Next review for this card in {flashcard.interval} day(s).")

def add_flashcard():
  filename = 'flashcards.json'
  flashcards = load_flashcards(filename)

  question = input("Enter the question: ").strip()
  answer = input("Enter the answer: ").strip()
  flashcards.append(Flashcard(question, answer))

  save_flashcards(flashcards, filename)
  print("Flashcard added successfully!")

if __name__ == "__main__":
  while True:
      print("1. Review flashcards")
      print("2. Add new flashcard")
      print("3. Quit")
      choice = input("Choose an option: ").strip()

      if choice == '1':
          main()
      elif choice == '2':
          add_flashcard()
      elif choice == '3':
          break
      else:
          print("Invalid choice. please try again" ) 

      

    
     
      

