
#imports
import sys
import pandas as pd
import re
from collections import defaultdict
import json
import sqlite3
import os
import shutil



# Set of predefined common words to be ignored. The list can be modified as required. For the purpose of this program, these stopwords are as provided by the NLTK library

stop_words={'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"}


file_name= sys.argv[1] # file_name to be processed, should be present in the "input" directory
source_path = 'input/'+file_name
input_df = pd.read_csv(source_path) # reading the CSV file into pandas dataframe


input_df["word_frequency"]='' # creating an empty column in the dataframe to hold word frequency
 

pattern = r"[-+]?\d*\.\d+|\d+|[^\w\s]" # regex to match unwanted characters - integers, floating values, punctuations and emojis
 

# this piece of code will loop over all the rows in the dataframe and get the word frequency
for ind in input_df.index:
    
    text=input_df['original_text'][ind]
    text = re.sub(pattern, '', text).strip() # removing unwanted characters as defined by earlier regex
    
    word_freq_dict = defaultdict(int) # dictionary to hold word frequency per row

    for word in text.casefold().split():
        
        if word not in stop_words and word != '': # condition to ignore the stopwords and empty strings
            word_freq_dict[word] += 1
            
    serialised = json.dumps(word_freq_dict) # converting ditionary to a JSON object to be further stored in Database
    input_df.loc[ind,'word_frequency']= serialised # Updating the word_frequency column in dataframe


input_df.to_csv('output.csv', index=False) # saving resultant dataframe as CSV

# Database - SQLite for disk-based database solution
conn = sqlite3.connect('Word_Frequency.db')

input_df.to_sql('Word_Frequency', conn, if_exists='replace', index=False) # converted the dataframe to SQLite DB table
cur = conn.cursor()


# # SQL query to retrieve data from the database 
# cur.execute("SELECT * FROM Word_Frequency") 

# result = cur.fetchall() # the method fetches all rows of a query result set and returns a list of tuples

# # displaying rows returned
# for row in result: 
#     print(row) 
#     print("\n")


os.mkdir('processed') # creating a new directory to move the processed file to


destination_path = 'processed/'+file_name
shutil.move(source_path, destination_path)


