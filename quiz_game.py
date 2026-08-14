import sys
from typing import List

from input_util import get_selection
from exceptions import ExitSignalException
from quiz import Quiz


class QuizGame:
  def __init__(self):
    self.state = {}
    self.state["quizzes"] = self.load_quizzes()


  def load_quizzes(self) -> List[Quiz]:
    quizzes = None
    # TODO: load quizzes from file

    if not quizzes:
      quizzes = [
        Quiz("중국의 수도는?", ["상하이", "베이징", "칭다오", "하이난"], 2),
        Quiz("러시아의 수도는?", ["샹트페테르부르크", "블라디보스토크", "모스크바", "카잔"], 3),
        Quiz("일본의 수도는?", ["도쿄", "교토", "삿포로", "오사카"], 1),
        Quiz("북한의 수도는?", ["함흥", "청진", "개성", "평양"], 4),
        Quiz("대만의 수도는?", ["타이중", "타이난", "타이베이", "타오위안"], 3),
      ]

    return quizzes


  def show_title(self):
    print()
    print("========================================")
    print("        🎯 나만의 퀴즈 게임 🎯          ")
    print("========================================")


  def show_menu(self):
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


  def show_menu_input(self, max_value=5) -> int:
    print("========================================")
    choice = get_selection(
      max_value=5)
    return choice


  def run(self):
    try:
      while True: 
        quiz_game = QuizGame()
        quiz_game.show_title()
        quiz_game.show_menu()

        choice = quiz_game.show_menu_input()
        match choice:
          case 1:
            self.play_quiz()
          case 2:
            pass
          case 3:
            pass
          case 4:
            pass
          case 5:
            self.save_and_exit()
          case _:
            print("입력이 올바르지 않습니다. 다시 입력해주세요.")
    except ExitSignalException:
      self.save_and_exit()


  def play_quiz(self):
    # TODO: 몇 문제를 풀지 선택할 수 있다.
    quizzes = self.state["quizzes"]
    # TODO: 

    n = len(quizzes)

    self.quiz_count = {
      "correct": 0,
      "total": n
    }

    if n == 0:
      print("풀 수 있는 문제가 없습니다.")
      return

    print()
    print(f"📝 퀴즈를 시작합니다! (총 {n}문제)")

    for i, quiz in enumerate(quizzes):
      print()
      print("----------------------------------------")
      print(f"[문제 {i+1}]")
      print(quiz.question)
      # TODO: 풀이 중 힌트를 볼 수 있다.
      for j, choice in enumerate(quiz.choices):
        print(f"{j+1}. {choice}")

      try:
        choice = quiz.show_quiz_input()

        # TODO: 힌트 사용시 점수 차감로직을 구현한다.
        result = quiz.show_quiz_result(choice)

        if result == True:
          self.quiz_count["correct"] += 1
          pass
      except ExitSignalException:
        self.save_and_exit()

    self.show_quiz_result()


  def show_quiz_result(self):
    correct_quiz_count = self.quiz_count['correct']
    total_quiz_count = self.quiz_count['total']
    score = (correct_quiz_count * 100) // total_quiz_count

    print("========================================")
    print(f"🏆 결과: {total_quiz_count}문제 중 {correct_quiz_count}문제 정답! ({score}점)")
    # TODO: 최고 점수 갱신 확인해서 추가 메시지 표시하기
    # print("🎉 새로운 최고 점수입니다!")
    print("========================================")


  def save_and_exit(self):
    # TODO: self.state 값을 json으로 저장히고 끝내기
    sys.exit(0)


if __name__ == "__main__":
  quiz_game = QuizGame()
  for quiz in quiz_game.state["quizzes"]:
    print(quiz.question, quiz.choices, quiz.answer)

  quiz_game.run()
