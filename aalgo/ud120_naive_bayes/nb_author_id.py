#!/usr/bin/python

"""
This is the code to accompany the Lesson 1 (Naive Bayes) mini-project of Udacity 120 Introduction to Artificial Intelligence.

Use a Naive Bayes Classifier to identify emails by their authors.

Sara has label 0, Chris has label 1.
"""

import numpy
import sys


class SolutionClass(object):

    """A SolutionClass is one of the categories that a classifier can solve to."""

    def __init__(self, training_features):
        """Create a new SolutionClass with its training data."""
        self.features = training_features
        self.num_features = len(training_features[0])
        self.num_training_data = len(training_features)
        # TODO: Enforce the below access instructions using getters.
        self.variances = numpy.full(self.num_features, -1.0, dtype='Float64')  # Never access this directly.  Use the self.variance() method.
        self.mles = numpy.full(self.num_features, -1.0, dtype='Float64')       # Never access this directly.  Use the self.mle() method.
        self.sums = numpy.full(self.num_features, -1.0, dtype='Float64')       # Never access this directly.  Use the self.feature_sum() method.

    def feature_sum(self, feature_index):
        """Return the sum across all training features of the given feature for the given class."""
        stored_value = self.sums[feature_index]
        if stored_value != -1:
            return stored_value

        total = 0.0
        for features in self.features:
            total += features[feature_index]
        self.sums[feature_index] = total
        return total

    def mle(self, feature_index):
        # Equation from http://cs.nyu.edu/~dsontag/courses/ml12/slides/lecture17.pdf and http://www.cs.cmu.edu/~epxing/Class/10701-10s/Lecture/lecture5.pdf
        """Estimate the maximum likelihood using mean."""
        stored_value = self.mles[feature_index]
        if stored_value != -1:
            return stored_value

        features_sum = self.feature_sum(feature_index)
        # The smoothing factor is Laplace smoothing as described in http://cs229.stanford.edu/notes/cs229-notes2.pdf
        smoothing_factor = numpy.float64(1.0)
        estimate = self.mles[feature_index] = (features_sum + smoothing_factor) / (self.num_training_data + self.num_features * smoothing_factor)
        return estimate

    def variance(self, feature_index):
        # Equation from http://cs.nyu.edu/~dsontag/courses/ml12/slides/lecture17.pdf and http://www.cs.cmu.edu/~epxing/Class/10701-10s/Lecture/lecture5.pdf
        """Variance."""
        stored_value = self.variances[feature_index]
        if stored_value != -1:
            return stored_value

        mle = self.mle(feature_index)
        weighted_sum = 0
        for features in self.features:
            weighted_sum += (features[feature_index] - mle) ** 2
        variance = self.variances[feature_index] = weighted_sum / (self.num_training_data - 1)
        return variance

    def feature_log_probability(self, feature_value, feature_index):
        """Predict the probability that this feature belongs to this class."""
        mle = self.mle(feature_index)
        var = self.variance(feature_index)
        # Equation from http://scikit-learn.org/stable/modules/naive_bayes.html
        return (-(feature_value - mle) ** 2 / (2 * var)) - numpy.log(numpy.sqrt(2 * numpy.pi * var))


def classify(solution_classes, features):
    """Given a list of features, decide which of the given solution_classes it fits into. Returns a SolutionClass object or -1 if none of the given features match any of the given solution classes."""
    winner_probability = -sys.maxsize
    winner = -1

    for solution_class in solution_classes:
        probability = numpy.float64(0.0)
        feature_index = 0
        for feature in features:
            if feature:     # If the feature isn't present in the test features, then omit it from the classification
                feature_probability = solution_class.feature_log_probability(feature, feature_index)
                if feature_probability:    # A feature probability of 0 means that this feature never appears in this class' training data.  However, this does not necessarily mean it's impossible that this test data belongs to this class.
                    probability += feature_probability
            feature_index += 1
        if probability > winner_probability:
            winner = solution_class
            winner_probability = probability
    return winner
