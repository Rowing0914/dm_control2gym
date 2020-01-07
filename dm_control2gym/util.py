import gym
import dm_control2gym
from dm_control2gym.base_wrappers import wrap_deepmind

DM_TASKS = {
    "cartpole_balance": ('cartpole', 'balance'),
    "cartpole_swingup": ('cartpole', 'swingup'),
    "cheetah_run": ("cheetah", "run"),
    "reacher_easy": ("reacher", "easy"),
    "cup_catch": ("ball_in_cup", "catch"),
    "walker_walk": ("walker", "walk"),
    "finger_spin": ("finger", "spin"),
}


class PixelObservationWrapper(gym.ObservationWrapper):
    """ check this post: https://github.com/openai/gym/pull/740#issuecomment-470382987 """

    def __init__(self, env, img_shape=None):
        gym.ObservationWrapper.__init__(self, env)
        self.img_shape = img_shape

    def observation(self, observation):
        img = self.env.render(mode='rgb_array')
        return img if self.img_shape is None else img.image_resize(self.img_shape)


def make_dm2gym_env_obs(env_name="cheetah_run", num_repeat_action=1):
    """ Invoke POMDP tasks """
    env_name_tuple = DM_TASKS[env_name.lower()]
    domain_name, task_name = env_name_tuple[0], env_name_tuple[1]
    env = dm_control2gym.make(domain_name=domain_name, task_name=task_name)
    env = PixelObservationWrapper(env=env)
    env = wrap_deepmind(env=env, num_repeat_action=num_repeat_action)
    return env


def make_dm2gym_env_state(env_name="cheetah_run"):
    """ Invoke MDP tasks """
    env_name_tuple = DM_TASKS[env_name.lower()]
    domain_name, task_name = env_name_tuple[0], env_name_tuple[1]
    env = dm_control2gym.make(domain_name=domain_name, task_name=task_name)
    return env
