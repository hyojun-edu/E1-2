from exceptions import InvalidInputException, ExitSignalException


def get_selection(
    min_value=0, 
    max_value=4, 
    input_msg="선택: ",
    err_msg="입력이 올바르지 않습니다. 다시 입력해주세요.",
    exit_msg="종료 시그널을 받았습니다. 저장 후 안전하게 종료합니다."
) -> int:
  selection = None
  try:
    while selection is None:
      try:
        try:
          selection = int(input(input_msg).strip())
        except ValueError:
          raise InvalidInputException

        if selection < min_value or selection > max_value:
          raise InvalidInputException

        return selection

      except InvalidInputException:
        print(err_msg)
        selection = None
        continue
      
  except (KeyboardInterrupt, EOFError):
    print(f"\n{exit_msg}")
    raise ExitSignalException


if __name__ == "__main__":
  try:
    print(f"{get_selection()} 선택됨")
  except ExitSignalException:
    print("(종료 시그널 시나리오 처리)")
