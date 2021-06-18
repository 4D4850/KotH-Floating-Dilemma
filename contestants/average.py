def strategy(is_new_game, store):
  if store['move']:
    if(store['mylast']):
      store['mylast'] = (store['move'] + store['mylast']) / 2
    store['mylast'] = (store['move'] + .5) / 2
  store['mylast'] = .5
  return store['mylast']

def plan(opmove, store):
  store['move'] = opmove

