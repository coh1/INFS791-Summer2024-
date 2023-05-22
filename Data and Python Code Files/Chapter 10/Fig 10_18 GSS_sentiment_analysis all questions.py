import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textwrap

gss_questions_df = pd.read_csv("GSS_all_questions.txt", sep='|')
just_questions = gss_questions_df["question_text"]

sia = SentimentIntensityAnalyzer()

question_count = 0

for question in just_questions:
    question_count = question_count + 1

    if question_count > 75 and question_count < 80:
        print("Question text:")
        question_parts=textwrap.wrap(question, width = 50)

        for i in question_parts:
            print(i)
        score = sia.polarity_scores(question)

        for i in score:
            print(i, score[i])
        print()

print("Total number of questions: ", question_count)

