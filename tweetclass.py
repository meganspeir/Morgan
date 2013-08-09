import re
import math

""" Some sample training data to feed the classifier.
"""

def sample_train(cl):
    cl.train('Nobody owns the water.', 'positive')
    cl.train('The quick rabbit jumps fences', 'positive')
    cl.train('Buy pharmaceuticals now', 'negative')
    cl.train('Make quick money at the online casino', 'negative')
    cl.train('The quick brown fox jumps', 'positive')

def get_words(tweet):
    splitter=re.compile('\\W*') # Lookup
    # Split the words by non-alpha characters
    words = [s.lower() for s in splitter.split(tweet)
                if len(s)>2 and len(s)<20]

    # Return the unique set of words only
    return dict([(w,1) for w in words])

class Classifier:
    def __init__(self, get_features, filname=None):
        # Counts of feature/category combinations
        self.fc = {}
        # Counts of tweets in each category
        self.cc = {}
        self.get_features = get_features # we will use get_words

    """ The methods in the class won't use the dictionaries directly because
    this restricts potential options for storing the training data in a file or database.
    The helper methods below will increment and get counts.
    """

    # Increment the count of a feature/category pair
    def increase_features(self, f, cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat]+=1

    # Increase the count of a category
    def increase_category(self, cat):
        self.cc.setdefault(cat,0)
        self.cc[cat]+=1

    # The number of times a feature has appeared in a category
    def feature_count(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    # The number of items in a category
    def category_count(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    # The total number of items
    def total_count(self):
        return sum(self.cc.values())

    # The list of all categories
    def categories(self):
        return self.cc.keys()

    """ The train method takes an item (a tweet in this case) and a
    classification. It uses the get_words function of the class to break the item
    into its separate features. Then calls increase_features to increase the counts for
    this classification for every feature. Finally, it increases the total count
    for this classification:
    """

    def train(self, item, cat):
        features = self.get_features(item)
        # Increment the count for every feature with this category
        for f in features:
            self.increase_features(f, cat)

        # Increment the count for this category
        self.increase_category(cat)

    """ Calculate condititonal probability. The probability of A givin B.
    Uses only the information it has seen so far which makes it incredibly
    sensitive during early training and to words that appear very rarely.
    """

    def feature_prob(self, f, cat):
        if self.category_count(cat) == 0: return 0
        # The total number of times this feature appeared in this
        # category divided by the total number of items in this category
        # print self.feature_count(f, cat)
        # print self.category_count(cat)
        return self.feature_count(f, cat)/self.category_count(cat)

    """ It would be much more realistic for the value to approach zero as a word
    ia found in more and more tweets with the same category. Thus, we create assumed
    probability, to be used when you have very little information about the feature in question.
    """

    def weighted_prob(self, f, cat, prf, weight=1.0, ap=0.5):
        # Calculate current probability
        basic_prob = prf(f, cat)

        # Count the number of times this feature/word has appeared in all categories
        totals = sum([self.feature_count(f, c) for c in self.categories()])

        # Calculate the weighted average
        bp = ((weight*ap)+(totals*basic_prob))/(weight+totals)
        return bp

    """ The classify method will calculate the probability for each category, and determine
    which one is the largest and whether it exceeds the next largest by more than its
    threshold. If none of the categories can accomplish this, the method returns the default
    values.
    """

    def classify(self, item, default=None):
        probs = {}
        # Find the category with the highest probability.
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.probability(item, cat)
            if probs[cat]>max:
                max = probs[cat]
                best_match = cat
        # Make sure the probability exceeds threshold*next best match
        for cat in probs:
            if cat == best_match: continue
            if probs[cat]*self.get_threshold(best_match)>probs[best_match]: return default
        return best_match

    """ A naive Bayesian classifier assumes that the probabilities being combined are
    independent of each other. Determine the probability of an entire tweet being given a
    classification. Calculate the entire tweet probability by multiplying together all the
    probabilities of the individual words in the tweet.
    """

# This is a subclass of our main class Classifier
class Bayes(Classifier):

    def __init__(self,get_features):
        Classifier.__init__(self, get_features)
        self.thresholds={}

    def set_threshold(self,cat,t):
        self.thresholds[cat]=t

    def get_threshold(self,cat):
        if cat not in self.thresholds: return 1.0
        return self.thresholds[cat]

    def tweet_prob(self, item, cat):
        features = self.get_features(item)

        # Multiply the probabilities of all the features together
        p = 1
        for f in features:
            p*=self.weighted_prob(f, cat, self.feature_prob)
        return p

    def probability(self, item, cat):
        category_prob = self.category_count(cat)/self.total_count()
        tweet_prob = self.tweet_prob(item, cat)
        return tweet_prob*category_prob

    """ Now let's decide in which category a new item belongs. To minimize the margin of
    error, we will set up a minimum threshold for each category. For a new item to be
    classified into a particular ctageory, its probability must be a specified amount larger
    then the probability of another category. See the __init__ added to Bayes.
    """










