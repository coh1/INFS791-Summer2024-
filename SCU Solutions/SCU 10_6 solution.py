import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

gss_questions_df = pd.read_csv("GSS_all_questions.txt", sep='|')
just_questions = gss_questions_df["question_text"]

sia = SentimentIntensityAnalyzer()

num_pos = 0
num_neg = 0
num_neut = 0
num_none = 0

for question in just_questions:
    # Add line of code below to determine sentiment values
    score = sia.polarity_scores(question)

    # The following code tallies questions by sentiment
    #  considered pos, neg or neutral if value > 0.5
    if score['pos'] > 0.5:
        num_pos += 1
    elif score['neg'] > 0.5:
        num_neg += 1
    elif score['neu'] > 0.5:
        num_neut += 1
    else:
        num_none += 1

print("Total number of positive questions: ", num_pos)
print("Total number of negative questions: ", num_neg)
print("Total number of neutral questions: ", num_neut)
print("Questions in none of the categories: ", num_none)

