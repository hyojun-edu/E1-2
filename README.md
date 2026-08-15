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

## 요구변경 시 수정 위치
 - 각 기능에 따라 메소드가 QuizGame에 나누어져 구현되어 있기 때문에 요구사항 변경 발생시 해당 메소드의 내용을 찾아 수정하면 됨
 - 퀴즈 풀기 및 점수 계산 로직 -> QuizGame.play_quiz
 - 퀴즈 추가하기 -> QuizGame.add_quiz
 - 퀴즈 삭제하기 -> QuizGame.delete_quiz
 - 퀴즈 목룍보기 -> QuizGame.show_quiz_list
 - 퀴즈 점수보기 -> QuizGame.show_records

## 클래스 사용 이유(장점) 및 함수 대비 차이점
 - 클래스를 사용하면 매번 데이터(속성)을 파라미터로 넣어줄 필요 없이 메소드에서 클래스의 변수를 읽어 기능을 수행할 수 있다
 - 또한, 데이터가 바로 클래스에 저장되기 때문에 별도로 데이터를 관리하는 변수를 둘 필요가 없다
 - 일회성으로 입력을 받는 등의 간단한 동작은 그냥 함수를 사용해도 충분하다

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

## best_score 필드 설계 시 중첩 구조 선택 이유
 - 단순 정답 밎춘 수 혹은 점수만 기록해서는 전체 중에 얼마나 맞추었는지를 표시할 수 없음
 - 하나의 필드에 거의 항상 같이 사용되는 값 2개를 같이 저장함으로써 데이터 관리를 편리하게 설계함

## JSON 저장 형식을 선택한 이유
 - json은 데이터를 저장하는데 널리 사용되는 형식으로 많은 언어와 어플리케이션에서 지원되기 때문에 선택
 - 가동성이 좋고 텍스트, 숫자, 리스트, 딕셔너리 형식의 데이터를 저장하기에 적절한 형식임
 - 데이터를 human-readable format으로 저장하다보니 용량 낭비가 발생할 수 있음 (예를 들어, 같은 key를 가진 오브젝트가 리스트 안에 많이 있는 경우 key 문자열이 리스크 크기만큼 반복되어 나타남)

## 대용량 데이터(퀴즈 1000개 이상 확장 시) 대응 방안
 - 성능/메모리·검색 한계가 발생할 수 있음
   - 모든 퀴즈를 한번에 다 메모리에 올려야 함
   - 적절한 검색 매커니즘이 구현되어있지 않아서 특정 문제를 찾아야할 때 모든 퀴즈의 데이터에 대해서 탐색 필요
  - 대용량 데이터로 확장해야 할 때는 DB 도입을 고려
   - index를 이용한 검색 가능
   - 모든 데이터를 로드하지 말고 현재 읽고 써야하는 데이터 범위만 로드해서 사용

## 예외 발생 사례(권한·파일손상 등)와 복구 구현사항
 - 예외 발생시 자동으로 현재 상태를 저장한 다음 사용자 안내 후 종료
 - 만약 파일에 문제가 있어 로드할 수 없는 경우 어플리케이션의 state을 초기값으로 생성하여 종료시 저장하여 state.json파일을 정상 상태로 복구

## 커밋 단위·메시지 규칙(단위 설명, 메시지 템플릿 등)
 - 커밋 단위: 가능한한 하나의 기능 단위로 커밋
 - 메시지 규칙: 무의미한 메시지는 금지, 어떤 작업이 이루어졌는지 쉽게 알 수 있도록 요약해서 기록
 - 메시지 템플릿
   - Feat: {작업내용}
   - Docs: {작업내용}
   - Refactor: {작업내용}

## 브랜치 전략 병합 정책
 - 새로운 기능의 범위가 크다고 판단되는 경우 (기능 요구사항이 여러개, 수정해야하는 파일 여러개) 브렌치를 만들어서 작업
 - 작업이 완료된 다음 main 브렌치로 병합, 충돌 발생시 작업자가 다른 경우 논의해서 충돌 해결


## 스크린샷
 - 개발 환경 설정 스크린샷 + `git log --oneline --graph` 결과 스크린샷
   - 10개 이상의 커밋 확인 ✅
   - 브랜치 생성·병합 기록(merge 커밋 등) 확인 ✅
   - 
<img width="1443" height="1152" alt="개발환경 세팅 + git 로그" src="https://github.com/user-attachments/assets/42651ecc-0952-4496-bbe6-01a27de28c47" />
 - git 실행 로그
    - git clone, git pull, git push 등 명령어 실습 확인 ✅
<img width="776" height="459" alt="image" src="https://github.com/user-attachments/assets/096bf938-57b0-40e1-9268-4d22b277545d" />

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
