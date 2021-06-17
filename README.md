# Background
So, nowadays the popular Prisoner's Dilemma variant is the Prisoner's Trilemma, where there are three options. I can easily see that being increased, so I figured
> Why settle for *three* options, when we can have ***INFINITE*** options?

Therefore, I created the Floating Point Prisoner's ?Lemma.

# Technical Stuff
Create a bot that can play this Python implementation of the Prisoner's ?Lemma. Make two functions, `strategy` and `plan`, that are in a similar format as the below examples.
```python
def strategy(is_new_game):
  # Put Stuff Here™. is_new_game tells the function if it's a new game. returns a value between 0 and 1, where 1 = coop and 0 = defect, and in-between stuff correlates to probability of coop or defect.
def plan(opmove):
  # opmove is the opponents move last round. This function shouldn't return anything. Put pass here if you don't use this.
```
# Forbidden Stuff
* Standard Loopholes are forbidden.
* No interacting with the controller other then by returning values in the strategy function.
* No interference with other bots (with global variables, other stuff) (You can have your bot interact with itself through global vars, for example, for communication)
* More stuff may be added
# Generic Stuff
Global vars are allowed. It uses an equation from the wonderful fellows at https://math.stackexchange.com to determine what to do, with the floating point numbers correlating to probability of coop or defect. However, the controller is deterministic in terms of the scoring stuff, and the probabilities are not treated as probabilities. The equations are in the play function in the controller.

**NOTE:** <s>Right now, the controller can only handle 11 bots, because the score array has a length of 11. I'll increase or fix this when it becomes a problem.</s> Problem hopefully fixed.
## Example Bots
♫Coop Bop Bot♫
```python
#Example Contestant
def strategy(is_new_game):
  return 1

def plan(opmove):
  pass
```
Random
```python
#Example Contestant
import random
def strategy(is_new_game):
  return random.random()
def plan(opmove):
  pass
```

Controller is at https://github.com/4D4850/KotH-Floating-Dilemma

Feel free to make a pull request.
