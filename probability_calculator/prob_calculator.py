import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, balls):
    if balls >= len(self.contents):
      return self.contents
    else:
      drawn_balls = []
      for i in range(balls):
        ball = random.choice(self.contents)
        self.contents.remove(ball)
        drawn_balls.append(ball)
      return drawn_balls
      
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for n in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)
    correct = 0
    for key, item in expected_balls.items():
      if balls.count(key) >= item:
        correct += 1
    if correct == len(expected_balls):
      count += 1
  probability = count / num_experiments
  return probability