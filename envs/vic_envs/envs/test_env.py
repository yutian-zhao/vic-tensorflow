import gymnasium as gym
from gymnasium import error, spaces, utils
from gymnasium.utils import seeding


class TestEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode="human", close=False):
        pass
