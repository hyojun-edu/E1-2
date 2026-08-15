## 프로젝트 개요
 - 터미널에서 동작하는 수도 맞추기 퀴즈 게임을 처음부터 끝까지 구현

## 퀴즈 주제 선정 이유
 - 기본 상식을 키우기 위해서

## 실행 방법
```
python3 app.py
```

## 기능 목록
 - 프로그램 실행 시 메뉴 출력 
 - 기본 퀴즈 데이터 제공
 - 퀴즈 풀기
   - 저장된 퀴즈를 랜덤 출제
   - 문제 수 선택
   - 힌트 기능 사용시 점수 차감
   - 정답 입력
   - 정답/오답 여부를 알려줌
   - 모든 문제를 풀면 결과를 표시
 - 퀴즈 추가/삭제
 - 퀴즈 목록
 - 최고 점수 확인
 - 점수 기록 히스토리 (날짜/시간, 푼 문제 수, 점수)

## 파일 구조
 - app.py: QuizGame 생성 및 실행
 - exceptions.py: 예외처리를 위한 커스텀 exception 정의
  - InvalidInputException - 범위 밖의 입력이 들어왔을 때
  - ExitSignalException - KeyboardInterrup, EOF 입력되었을 때
 - input_util.py: 사용자 입력을 받는 유틸리티 함수 정의
  - get_selection - min_value~max_value사이의 숫자 입력만 허용하는 입력 UI 띄우고 선택된 값 반환
 - quiz.py: 퀴즈 데이터 관리 및 정답 판정 로직을 위한 Quiz 클래스 정의
  - 속성:
   - question: 퀴즈 질문
   - choices: 선택지
   - answer: 정답 번호
   - hint: 힌트
  - 메소드:
   - show_quiz: 퀴즈 내용 출력
   - show_quiz_input: 퀴즈 정답 입력 UI 띄우기
   - show_quiz_result: 퀴즈 정답 여부 출력 및 판정 결과 반환
   - to_dict: dict으로 변환 (json 저장시 사용)
 - quiz_record.py: 퀴즈 기록 데이터 담기 위한 QuizRecord 클래스 정의
  - 속성:
   - timestamp: 1970-01-01부터 초 단위 경과시간 (datetime.datetime.timestamp() 값)
   - total: 전체 문제 수
   - correct: 맞춘 문제 수
  - 메소드:
   - to_dict: dict으로 변환 (json 저장시 사용)
 - quiz_game.py: 퀴즈 게임 실행을 위한 QuizGame 클래스 정의
  - 속성: 
    - quizzes: 퀴즈 데이터
    - current_record: 현재 게임 기록
    - best_score: 최고 게임 기록
    - records: 전체 게임 기록
  - 메소드: 
    - run: 퀴즈 게임 어플리케이션 실행
    - load_quizzes: 퀴즈 불러오기(state.json 없으면 기본 퀴즈셋 로드)
    - show_title: 퀴즈 게임 타이틀 출력
    - show_menu: 퀴즈 게임 메뉴 출력
    - show_menu_input: 퀴즈 게임 메뉴 입력 받는 UI 띄우기
    - play_quiz: 퀴즈 풀기
    - show_quiz_result: 퀴즈 풀기 결과 출력
    - add_quiz: 퀴즈 추가하기
    - show_quiz_list: 퀴즈 목록 출력
    - delete_quiz: 퀴즈 삭제하기
    - show_records: 전체 게임 기록 및 최고 점수 출력
    - save: 현재 상태 저장하기
    - save_and_exit: 현재 상태 저장하고 종료하기

## 데이터 파일 설명(state.json)
 - best_score
  - total: int - 전체 퀴즈 수
  - correct: float - 맞춘 퀴즈 수 (힌트 사용시 소수점 단위로 차감될 수 있어 float 사용)
 - quizzes: List[Quiz]
  - question: str - 퀴즈 문제
  - choices: List[str] - 선택지 배열
  - answer: int - 정답 번호
  - hint: Optional[str] - 힌트 (생략 가능)
 - records: List[QuizRecord]
  - timestamp: float - 퀴즈 종료 시간
  - total: int - 전체 퀴즈 수
  - correct: float - 맞춘 퀴즈 수 (힌트 사용시 소수점 단위로 차감될 수 있어 float 사용)

## 스크린샷
 - 개발 환경 설정 스크린샷 + `git log --oneline --graph` 결과 스크린샷
<img width="1443" height="1152" alt="개발환경 세팅 + git 로그" src="https://github.com/user-attachments/assets/42651ecc-0952-4496-bbe6-01a27de28c47" />

 - 프로그램 실행 결과 스크린샷
 
   - 메뉴
<img width="439" height="245" alt="image" src="https://github.com/user-attachments/assets/bbfeeb5d-983c-4163-a681-40f466d800ae" />

   - 퀴즈 추가
<img width="462" height="225" alt="image" src="https://github.com/user-attachments/assets/51d97d3e-a68c-48b6-8768-b5ddb24b176b" />

   - 목록
<img width="429" height="245" alt="image" src="https://github.com/user-attachments/assets/4e4d0034-5f94-4f74-8ce3-62914f13e371" />

   - 플레이
<img width="420" height="628" alt="image" src="https://github.com/user-attachments/assets/f0edb68a-79d4-491e-bff3-e52954515472" />

   - 점수
<img width="442" height="323" alt="image" src="https://github.com/user-attachments/assets/ec8e506a-5c3b-41e8-9f72-ad98eb5c6e3a" />

   - 삭제
<img width="452" height="101" alt="image" src="https://github.com/user-attachments/assets/982e2d18-ebc4-4b17-9788-8ef0fdb856d4" />
