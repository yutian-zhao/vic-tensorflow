from __future__ import print_function

from experiments.grid_world_exp import GridWorldExperiment
import time

n_trajectories = 3
if __name__ == "__main__":
    runner = GridWorldExperiment()
    runner.train(n_episodes=1000)  # TODO: pickle/load the results of experiment
    
    x = input("Enter to proceed")
    for omega in range(runner.n_options):
        print("\noption", omega, "\n=============")
        for traj in range(n_trajectories):
            print("epsilon", runner.policy.epsilon)
            runner.rollout(omega, render=False)
            print("trajectory", traj, "final state", runner.env.state)
            # TODO: matrix map

# option 0 
# =============
# epsilon 0.001
# trajectory 0 final state [2, 5]

# option 1 
# =============
# epsilon 0.001
# trajectory 0 final state [4, 4]

# option 2 
# =============
# epsilon 0.001
# trajectory 0 final state [2, 5]

# option 3 
# =============
# epsilon 0.001
# trajectory 0 final state [2, 4]

# option 4 
# =============
# epsilon 0.001
# trajectory 0 final state [1, 4]

# option 5 
# =============
# epsilon 0.001
# trajectory 0 final state [0, 3]

# option 6 
# =============
# epsilon 0.001
# trajectory 0 final state [1, 2]

# option 7 
# =============
# epsilon 0.001
# trajectory 0 final state [0, 4]

# option 8 
# =============
# epsilon 0.001
# trajectory 0 final state [2, 4]

# option 9 
# =============
# epsilon 0.001
# trajectory 0 final state [4, 4]

# [0., 0., 0., 6., 8., 0., 0., 0., 0.],
# [0., 0., 7., 0., 5., 0., 0., 0., 0.],
# [0., 0., 0., 0., 4., 3., 0., 0., 0.],
# [0., 0., 0., 0., 0., 0., 0., 0., 0.],
# [0., 0., 0., 0., 2., 0., 0., 0., 0.]