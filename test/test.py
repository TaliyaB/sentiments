"""
Tester Code
"""
from sentiments import TextProcessor, Visualizer, MachineLearning
import os

path = os.path.join(os.getcwd(), "sample_data/Student' s Perception towards Online Learning Questionnaire.csv")

#create data object
data = TextProcessor.TextProcessor()
data.parser(path=path)
print('Total respondents per course: {}'.format(data.dict_respondents_course))
print('Total number of respondents: {}'.format(data.int_respondents_count))
#print('Tokens per question {}'.format(data.list_tokens_per_question))
print('Number of responses for sentiment analysis: {}\nCorresponding tokens {}'.format(len(data.list_texts), len(data.list_tokens_per_text)))
print('Dataframe for sentiment analysis {}'.format(data.df_final_data_for_sentiment_analysis))

machine_learning_processes = MachineLearning.MachineLearning(df_for_sentiment_analysis=data.df_final_data_for_sentiment_analysis,
                                                             tokens_per_question=data.list_tokens_per_question,
                                                             respondents_by_course=data.dict_respondents_course,
                                                             respondents_by_block=data.dict_respondents_block,
                                                             total_respondents=data.int_respondents_count)
machine_learning_processes.exploratory_data_analysis(n_words=5)
machine_learning_processes.sentiment_analysis()
#print('Sentiment Analysis\n{}'.format(machine_learning_processes.df_sentiment_analysis_result))
#print('Positive Texts\n{}'.format(machine_learning_processes.df_positive_predicted_sentiments))
machine_learning_processes.LatentDirichletAllocation(
    tokens= machine_learning_processes.df_negative_predicted_sentiments['Tokens'].tolist(),
    filename_lda_model= 'all_generated\\negative.gensim',
    filename_corpus= 'all_generated\\negative_corpus.pkl',
    filename_dictionary= 'all_generated\\negative_dictionary.gensim'
)
machine_learning_processes.LatentDirichletAllocation(
    tokens=machine_learning_processes.df_positive_predicted_sentiments['Tokens'].tolist(),
    filename_lda_model= 'all_generated\\positive.gensim',
    filename_corpus= 'all_generated\\positive_corpus.pkl',
    filename_dictionary= 'all_generated\\positive_dictionary.gensim'
)
positive_wordCloud = Visualizer.Visualizer()
positive_wordCloud.wordCloud(text=machine_learning_processes.df_positive_predicted_sentiments['Text'].tolist(),
                             color='white', title='Positive WordCloud', output_file='all_generated\\positive_wordcloud.png')
negative_wordCloud = Visualizer.Visualizer()
negative_wordCloud.wordCloud(text=machine_learning_processes.df_negative_predicted_sentiments['Text'].tolist(),
                             color='black', title='Negative WordCloud', output_file='all_generated\\negative_wordcloud.png')