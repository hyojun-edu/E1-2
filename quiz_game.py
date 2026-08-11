from input_util import get_selection
from exceptions import ExitSignalException
from typing import List
from quiz import Quiz


class QuizGame:
  def __init__(self):
    self.quiz_list = self.load_quiz_list()

  def show_title(self):
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
      max_value=5,
      exit_msg="종료 신호를 받았습니다. 안전하게 종료합니다.")
    return choice

  def load_quiz_list(self) -> List[Quiz]:
    quiz_list = None
    # TODO: load quiz list from file

    if not quiz_list:
      quiz_list = [
        Quiz("중국의 수도는?", ["상하이", "베이징", "칭다오", "하이난"], 2),
        Quiz("러시아의 수도는?", ["샹트페테르부르크", "블라디보스토크", "모스크바", "카잔"], 3),
        Quiz("일본의 수도는?", ["도쿄", "교토", "삿포로", "오사카"], 1),
        Quiz("북한의 수도는?", ["함흥", "청진", "개성", "평양"], 4),
        Quiz("대만의 수도는?", ["타이중", "타이난", "타이베이", "타오위안"], 3),
      ]

    return quiz_list

  def run(self):
    try:
      while True: 
        quiz_game = QuizGame()
        quiz_game.show_title()
        quiz_game.show_menu()

        choice = quiz_game.show_menu_input()
        print(f"{choice} 입력됨")
    except ExitSignalException:
      pass # 메인 메뉴에서는 별도 처리없이 종료해도 안전함


if __name__ == "__main__":
  quiz_game = QuizGame()
  for quiz in quiz_game.quiz_list:
    print(quiz.question, quiz.choices, quiz.answer)

  quiz_game.run()
