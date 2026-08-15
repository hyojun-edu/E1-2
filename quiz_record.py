import datetime


class QuizRecord:
  def __init__(
    self,
    timestamp: float,
    total: int,
    correct: float
  ):
    self.timestamp = timestamp
    self.total = total
    self.correct = correct

  def to_dict(self):
    return {
      "timestamp": self.timestamp,
      "total": self.total,
      "correct": self.correct
    }