Title: Mario Learning
Date: 2018-5-27 23:21
Tags: thats, awesome, ML, emulation
Category: yeah
Slug: mario-learning

# Part 4. Reinforcement Learning - Q-Learning

Now we have everything set up and the basic random policy. Mario would have to be super lucky to get anywhere with this.
It's time to improve the policy.

![mario learning]({static}/images/rl/mario-learning.jpg)

I'm going to use the reinforcement learning technique of deep Q-learning.

## Deep Q-Learning

This is the algorithm [deepmind](http://arxiv.org/abs/1312.5602) used when learning to play atari games.
There are a few concepts we need to go over first.

### Markov Decision Process

This is a topic in itself. For more detail see [here](https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/markov_decision_process.html).  
Basically it means we can transition around states using actions. For the algorithm to work we need an interesting property to hold, the Markov property.

> The probability of the next state s<sub>i+1</sub> depends only on current state s<sub>i</sub> and performed action a<sub>i</sub>, but not on preceding states or actions.

This essentialy means that to calculate the next state we only need to know the current state and action. How we got to this state and all the history we can ignore.  


### Discounted Future Reward

How do we know how good the current state is? we can add up all of the future rewards.
How much do rewards in the present count over rewards in the future?  We can add a discount factor, such that present values aren't discounted much and those in the future are discounted heavily (up to a point where it discounts the reward to zero in the further future). This constrains the future reward calculation and also handles the uncertainty that future actions bring.


> R<sub>t</sub> = r<sub>t</sub> + γ(r<sub>t+1</sub> + γ(r<sub>t+2</sub> + …)) = r<sub>t</sub>+γR<sub>t+1</sub>


γ (lamda) is the discount factor ranging from 0 to 1.  
0 means we only consider the next step.  
1 means actions in the far future have equal weight to those near the present.


### Exploitation vs Exploration (ϵ-greedy)

We go to one restaurant and we really like the food. Next time we can go to the same restaurant where we know the food is nice, or we can go to another restaurant and run the risk the food being poor or even better than the first. This is the basic idea of, do we have the agent do the best action each time (greedy approach) or do we have it explore new avenues that initially look worse but could lead to better long term rewards.

Exclusively following the greedy route will often lead to a sub optimal solution. Exclusively following the random approach means the agent may be learning but it is never applying the learning and we end up with a sort of drunkards walk.

(ϵ = epsilon)  
The common strategy here is called the ϵ-greedy approach.
At the start the agent picks random actions (explore) as we know little about the environment. As it starts to learn we reduce the chance of random actions and increase the chances of learned actions (exploit). Later on the agent reaches a point where it's mostly doing learned actions. We can stop reducing the random choice odds from now on. We still want some exploration so we don't reduce ϵ to zero, just a low value.


In the implementation we transition through 3 states  
Explore -> Reducing Epsilon -> Static Epsilon

```python
OBSERVE = 50
INITIAL_EPSILON = 0.1
FINAL_EPSILON = 0.0001  # final value of epsilon
EXPLORE = 3000
```

```python
if random.random() <= epsilon:
    # Random Action
    action_index = random.randrange(NUM_ACTIONS)
    action[action_index] = 1
else:
    # Learned action
    q = model.predict(state_stack)
    ...

# We reduced the epsilon gradually
if epsilon > FINAL_EPSILON and tick > OBSERVE:
    epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE
```

### Q function

The discounted reward function above can be reduced to what is known as the Bellman equation. The reward the agent receives is equal to the current reward plus the maximum of the reward at the next step. 

> Q(s,a) = r + γ maxQ(s<sub>t+1</sub>, a<sub>t+1</sub>)

The idea behind q-learning is taht we can iterativel approximate Q

> Q<sub>t+1</sub>(s<sub>t</sub>,a<sub>t</sub>) = Q<sub>t</sub>(s<sub>t</sub>,a<sub>t</sub>) + α(r<sub>t+1</sub> + γ maxQ<sub>t</sub>(s<sub>t+1</sub>, a) - Q<sub>t</sub>(s<sub>t</sub>, a<sub>t</sub>))

α is the learning rate. One of the hyperperameters that will need tuning

This says for a state s and taking action a then Q is the exected reward. If we are exploting then we pick maxQ. 
(Another method is the agent picks the action from a probability distribution such that the maxQ will be chosen most often.)

To hold a mapping from screen to best action in mario land would require immense amounts of memory and take a very long time to calculate. We need something that can approximate this mapping.
Neural networks are also know as universal function approximators which we can use here to approximate Q. Hence the deep part of deep reinforcement learning.

```python
q = model.predict(state_stack)
max_Q = np.argmax(q)
action[max_Q] = 1
```

### Convolutional Neural Network model

The agents view of the world is a grey (green?) scale image. We need to stack 4 (current and 3 previous) of them on top of each to help the learning process gauge marios direction and velocity. If we just used a single frame the model wouldn't be able to tell if mario was falling or jumping.
(TODO - the learning stack size should be a hyperparameter)

We store these stacks in a big cache called the replay memory. This is one of the parts I thought was pretty innivative.
On each tick the agent doesn't run a learning cycle on the last action, it runs it on a random action from the past. If we only picked the last action then the known reward would only be from the last action taken as the future for the action hasn't yet happened. By picking a random action from the past we can get a decent calculation of the future reward from that old action by traversing the future of that old action in the cache.

### The model

We use a [convolutional network](https://medium.freecodecamp.org/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050) given our imput is images. After the convolution layers we flatten the data and pass it through a standard dense layer. The final output has 3 nodes, with each node containing the predicted weighting of each action (left, none, right). 


```python
def buildmodel():
    # Adapted from https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html
    print("Building the model ")

    model = Sequential()
    model.add(layers.Convolution2D(
        32, 8, 8, subsample=(4, 4), border_mode='same',
        input_shape=(IMG_ROWS, IMG_COLS, IMG_CHANNELS)))
    model.add(layers.Activation('relu'))
    model.add(layers.Convolution2D(
        64, 4, 4, subsample=(2, 2), border_mode='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Convolution2D(
        64, 3, 3, subsample=(1, 1), border_mode='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(512))
    model.add(layers.Activation('relu'))
    model.add(layers.Dense(3))

    adam = Adam(lr=1e-6)
    model.compile(
        loss='mse',
        optimizer=adam)
    print("We finish building the model")
    return model
```

### Running

Putting it all together and we can kick off some learning, woohoo!

There is a script in the [repo](https://github.com/garybake/PyBoy) called run_mario_test.sh that launches the client and server in parallel.  


<iframe width="560" height="315" src="https://www.youtube.com/embed/1NzQAoZR-E0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


### Tuning

This is the part where we would tune the model (both the network and the Q-learning parameters).
Unfortunately I'm running this on a laptop without a graphics card for accelerated learning. You can see on the video each step is really slow.
It starts slowish on the exploration phase and then slows right down when it starts learning. I'm not going to get enough cycles to even start tuning the network.

I've left it running for an hour and you can see a vague strategy developing. Mario wants to maximize his reward for running to the right. If he runs too far he gets killed by the first goomba. So he runs to the right and gets close to the goomba, then starts to zig zag back and forth collection the 'right' reward until he runs out of space and the goomba gets him. 

It's pretty neat. Looking at some of the strategies that evolve out of RL show you how powerful it can be.

### TODO

Phew, this is where I'm currently up to with it. There is more todo, primarily around speeding up the steps.
I think I need to run this on an aws instance with a decent gpu, but this means getting it running it headless but still rendering enough.
There is still plenty of fat to trim in the whole process.


### A third way?
Whilst writing this post Open AI [announced](https://blog.openai.com/gym-retro/) support for more consoles, including gameboy, happy days!  
[repo](https://github.com/openai/retro/tree/develop)  

Maybe there will Step 5 if I can get it working

### Shoutout

Finally a shoutout to a book that has been really helpful for me learning deep learning. It's written by the author of the keras library, and it's really approachable and understandable. I can't recommend it enough.

*(edited 05/02/23 to show second edition of book)*

[Deep Learning with python by François Chollet](https://www.manning.com/books/deep-learning-with-python-second-edition)

![Keras Book]({static}/images/rl/keras_book.jpg)

### Links

- [Part 1. GBakeBoy Emulator](./GBakeBoy.html)  
- [Part 2. Mario Environmental](./mario-environmental.html)  
- [Part 3. Mario Environment API](./mario-environment-api.html)  
- [Part 4. Reinforcement Learning - Q-Learning](./mario-learning.html)  
