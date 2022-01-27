import pandas as pd
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import spacy
spacy.cli.download("en_core_web_md")
import en_core_web_md


class TextProcessor():
    def __init__(self, path):
        self.path = path
        self.df_parsed_data = []
        self.list_lemmatized = None
        self.list_removed_stopwords = None
        self.list_cleaned = None

    def parser(self):
        # get dataframe for each question and append to list
        data = pd.read_csv(self.path)
        for i in range(1,len(data.columns)):
            self.df_parsed_data.append(data.iloc[i:,i])

    def lemmatization(self, list):
        return

    def remove_stopwords(self, list):
        return

    def clean_text(self, list):
        return

    def make_dataframe(self, list):
        cols = ['Text', 'Question Number']
        return

    def convert_to_csv(self):
        return

