

import numpy as np
from pysc2.agents import base_agent
from pysc2.lib import actions, features
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers.convolutional import Conv2D

class CNNAgent(base_agent.BaseAgent):
  def __init__(self):
    super(CNNAgent, self).__init__()

    self.model = Sequential()
    self.model.add(Conv2D(16, (3, 3), padding='same', input_shape=(64, 64, 3), activation='relu'))
    self.model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    self.model.add(Flatten())
    self.model.add(Dense(256, activation='relu'))
    self.model.add(Dense(1, activation='sigmoid'))
    self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

  def step(self, obs):
    super(CNNAgent, self).step(obs)

    # Your code here
    return actions.FunctionCall(0, [])

    