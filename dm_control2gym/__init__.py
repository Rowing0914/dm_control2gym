from gym.envs.registration import register
import gym
import hashlib


def make(domain_name, task_name, task_kwargs=None, visualize_reward=False):
    # register environment
    prehash_id = domain_name + task_name + str(task_kwargs) + str(visualize_reward)
    h = hashlib.md5(prehash_id.encode())
    gym_id = h.hexdigest() + '-v0'

    # avoid re-registering
    if gym_id not in gym_id_list:
        register(
            id=gym_id,
            entry_point='dm_control2gym.wrapper:DmControlWrapper',
            kwargs={'domain_name': domain_name, 'task_name': task_name, 'task_kwargs': task_kwargs,
                    'visualize_reward': visualize_reward, 'render_mode_list': render_mode_list}
        )
    # add to gym id list
    gym_id_list.append(gym_id)

    # make the Open AI env
    return gym.make(gym_id)


def create_render_mode(name, show=True, return_pixel=False, height=240, width=320, camera_id=0, overlays=(),
                       depth=False, scene_option=None):
    render_kwargs = {'height': height, 'width': width, 'camera_id': camera_id,
                     'overlays': overlays, 'depth': depth, 'scene_option': scene_option}
    render_mode_list[name] = {'show': show, 'return_pixel': return_pixel, 'render_kwargs': render_kwargs}


gym_id_list = []
render_mode_list = {}
create_render_mode('human', show=True, return_pixel=False)
create_render_mode('rgb_array', show=False, return_pixel=True)
create_render_mode('human_rgb_array', show=True, return_pixel=True)
