"""
Tester Code
"""
from sentiments import TextProcessor, Visualizer, MachineLearning
import os

p= os.path.join(os.getcwd(), "sample_data\\Student' s Perception towards Online Learning Questionnaire.csv")
#create data object
data = TextProcessor.TextProcessor()
data.parser(path=p)
print(data.dict_respondents_block.keys())
