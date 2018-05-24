Title: Mario Environment API
Date: 2018-5-24 12:38
Tags: thats, awesome, ML
Category: yeah
Slug: mario-environment-api

# Step 3. Build an api for the environment

Now that we can pull out information from the gameboy environment, why do we need to do this?

## Reinforcement learning overview

I'll discuss the basic premise of reinforcement learning (RL). 
RL mimics how we humans learn things in the real world. We do an action and then we observe the world around us, we then learn how good the action was through feedback from the environment. i.e. 

- I reach out to touch this radiator (action)  
- The radiator burns my hand (environment)  
- Pain in the hand (negative reward)  
- I learn not to touch a hot radiator (policy)  
- I may try again in the future though (exploration vs exploitation dilemma)  

There are 2 main parts:

- **Agent**  
In real life this is us. In the mario game this is our learning script. It is the part that learns and makes decisions about what action to take next.    

- **Environment**  
The things external to the agent. The world around us or the gameboy emulator.

Next the information that pass between the agent and environment

- **State**  
The current state of the environment. Usually a minimal set of information as we don't need to know everything about the outside world.
(I don't need to know the weather in Australia to drive my car in the UK)

- **Action**  
The action the agent is taking, pressing the brake pedal, smiling, pressing right on the dpad etc.
This may or may not produce a change in the environment

- **Reward**  
How good was the change in the environment caused by our last action. This is what we want to maximise.

<img src="images/rl/reinforcement-learning.jpg" alt="rl" style="height: 270px;"/>

In our mario world each timestep can be seen as discrete rather than continous. We press a button and the gameboy moves forward one tick.
There are RL methods to handle continuous time but discrete keeps things a lot simpler.


