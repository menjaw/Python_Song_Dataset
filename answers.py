import webget as wg
#from builtins import print
import pandas as pd
import collections
import matplotlib.pyplot as plt



url = 'https://raw.githubusercontent.com/KasperOnFire/ImpossibleTechnology/master/Datasets/songdata.csv'

#wg.download(url)


df = pd.read_csv('.\songdata.csv')


def question1():
    """QUESTION 1:What is the most used words in the songs?"""
    most_used_word = df['text'].str.split(expand=True).stack().value_counts() #expand returnerer et nyt dataframe (her kun med colunm text fra csv)
    print("The most used word in the songs are: \n{}".format(most_used_word[0:1]))


def question2():
    """QUESTION 2: How many times are each word repeated in a song? (Or perhaps - what song repeats the top 4 repeated words the most? - finds the most repetitive song)"""
    top_10_words = df['text'].str.split(expand=True).stack().value_counts()
    print("The top 10 most used words in the songs are: \n{}".format(top_10_words[0:11]))


def question3():
    """QUESTION 3: What song uses the word "X" the most time? (X meaning a specific word, choose your own!) columns=['Text']"""
    # Search less strict for all rows where column contains the specific word
    data = {'Lyrics': df['text'],
            'Title': df['song']}
    dataframe = pd.DataFrame(data)
    dataframe['Count'] = dataframe.Lyrics.str.count('fuck')
    contain_specific_word = dataframe[dataframe['Lyrics'].str.contains('fuck', case=False)]
    print(contain_specific_word[0:5].sort_values(by=['Count'], ascending=False))


def question4():
    """QUESTION 4: What is the average number of words per song?"""
    lines = df['text'].str.split().count() #antal af sange
    all_words = sum(df['text'].str.split(expand=True).stack().value_counts()) #antal af ord i sange
    print("All words: {}".format(all_words))
    print("All lines: {}".format(lines))
    print("Average numbers of words in songs: {} ".format(all_words / lines))



def question5():
    """QUESTION 5: Show the distribution of number of words in the songs. (Example: how many songs have 5-10 words, 10-20 words)"""
    song = df['text'].str.split()  # Tager hver sang og splitter alle ordene op med et komma
    list_of_counts = []
    for words in song:
        list_of_counts.append(len(words))
    print(list_of_counts)


    #Histogram
    y = list_of_counts

    plt.hist(y, histtype='bar', rwidth=0.8)
    plt.title('distribution of number of words')
    plt.xlabel('number of words')
    plt.ylabel('songs')

    plt.show()


#Run methods
question1()
question2()
question3()
question4()
question5()



