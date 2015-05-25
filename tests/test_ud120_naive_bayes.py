"""Test the arithmetic functions."""

from aalgo.ud120_naive_bayes.nb_author_id import SolutionClass, classify
from aalgo.ud120_naive_bayes.email_preprocess import preprocess
import os
import numpy
from tests.test_helpers import number_close_to


def test_mean():
    """Test that the mean method works."""
    solution_class1 = SolutionClass(numpy.array([[0.02, 0.001, 0.0], [1.0, 1.5, 3.0]]))
    solution_class2 = SolutionClass(numpy.array([[0.5, 0.7, 0.0], [0.0, 0.0, 0.0]]))

    assert solution_class1.feature_sum(0) == 1.02
    assert solution_class1.feature_sum(1) == 1.501
    assert solution_class1.feature_sum(2) == 3.0
    assert solution_class2.feature_sum(0) == 0.5
    assert solution_class2.feature_sum(1) == 0.7
    assert solution_class2.feature_sum(2) == 0.0
    assert solution_class1.mean(0) == 0.51
    assert solution_class1.mean(1) == 1.501 / 2
    assert solution_class1.mean(2) == 3.0 / 2
    assert solution_class2.mean(0) == 0.5 / 2
    assert solution_class2.mean(1) == 0.7 / 2
    assert solution_class2.mean(2) == 0.0 / 2
    number_close_to(solution_class1.variance(0), 0.4802, 0.0001)
    number_close_to(solution_class1.variance(1), 1.1235, 0.0001)
    number_close_to(solution_class1.variance(2), 4.5, 0.0001)
    number_close_to(solution_class2.variance(0), 0.125, 0.0001)
    number_close_to(solution_class2.variance(1), 0.245, 0.0001)
    number_close_to(solution_class2.variance(2), 0.0, 0.0001)
    assert solution_class1 == classify([solution_class1, solution_class2], [1.0, 1.5, 3.0])
    assert solution_class2 == classify([solution_class1, solution_class2], [0.5, 0.7, 0.0])
    assert solution_class2 == classify([solution_class1, solution_class2], [0.02, 0.7, 0.0])
    assert solution_class2 == classify([solution_class1, solution_class2], [0.02, 0.02, 0.0])
    assert solution_class1 == classify([solution_class1, solution_class2], [1.0, 1.0, 1000.0])
    assert solution_class2 == classify([solution_class2, solution_class2], [0.0, 0.0, 0.0])


def test_naive_bayes():
    """Test the accuracy of the Naive Bayes algorithm at identifying who wrote a piece of text."""
    # Item labels and features separated into the training and testing sets
    data_dir = os.path.join(os.path.dirname(__file__), "data/")
    words_file = os.path.join(data_dir, "word_data.pkl")
    authors_file = os.path.join(data_dir, "email_authors.pkl")
    training_features, testing_features, training_labels, testing_labels = preprocess(words_file, authors_file)

    numpy.set_printoptions(threshold=numpy.nan)

    # Sara SolutionClass
    sara_positions = numpy.where(training_labels == 0)[0]
    sara_features = training_features[sara_positions]
    sara_solution_class = SolutionClass(sara_features)

    # Chris SolutionClass
    chris_positions = numpy.where(training_labels == 1)[0]
    chris_features = training_features[chris_positions]
    chris_solution_class = SolutionClass(chris_features)

    key = {sara_solution_class: 0, chris_solution_class: 1}

    i = 0
    right = 0
    total = len(testing_features)
    for features in testing_features:
        print('Testing email {}/{}'.format(str(i), str(total)))
        decision = classify([sara_solution_class, chris_solution_class], features)
        if decision == -1:
            print('Got -1 for the winner')
        if decision != -1 and key[decision] == testing_labels[i]:
            print('Got {}/{} right'.format(str(right), str(i)))
            right += 1
        i += 1
    print('Got {}% right'.format(str(right / total * 100)))
    assert right / total * 100 > 67
