''' 
This file be the primary driver for running a variant of rotting/non-stationary contextual bandits. 
The notion is that rewards may decay over time as the "best" arm may be over used. This creates a change
in what would be considered the best arm. The idea behind this notional environmental set-up is that
patients bodies become resistant or build a tolerance toward certain medications, ads lose their effect
the more frequently they are served... In a way, you could consider this non-stationarity to be a form of 
inverse novelty.

There are a couple of different ways that I've considered implementing the nonstationarity... 
    I: The distributions of reward have a temporal component (decaying or improving) that influence their magnitude
    II: The reward can be considered a resource. High potential reward with fewer draws vs. medium potential reward with many draws vs. low/no reward with infinite draws
    III: Similar to II but the resources can be replenished if the different arms are left alone for a period of time.

The real challenge is determining how to best organize an algorithm to stay somewhat flexible as many Contextual Bandit 
approaches converge to a fixed/static policy after some time. There have been a couple of papers that have dealt with
this. I'm needing to read them to get a better idea of what I need to do to differentiate my work from theirs as well 
as build upon already "proven" methods.
    "Stochastic MAB Problem with Non-stationary Rewards": https://papers.nips.cc/paper/5378-stochastic-multi-armed-bandit-problem-with-non-stationary-rewards.pdf
    "Rotting Bandits": https://arxiv.org/pdf/1702.07274.pdf
    "Efficient Contextual Bandits in Non-Stationary Worlds": https://arxiv.org/pdf/1708.01799.pdf
    "Contextual GP Bandit Optimization": http://www.ong-home.my/papers/krause11cgp-ucb.pdf


 Nov. 2019 by Taylor Killian, University of Toronto
----------------------------------------------------------------------------------------
Notes:
      
'''