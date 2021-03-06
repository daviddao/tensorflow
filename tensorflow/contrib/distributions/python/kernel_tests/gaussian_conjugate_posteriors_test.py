# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for initializers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

import tensorflow as tf

gaussian_conjugate_posteriors = tf.contrib.distributions.gaussian_conjugate_posteriors  # pylint: disable=line-too-long


class GaussianTest(tf.test.TestCase):

  def testGaussianConjugateKnownSigmaPosterior(self):
    with tf.Session():
      mu0 = tf.constant(3.0)
      sigma0 = tf.constant(math.sqrt(1/0.1))
      sigma = tf.constant(math.sqrt(1/0.5))
      x = tf.constant([-2.5, 2.5, 4.0, 0.0, -1.0, 2.0])
      s = tf.reduce_sum(x)
      n = tf.size(x)
      prior = tf.contrib.distributions.Gaussian(mu=mu0, sigma=sigma0)
      posterior = gaussian_conjugate_posteriors.known_sigma_posterior(
          prior=prior, sigma=sigma, s=s, n=n)

      # Smoke test
      self.assertTrue(isinstance(posterior, tf.contrib.distributions.Gaussian))
      posterior_log_pdf = posterior.log_pdf(x).eval()
      self.assertEqual(posterior_log_pdf.shape, (6,))

  def testGaussianConjugateKnownSigmaPredictive(self):
    with tf.Session():
      mu0 = tf.constant(3.0)
      sigma0 = tf.constant(math.sqrt(1/0.1))
      sigma = tf.constant(math.sqrt(1/0.5))
      x = tf.constant([-2.5, 2.5, 4.0, 0.0, -1.0, 2.0])
      s = tf.reduce_sum(x)
      n = tf.size(x)
      prior = tf.contrib.distributions.Gaussian(mu=mu0, sigma=sigma0)
      predictive = gaussian_conjugate_posteriors.known_sigma_predictive(
          prior=prior, sigma=sigma, s=s, n=n)

      # Smoke test
      self.assertTrue(isinstance(predictive, tf.contrib.distributions.Gaussian))
      predictive_log_pdf = predictive.log_pdf(x).eval()
      self.assertEqual(predictive_log_pdf.shape, (6,))

if __name__ == '__main__':
  tf.test.main()
