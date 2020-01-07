"""
Unit test for MuJoCo's robots in dm_control universe
"""
import itertools
from dm_control2gym.util import make_dm2gym_env_obs

env = make_dm2gym_env_obs(env_name="cheetah_run", num_repeat_action=1)

obs = env.reset()
print("Obs shape: ", obs.shape)

total_reward = 0

for t in itertools.count():
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    total_reward += reward

    if done: break

env.close()
print("Total Reward: {}".format(total_reward))
