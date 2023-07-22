# This script trains the LLM
import xgboost as xgb
from collections import defaultdict as dd
from collections import Counter

lookup = dd(Counter)

def simple_inverter(_val):
    # takes an int and returns the most likely word (string)
    return lookup[_val].most_common()


def simple_hash_encoder(word):
    N = 10000
    # takes a string and returns an int
    val = abs(hash(word)) % N
    lookup[val][word] += 1
    return val

if __name__ == "__main__":
   # get the data
   records = [] 
   with open('shakespeare.txt') as f:
       for line in f:
           line = line.split(' ')
           for word in line:
               records.append(simple_hash_encoder(word)) 

   # now we have all the text as a long string of integers

   # the problem is to predict the N+1th word, given the preceding N words

   # for xgboost, we make a call to model.fit(X_train, y_train)
   # X_train is rows with the preceding N words.
   # y_train is rows of the N+1th word.

   # encode training data
   # train model
   model = xgb.sklearn.XGBClassifier()
   model.fit(X_train, y_train)
   # evaluate performance
   model.predict(y_test)

   #   we'll need to invert the hashing encoder to print out the predicted next words


 
