"""
DATA EXTRACTOR CODE
"""
from sentiments import TextProcessor, Visualizer, MachineLearning
import os
path =  "C:\\Users\\user\\Documents\\Freelance\\sentiments\\sample_data\\Student' s Perception towards Online Learning Questionnaire.csv (1)\\Student' s Perception towards Online Learning Questionnaire.csv"
path = os.path.join(os.getcwd(), path)

#create data object
data = TextProcessor.TextProcessor()
data.parser(path=path)

print(data.df_final_data_for_sentiment_analysis)
machine_learning_processes = MachineLearning.MachineLearning(df_for_sentiment_analysis=data.df_final_data_for_sentiment_analysis,
                                                             tokens_per_question=data.list_tokens_per_question,
                                                             respondents_by_course=data.dict_respondents_course,
                                                             respondents_by_block=data.dict_respondents_block,
                                                             total_respondents=data.int_respondents_count)
machine_learning_processes.exploratory_data_analysis(n_words=5)
machine_learning_processes.sentiment_analysis()

respondents_per_block = Visualizer.Visualizer()
print(data.dict_respondents_block)
respondents_per_block.pie(x_data=data.dict_respondents_block.keys(),
                          y_data=data.dict_respondents_block.values(),
                          title="Distribution of Respondents per Course",
                          output_filename="all_generated/respondents_per_block.png")
respondents_per_course = Visualizer.Visualizer()
print(data.dict_respondents_course)
respondents_per_course.pie(x_data=data.dict_respondents_course.keys(),
                           y_data=data.dict_respondents_course.values(),
                           title="Distribution of Respondents per Course",
                           output_filename="all_generated/respondents_per_course.png")

#adj
top_n_adj = Visualizer.Visualizer()
print(machine_learning_processes.df_top_n_adjectives)
top_n_adj.multiple_bar_for_top_n_words(df_top_n_words=machine_learning_processes.df_top_n_adjectives,
                                       word_type='Adjective',
                                       title="Top Adjectives per Question",
                                       output_file="visuals/templates/top_n_Adjective.png")

#noun
top_n_noun = Visualizer.Visualizer()
top_n_noun.multiple_bar_for_top_n_words(df_top_n_words=machine_learning_processes.df_top_n_nouns,
                                         word_type='Noun',
                                         title="Top Nouns per Question",
                                         output_file="visuals/templates/static/top_n_Noun.png")

#block
respondents_per_block = Visualizer.Visualizer()
respondents_per_block.pie(x_data=data.dict_respondents_block.keys(),
                          y_data=data.dict_respondents_block.values(),
                          title="Distribution of Respondents per Course",
                          output_filename="visuals/templates/static/respondents_per_block.png")

#course
respondents_per_course = Visualizer.Visualizer()
respondents_per_course.pie(x_data=data.dict_respondents_course.keys(),
                          y_data=data.dict_respondents_course.values(),
                          title="Distribution of Respondents per Course",
                          output_filename="visuals/templates/static/respondents_per_course.png")
