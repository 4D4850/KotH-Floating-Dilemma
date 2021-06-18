import random
def strategy(is_new_game, store):
  if is_new_game:
    store["array"] = [0, 0]
  if is_new_game or store["array"][0]%100 < 10:
    store["array"][1] += 1
    return random.random()
  else:
      store["array"].append(store["array"][1] + 1, (sum(store["array"])/len(store["array"])))
      store[1] += 1
      return sum(list(store["array"])[1:])/len(list(store["array"])[1:])
def plan(opmove, store):
  store["array"].append(store["array"][1] + 1, opmove)
  store["array"][1] += 1
  store["array"][0] += random.random() + random.random()

