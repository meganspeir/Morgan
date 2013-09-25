Morgan
=======

It's like "Klout" for events!

Twitter sentiment analysis using a Naïve Bayes classifier.

This project currently implements a small subset of data. However, the algorithm could easily be seeded with your own training data.

The screenshot below shows the data representation as would be rendered with some help using D3 for data visualization.

Each chart represents a group of Tweets from a specific Twitter hashtag that have been assigned a score based upon positive or negative sentiment. 100 being most positive and 0 being the worst.

The words [or features] that occur the most are shown in sentiments. See `tweetclass.py` to see the training!

```python
    def feature_count(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
```

And an additional feature will include keeping track of the people who are talking about your event the most on Twitter.

![alt tag](https://raw.github.com/meganspeir/Morgan/master/screenshot.png)
