# Floating Point Prisoners Dilemma

## Background
So, nowadays the popular Prisoner's Dilemma variant is the Prisoner's Trilemma, where there are three options. I can easily see that being increased, so I figured
> Why settle for *three* options, when we can have ***INFINITE*** options?

Therefore, I created the Floating Point Prisoner's ?Lemma.




## Equations:

Each round, your score will be calculated as (\$a\$ is what Player 1 returns, \$b\$ is what Player 2 returns):

$$
\text{Player 1 expected score: }\quad 2ab+3(1-a)b+(1-a)(1-b)
$$

$$
\text{Player 2 expected score: }\quad 2ab+3a(1-b)+(1-a)(1-b)
$$

\$3\$ is the temptation payoff, the payoff \$a\$ gets if \$a\$ defects and \$b\$ cooperates. \$2\$ is the reward, for if both cooperate. \$1\$ is the punishment, for if both defect. The sucker's payoff is \$0\$, which is what \$a\$ gets when \$a\$ cooperates and \$b\$ defects.

### Explanation of what floating point numbers mean in output

Basically, an output of 0.5 means that the figurative probability (The controller is almost deterministic, only matching up contestants at random) of cooperation is 0.5. This means that since the output is closer to 1 than 0 is, the opponent gets some score, but not as much as if the output of the contestant we're focusing on was 1.

## Forbidden Stuff
* Standard Loopholes are forbidden.
* No interacting with the controller other then by returning values in the strategy function.
* No interference with other bots (with global variables, other stuff)
* Global Vars are Highly Discouraged. Instead, use the store dict.
* More stuff may be added
## Generic Stuff
It uses an equation from the wonderful fellows at https://math.stackexchange.com to determine what to do, with the floating point numbers correlating to probability of coop or defect. However, the controller is deterministic in terms of the scoring stuff, and the probabilities are not treated as probabilities. The equations are in the play function in the controller.


## Technical Stuff
Create a bot that can play this Python implementation of the Prisoner's ?Lemma. Make two functions, `strategy` and `plan`, that are in a similar format as the below examples.
```python
def strategy(is_new_game, store):
  # Put Stuff Here™. is_new_game tells the function if it's a new game. returns a value between 0 and 1, where 1 = coop and 0 = defect, and in-between stuff correlates to probability of coop or defect. Store is a dict for storage.
def plan(opmove, store):
  # opmove is the opponents move last round. This function shouldn't return anything. Put pass here if you don't use this.
```
### Example Bots

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
