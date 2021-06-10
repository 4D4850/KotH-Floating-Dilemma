#Example Contestant
def strategy(is_new_game):
  global mymove
  if is_new_game == 1:
    mymove = 1
    return mymove
  return mymove

def plan(opmove):
  global mymove
  mymove = opmove
