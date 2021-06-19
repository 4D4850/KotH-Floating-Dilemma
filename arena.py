import sys
import webbrowser

from controller import Controller
from timer import timer, times
from random import randint

from contestants import coop
from contestants import random
from contestants import helped
from contestants import randalt
from contestants import tit_for_tat

contestants = [
  ("Cooperator", coop.strategy, coop.plan),
  ("Random", random.strategy, random.plan),
  ("Helped", helped.strategy, helped.plan),
  ("Random Alternator", randalt.strategy, randalt.plan),
  ("Tit for Tat", tit_for_tat.strategy, tit_for_tat.plan),
]


contestants = [[x[0], timer(x[0], x[1]), timer(x[0], x[1])] for x in contestants]
scores = [0] * len(contestants)
wins = [0] * len(contestants)

game = 0
repeats = 100
score_array = []
for i in range(len(contestants) + 1):
  score_array.append([i, 0])
for k in range(repeats):
  if "-i" in sys.argv or "--import-antigravity" in sys.argv:
    print("Ooh! an undocumented feature!")
    webbrowser.open("https://xkcd.com/353/")
  if "-s" in sys.argv or "--open-question" in sys.argv:
    print("Sorry, this feature hasn't been implemented ^yet.^ That\'s sad. :(")
    #Make sure to make it open the question in CGCC
  number_of_games = 99
  for i in range(len(contestants)):
    for j in range(i + 1):
      contestant = contestants[i]
      opponent = contestants[j]
      print(f"{game}/{int(len(contestants) * (len(contestants) + 1) * repeats / 2)}", end="\r")
      game += 1
      ctrl = Controller((contestant[0], opponent[0]), (contestant[1], opponent[1]), (contestant[2], opponent[2]))
      result  = ctrl.run(number_of_games)

      scores[i] += result[0] / repeats
      scores[j] += result[1] / repeats

      print(f"Contestants: {contestant[0]}, {opponent[0]}")

      print(f"Scores: {scores[i]}, {scores[j]}")

      if contestant == opponent:
        continue
      if result[0] > result[1]:
        wins[i] += 1 / repeats
      elif result[0] < result[1]:
        wins[j] += 1 / repeats
      else:
        wins[i] += 0.5 / repeats
        wins[j] += 0.5 / repeats
      for l in range(j + 2):
        if i == l:
          score_array[l][1] += scores[i]
        elif j == l:
          score_array[l][1] += scores[j]
      print(score_array)
ordered_score = sorted(zip(contestants, scores), key=lambda x: x[1], reverse=True)
ordered_wins = sorted(zip(contestants, wins), key=lambda x: x[1], reverse=True)

overall = {}
ordered_times = [[a, b] for a, b in times.items()]
ordered_times = sorted(ordered_times, key=lambda x: x[1], reverse=True)

def joint_rank(sorted_list, key):
  last = -1
  rank = 0
  buffer = 0
  out = []
  for item in sorted_list:
    score = key(item)
    if score != last:
      rank += buffer + 1
      buffer = 0
    else:
      buffer += 1
      out.append((item, rank))
      last = score
  return out


print("By Score: \n")
for i in range(len(contestants)):
  print(f"{contestants[i][0]}, {score_array[i][1]}")
