__author__ = 'kratra'

import nltk
import nltk.util

def main():
    print "Inside main..."

    pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('I am so happy','positive'),
              ('He is my best friend', 'positive')]


    neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking x to the concert', 'negative'),
              ('I am sad','negative'),
              ('He is my enemy', 'negative')]

    tweets = []
    for (words, sentiment) in pos_tweets + neg_tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered, sentiment))
    global word_features
    word_features = get_word_features(get_words_in_tweets(tweets))
    document = "love this car"
    features = extract_features(document)
    training_set = nltk.classify.apply_features(extract_features, tweets)
    print "Training set done.."
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    tweet = 'He is happy today'
    print classifier.classify(extract_features(tweet.split()))


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


if __name__ == '__main__':
    main()