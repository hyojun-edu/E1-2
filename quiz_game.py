import sys
from typing import List
import json
from random import sample

from input_util import get_selection
from exceptions import ExitSignalException
from quiz import Quiz

STATE_JSON_FILENAME = "state.json"

class QuizGame:
  def __init__(self):
    try:
      with open(STATE_JSON_FILENAME, 'r', encoding='utf-8') as f:
        state = json.load(f)
    except:
      state = {}
    
    self.best_score = state.get("best_score", 0)
    self.quizzes = self.load_quizzes(state.get("quizzes"))


  def load_quizzes(self, quizzes_from_state_json) -> List[Quiz]:
    if quizzes_from_state_json is not None and len(quizzes_from_state_json) > 0:
      quizzes = [
        Quiz(
          quiz_dict["question"], 
          quiz_dict["choices"], 
          quiz_dict["answer"],
          quiz_dict["hint"]
          ) for quiz_dict in quizzes_from_state_json
      ]
    else:
      quizzes = [
        Quiz("중국의 수도는?", ["상하이", "베이징", "칭다오", "하이난"], 2, "오리 요리로 유명한 도시!"),
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
    print("3. 퀴즈 삭제")
    print("4. 퀴즈 목록")
    print("5. 점수 확인")
    print("6. 종료")


  def show_menu_input(self, max_value=5) -> int:
    print("========================================")
    choice = get_selection(
      max_value=max_value)
    return choice


  def run(self):
    try:
      while True: 
        quiz_game = QuizGame()
        quiz_game.show_title()
        quiz_game.show_menu()

        choice = quiz_game.show_menu_input(max_value=6)
        match choice:
          case 1:
            self.play_quiz()
          case 2:
            self.add_quiz()
          case 3:
            # TODO: 퀴즈 삭제 구현
            pass
          case 4:
            self.show_quiz_list()
          case 5:
            # TODO: 점수 기록 히스토리 구현
            pass
          case 6:
            self.save_and_exit()
          case _:
            print("입력이 올바르지 않습니다. 다시 입력해주세요.")
    except ExitSignalException:
      self.save_and_exit()


  def play_quiz(self):
    n = len(self.quizzes)
    k = get_selection(
      input_msg=f"몇 문제 푸실건가요?(1~{n}): ",
      min_value=1,
      max_value=n)

    selected_quizzes = sample(self.quizzes, k)

    self.quiz_count = {
      "correct": 0,
      "total": k
    }

    if n == 0:
      print("풀 수 있는 문제가 없습니다.")
      return

    print()
    print(f"📝 퀴즈를 시작합니다! (총 {k}문제)")

    for i, quiz in enumerate(selected_quizzes):
      print()
      print("----------------------------------------")
      quiz.show_quiz(i+1)

      try:
        choice = quiz.show_quiz_input()

        if choice == 0:
          print(f"힌트: {quiz.hint}")
          self.quiz_count['correct'] -= 0.5
          choice = quiz.show_quiz_input(hint_used=True)

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
    score = int((correct_quiz_count * 100) // total_quiz_count)

    print("========================================")
    print(f"🏆 결과: {total_quiz_count}문제 중 {correct_quiz_count}문제 정답! ({score}점)")

    if (score > self.best_score):
      self.best_score = score
      print("🎉 새로운 최고 점수입니다!")
    print("========================================")


  def add_quiz(self):
    print()
    print("📌 새로운 퀴즈를 추가합니다.")

    question = input("문제를 입력하세요: ")
    n_choices = get_selection(
      input_msg="보기 수를 선택하세요(2~5): ", 
      min_value=2,
      max_value=5)
    choices = [input(f"선택지 {i+1}: ") for i in range(n_choices)]
    answer = get_selection(
      input_msg=f"정답번호 (1~{n_choices}): ",
      max_value=n_choices
    )
    hint = input("힌트(입력하지 않으려면 그냥 Enter키로 스킵): ")
    self.quizzes.append(Quiz(
      question=question,
      choices=choices,
      answer=answer,
      hint=hint if len(hint) > 0 else None
    ))
    self.save()


  def show_quiz_list(self):
    print()
    print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
    print()
    print("----------------------------------------")
    for i, quiz in enumerate(self.quizzes):
      print(f"[{i+1}] {quiz.question}")
    print("----------------------------------------")

  def save(self):
    with open(STATE_JSON_FILENAME, "w", encoding="utf-8") as f:
      json.dump({
        "best_score": self.best_score,
        "quizzes": [quiz.to_dict() for quiz in self.quizzes]
      }, f)

  def save_and_exit(self):
    self.save()
    sys.exit(0)


if __name__ == "__main__":
  quiz_game = QuizGame()
  quiz_game.run()
