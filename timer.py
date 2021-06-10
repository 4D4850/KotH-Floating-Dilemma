import time

times = {}

def timer(bot, func):
  times[bot] = 0
  def timid(*args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    times[bot] += end - start
    return result
  return timid
