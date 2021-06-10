class Controller:
  def __init__(self, names, strategy, plan):
    self.names = names
    self.strategy = strategy
    self.points = [0, 0]
    self.plan = plan

  def play(self, is_new_game):
    a = self.strategy[0](is_new_game)
    b = self.strategy[1](is_new_game)
    self.points[0] += a * b * 2 + (1 - a) * b * 3 + (1 - a) * (1 - b)
    self.points[1] += a * b * 2 + a * (1 - b) * 3 + (1 - a) * (1 - b)
    self.plan[0](b)
    self.plan[1](a)
  def run(self, numgames):
    self.play(1)
    for _  in range(numgames):
      self.play(0)

    print(f"Results: {self.points}")
    return self.points