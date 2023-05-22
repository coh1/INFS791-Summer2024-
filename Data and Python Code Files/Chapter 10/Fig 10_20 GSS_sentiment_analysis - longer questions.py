import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt

gss_questions_df = pd.read_csv("GSS_all_questions.txt", sep='|')
just_questions = gss_questions_df["question_text"]

sia = SentimentIntensityAnalyzer()

positive_scores = []
negative_scores = []
neutral_scores = []
compound_scores = []

question_count = 0
long_questions = 0

for question in just_questions:
    question_count = question_count + 1
    question_length = len(question)

    if question_length > 150:
        long_questions = long_questions + 1
        score = sia.polarity_scores(question)
        compound_scores.append(score['compound'])
        negative_scores.append(score['neg'])
        neutral_scores.append(score['neu'])
        positive_scores.append(score['pos'])

print("Total number of questions: ", question_count)
print("total questions processed:", long_questions)
print("Average of neutral scores: ", np.mean(neutral_scores))
print("Average of positive scores: ", np.mean(positive_scores))
print("Average of negative scores: ", np.mean(negative_scores))
print("Average of compound scores: ", np.mean(compound_scores))

plt.plot(neutral_scores, label="Neutral")
plt.plot(negative_scores, label="Negative")
plt.plot(positive_scores, label="Positive")
plt.title("Scores by Question #")
plt.legend()
plt.show()

