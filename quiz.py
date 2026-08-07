from typing import List

class Quiz:
  def __init__(
    self, 
    question: str, 
    choices: List[str], 
    answer: int # choices 중 정답의 index 표시
  ):
    self.question = question
    self.choices = [*choices]
    self.answer = answer

if __name__ == '__main__':
  Quiz('questions', [], -1) # 정답이 입력되지 않은 상태의 문제

