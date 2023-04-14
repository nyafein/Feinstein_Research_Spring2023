# Nya Feinstein
# Using this website: https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6

# Website for code: https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-download-auto-examples-core-run-core-concepts-py

# Imports
import pandas as pd
import re
import gensim
import pprint
from gensim import models
from gensim import similarities
import matplotlib.pyplot as plt


# First, extract data from CSV into a dataframe to be used
df = pd.read_csv("C:/Users/nsf00/PycharmProjects/Research_Spring_2023/mid6/saved/UNA_data_1.csv")
# Clean data:
# Remove everything between the delimiters and take out punctuation

# Iterate through each element
# The outer loop is for the columns (we have three)
for i in range(0,3):
    # Go through the rows
    for j in range(0, len(df.iloc[:])):
        df.iloc[j,i] = re.sub('<[^>]+>', '', df.iloc[j,i])

# Save the data without labels - Only do this once, so I commented it out
# df.to_csv('UNA_data_2.csv',index=False)

# For this, let's use the data we just edited. Just in case, I created a copy and will use that.
df2 = pd.read_csv("C:/Users/nsf00/PycharmProjects/Research_Spring_2023/mid6/saved/UNA_data_2_test.csv")

# That dataframe will be our corpus.

##################################################################################
# THE FOLLOWING CHUNK OF CODE IS BASED ON THE FILE run_core_concepts from the website:
# https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-download-auto-examples-core-run-core-concepts-py

# Next, we want to remove "little" words, such as "the", "a", etc
# Create a set of frequent words
stoplist = set('for a of the and to in'.split(' '))
# Now, let's create a list of frequent words
# We're going to look at the third column of the dataframe. That is our body.
texts = []
for i in range(0,len(df2)):
    # Lowercase each document, split it by white space and filter out stopwords
    text_bite = [word for word in df2.iloc[i,2].lower().split() if word not in stoplist]
# Get rid of any numbers!
    for j in text_bite:
        if j.isnumeric():
            text_bite.remove(j)

    texts.append(text_bite)

print(texts)

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    print(text)
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
pprint.pprint(processed_corpus)

# Next, associate each word with a unique integer ID

from gensim import corpora
dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)
print(len(dictionary))
# 42400 unique tokens

# View everything in the dictionary
pprint.pprint(dictionary.token2id)

# Convert corpus to a list of vectors with bag of words
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
pprint.pprint(bow_corpus)

# Now use a model: The tf-idf model
# transforms vectors from the bag-of-words representation to a vector space
# where the frequency counts are weighted according to the relative rarity of
# each word in the corpus.


# train the model
tfidf2 = models.TfidfModel(bow_corpus)

# Try "War in Ukraine" or "Putin"
words1 = "War Ukraine".lower().split()
print(tfidf[dictionary.doc2bow(words1)])
words2 = "Russia Putin".lower().split()
print(tfidf[dictionary.doc2bow(words2)])

# First entry is token ID, second is tf-idf weighting

# Once you've created the model, you can do all sorts of cool stuff with it.
# For example, to transform the whole corpus via TfIdf and index it, in
# preparation for similarity queries:
#

# 42400 features
index = similarities.SparseMatrixSimilarity(tfidf2[bow_corpus], num_features=42400)
# and to query the similarity of our query document ``query_document`` against every document in the corpus:

# WAR
query_document = 'war'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_war = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_war.append(score)
war_df = pd.DataFrame({'documents': documents, 'scores_war': scores_war})

# INVASION
query_document = 'invasion'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_invasion = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_invasion.append(score)
invasion_df = pd.DataFrame({'documents': documents, 'scores_invasion': scores_invasion})

# AID
query_document = 'aid'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_aid = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_aid.append(score)
aid_df = pd.DataFrame({'documents': documents, 'scores_aid': scores_aid})

# PEACE
query_document = 'peace'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_peace = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_peace.append(score)
peace_df = pd.DataFrame({'documents': documents, 'scores_peace': scores_peace})

# NEGOTIATION
query_document = 'negotiation'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_negotiation = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_negotiation.append(score)
negotiation_df = pd.DataFrame({'documents': documents, 'scores_negotiation': scores_negotiation})

# CONFLICT
query_document = 'conflict'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_conflict = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_conflict.append(score)
conflict_df = pd.DataFrame({'documents': documents, 'scores_conflict': scores_conflict})

# MILITARY
query_document = 'military'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_military = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_military.append(score)
military_df = pd.DataFrame({'documents': documents, 'scores_military': scores_military})

# ATTACK
query_document = 'attack'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_attack = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_attack.append(score)
attack_df = pd.DataFrame({'documents': documents, 'scores_attack': scores_attack})

# MISSILE
query_document = 'missile'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_missile = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_missile.append(score)
missile_df = pd.DataFrame({'documents': documents, 'scores_missile': scores_missile})

# SANCTION
query_document = 'sanction'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_sanction = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_sanction.append(score)
sanction_df = pd.DataFrame({'documents': documents, 'scores_sanction': scores_sanction})

# CYBER
query_document = 'cyber'.lower().split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf2[query_bow]]
print(list(enumerate(sims)))
documents = []
scores_cyber = []
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)
    documents.append(document_number)
    scores_cyber.append(score)
cyber_df = pd.DataFrame({'documents': documents, 'scores_cyber': scores_cyber})

# Create a list of dates
date = []
for i in df2.iloc[:,1]:
    date.append(i)
documents.sort()
date_df = pd.DataFrame({'documents': documents, 'date': date})

#############################################################################
# THIS IS AN OLD WAY TO DO EVERYTHING!!!!!! It doesn't work.
# Create a preliminary dataframe with the document and its respective scores
d = {'documents': documents, 'similarity_war': scores_war,'similarity_invasion': scores_invasion,
     'similarity_aid': scores_aid, 'similarity_peace': scores_peace, 'similarity_negotiation': scores_negotiation,
     'similarity_conflict': scores_conflict, 'similarity_military': scores_military, 'similarity_attack': scores_attack,
     'similarity_missile': scores_missile, 'similarity_sanction': scores_sanction, 'similarity_cyber': scores_cyber}
results_df = pd.DataFrame(data=d)

# Sort the values by document because we know that each document in order relates to a date
# For some reason, the documents are not in order right now
results_df = results_df.sort_values(by=['documents'])

# Add the date in
results_df['date'] = date

# Save to a CSV
results_df.to_csv("C:/Users/nsf00/PycharmProjects/Research_Spring_2023/mid6/saved/similarity_results_3.csv")
#############################################################################

#############################################################################
# This is the better way to do everything!
# I made everything into a dataframe and am now going to do an inner join
df_1 = pd.merge(war_df, invasion_df, on='documents', how='inner')
df_2 = pd.merge(df_1, aid_df, on='documents', how='inner')
df_3 = pd.merge(df_2, peace_df, on='documents', how='inner')
df_4 = pd.merge(df_3, negotiation_df, on='documents', how='inner')
df_5 = pd.merge(df_4, conflict_df, on='documents', how='inner')
df_6 = pd.merge(df_5, military_df, on='documents', how='inner')
df_7 = pd.merge(df_6, attack_df, on='documents', how='inner')
df_8 = pd.merge(df_7, missile_df, on='documents', how='inner')
df_9 = pd.merge(df_8, sanction_df, on='documents', how='inner')
df_10 = pd.merge(df_9, cyber_df, on='documents', how='inner')
df_total = pd.merge(df_10, date_df, on='documents', how='inner')

df_final = df_total.sort_values(by=['documents'])

# Use the below CSV for future analysis

df_final.to_csv("C:/Users/nsf00/PycharmProjects/Research_Spring_2023/mid6/saved/similarity_results_4.csv")













