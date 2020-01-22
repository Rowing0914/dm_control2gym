import itertools
from dm_control2gym.util import make_dm2gym_env_obs, DM_TASKS
from dm_control2gym.recorder import Monitor


for env_name, _ in DM_TASKS.items():
    print("=== Env: {} ===".format(env_name))
    env = make_dm2gym_env_obs(env_name=env_name, num_repeat_action=1)
    env = Monitor(env=env, directory="./video/{}".format(env_name), force=True)

    obs = env.reset()
    print("Obs shape: ", obs.shape)

    total_reward = 0

    env.record_start()
    env.reset()
    for t in itertools.count():
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward

        if done: break

    env.record_end()
    env.close()
    print("Total Reward: {}".format(total_reward))
