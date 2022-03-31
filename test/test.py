"""
Tester Code
"""
from sentsys.visuals import TextProcessor
import os

p= os.path.join(os.getcwd(), "sample_data\\Student' s Perception towards Online Learning Questionnaire.csv")
#create data object
data = TextProcessor.TextProcessor()
data.parser(path=p)
print(data.dict_respondents_block.keys())
