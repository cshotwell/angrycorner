import csv
import nltk
import random

def load_dataset(filename, sentiment):
    with open(filename, "rb") as csvfile:
        reader = csv.reader(csvfile)
        features = []
        for row in reader:
            features.append((dict([(word, True) for word in row[5].split(' ')]), sentiment))
        return features


def get_trained_classifier(training_set):
    return nltk.NaiveBayesClassifier.train(training_set)

positive_train = "data/1000_happy.csv"
negative_train = "data/1000_angry.csv"
test_data = "data/testdata.csv"

happy_set = load_dataset(positive_train, "happy")
angry_set = load_dataset(negative_train, "angry")
random.shuffle(happy_set)
random.shuffle(angry_set)

# 80-20 testing
test_cutoff = int(len(happy_set)*.8)

training_set = happy_set[test_cutoff:] + angry_set[test_cutoff:]
testing_set = happy_set[:test_cutoff] + angry_set[:test_cutoff]

classifier = get_trained_classifier(training_set)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testing_set)
classifier.show_most_informative_features()