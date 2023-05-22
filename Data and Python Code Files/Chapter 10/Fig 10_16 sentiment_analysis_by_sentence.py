from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Construct a sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

sentence = "The service here was very good"
sentence2 = "The service here was not good"

def measure_sentence(sentence):
    print(sentence)

     # Determine sentiment strength values
    score = sia.polarity_scores(sentence)
    for i in score:
        print(i, score[i])

measure_sentence(sentence)
print("\n")
measure_sentence(sentence2)

