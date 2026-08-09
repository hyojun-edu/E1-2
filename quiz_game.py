from input_util import get_selection
from exceptions import ExitSignalException

class QuizGame:
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
      exit_msg="종료 신호를 받았습니다. 안전하게 종료합니다")
    return choice

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
  QuizGame().run()
