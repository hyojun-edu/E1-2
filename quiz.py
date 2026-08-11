from typing import List
from input_util import get_selection
from exceptions import ExitSignalException

class Quiz:
  def __init__(
    self, 
    question: str, 
    choices: List[str], 
    answer: int # choices 중 정답의 위치(index+1) 표시
  ):
    self.question = question
    self.choices = [*choices]
    self.answer = answer

  def show_quiz(self, number: int):
    print(f"[문제 {number}]")
    print(self.question)
    print()
    for i, choice in enumerate(self.choices):
      print(f"{i+1}. {choice}")
  
  def show_quiz_input(self) -> int:
    choice = get_selection(
      input_msg="정답 입력: ",
      max_value=len(self.choices))
    return choice
  
  def show_quiz_result(self, choice) -> bool:
    if choice == self.answer:
      print("✅ 정답입니다!")
      return True
    else:
      print("❌ 오답입니다!")
      return False


if __name__ == '__main__':
  quizes = [
    Quiz('questions', [], -1), # 정답이 입력되지 않은 상태의 문제
    Quiz('알파벳 첫 글자는?', ['A', 'B', 'C'], 1)
  ]

  try:
    for i, quiz in enumerate([quiz for quiz in quizes if quiz.answer > 0]):
      quiz.show_quiz(i + 1)
      choice = quiz.show_quiz_input()
      result = quiz.show_quiz_result(choice)
      if result:
        print("점수 1점 획득")
      else:
        print("점수 획득 실패")
  except ExitSignalException:
    print("(현재까지 푼 문제수, 점수 기록 후 종료)")
