
from textblob import TextBlob
import nltk


review ="i am a good food"

decision = TextBlob(review)

# Polarity is a float value within the range
# [-1.0 to 1.0] where 0 indicates neutral, +1 indicates a very positive sentiment
# and -1 represents a very negative sentiment.

# Subjectivity is a float value within the range [0.0 to 1.0] where 0.0 is very objective and
# 1.0 is very subjective. Subjective sentence expresses some personal
# feelings, views, beliefs, opinions, allegations, desires, beliefs, suspicions, and speculations where
# as Objective sentences are factual

print(format(decision.sentiment))

c = format(decision.sentiment.polarity)
print(c)
if float(c) < 0.1:
    print("bad review")
else:
    print("good review")
