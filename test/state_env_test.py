"""
Unit test for MuJoCo's robots in dm_control universe
"""
import itertools
from dm_control2gym.util import make_dm2gym_env_state

env = make_dm2gym_env_state(env_name="cheetah_run")

state = env.reset()
print("State shape: ", state.shape)

total_reward = 0

for t in itertools.count():
    action = env.action_space.sample()
    state, reward, done, _ = env.step(action)
    total_reward += reward

    if done: break

env.close()
print("Total Reward: {}".format(total_reward))
