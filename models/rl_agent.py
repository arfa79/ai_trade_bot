import gym
from gym import spaces
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

class TradingEnv(gym.Env):
    def __init__(self, df):
        self.df = df
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,))  # -1=all sell, 1=all buy
        self.observation_space = spaces.Box(
            low=-np.inf, 
            high=np.inf, 
            shape=(df.shape[1],))  # Features: close, volume, RSI, etc.
        
    def reset(self):
        self.current_step = 0
        return self.df.iloc[self.current_step].values
    
    def step(self, action):
        self.current_step += 1
        done = self.current_step >= len(self.df) - 1
        reward = self._calculate_reward(action)
        obs = self.df.iloc[self.current_step].values
        return obs, reward, done, {}

    def _calculate_reward(self, action):
        # Reward = profit if correct action, penalty if wrong
        price_diff = self.df.iloc[self.current_step]['close'] - self.df.iloc[self.current_step-1]['close']
        return action[0] * price_diff

def train_rl_agent(df):
    env = TradingEnv(df)
    check_env(env)  # Validate environment
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10_000)
    return model