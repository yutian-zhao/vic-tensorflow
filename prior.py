import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()


class FixedUniformDiscretePrior:
    def __init__(self, n_options, sess):
        self.n_options = n_options
        self.sess = sess
        self.picker = tf.multinomial([self.n_options * [1.0]], 1)[0][0]

    def p_omega(self, omega):
        return 1.0 / self.n_options

    def all_p_omegas(self):
        return [1.0 / self.n_options] * self.n_options

    def sample_omega(self):
        """Returns an id of an option as a tensor of shape [1, 1]."""
        return self.sess.run(self.picker), 1.0 / self.n_options


# TODO: other priors
