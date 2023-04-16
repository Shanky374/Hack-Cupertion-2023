import numpy as np
from sklearn.linear_model import LinearRegression


# TRAINING DATA
# Responses to questions
Responses = np.array([
    [1, 1, 1, 1, 1, 1, 3],
    [1, 2, 2, 1, 1, 2, 4],
    [1, 2, 1, 2, 1, 1, 4],
    [1, 1, 2, 1, 1, 1, 4],
    [1, 1, 2, 2, 2, 2, 3],
    [1, 3, 2, 1, 2, 3, 2],
    [1, 2, 3, 2, 3, 3, 2],
    [1, 4, 3, 1, 1, 3, 2],
    [1, 3, 3, 2, 3, 3, 4],
    [1, 4, 2, 1, 3, 4, 3],
    [1, 2, 3, 1, 2, 3, 2],
    [1, 4, 3, 2, 1, 4, 2],
    [1, 2, 2, 1, 2, 3, 4],
    [1, 4, 5, 3, 2, 4, 5],
    [1, 2, 4, 2, 1, 2, 4],
    [1, 2, 3, 1, 2, 3, 4],
    [1, 2, 3, 2, 4, 3, 5],
    [1, 2, 4, 1, 4, 3, 5],
    [2, 2, 3, 2, 4, 3, 5],
    [2, 2, 3, 1, 2, 3, 4],
    [2, 2, 4, 2, 1, 2, 4],
    [2, 2, 1, 3, 1, 3, 4],
    [2, 3, 1, 2, 3, 2, 1],
    [2, 1, 2, 1, 3, 4, 4],
    [2, 2, 3, 2, 4, 3, 5],
    [2, 2, 3, 1, 2, 3, 4],
    [2, 2, 4, 2, 1, 2, 4],
    [2, 2, 1, 3, 1, 3, 4],
    [2, 3, 1, 2, 3, 2, 1],
    [2, 1, 2, 1, 3, 4, 4],
    [2, 2, 3, 2, 4, 3, 5],
    [2, 2, 3, 1, 2, 3, 4],
    [2, 2, 4, 2, 1, 2, 4],
    [2, 2, 1, 3, 1, 3, 4],
    [2, 3, 1, 2, 3, 2, 1],
    [2, 1, 2, 1, 3, 4, 4],
    [3, 2, 3, 2, 4, 3, 5],
    [3, 2, 3, 1, 2, 3, 4],
    [3, 2, 4, 2, 1, 2, 4],
    [3, 2, 1, 3, 1, 3, 4],
    [3, 3, 1, 2, 3, 2, 1],
    [3, 1, 2, 1, 3, 4, 4],
    [3, 2, 3, 2, 4, 3, 5],
    [3, 2, 3, 1, 2, 3, 4],
    [3, 2, 4, 2, 1, 3, 4],
    [3, 2, 1, 3, 1, 3, 4],
    [3, 3, 1, 2, 3, 2, 1],
    [3, 1, 2, 1, 3, 4, 4],
    [3, 2, 3, 2, 4, 3, 5],
    [3, 2, 2, 3, 1, 2, 3],
    [3, 2, 4, 2, 1, 2, 4],
    [3, 2, 1, 3, 1, 3, 4],
    [3, 3, 1, 2, 3, 2, 1],
    [3, 1, 2, 1, 3, 4, 4],
    [4, 1, 1, 1, 1, 1, 3],
    [4, 2, 2, 1, 1, 2, 4],
    [4, 2, 1, 2, 1, 1, 4],
    [4, 1, 2, 1, 1, 1, 4],
    [4, 1, 2, 2, 2, 2, 3],
    [4, 3, 2, 1, 2, 3, 2],
    [4, 2, 3, 2, 3, 3, 2],
    [4, 4, 3, 1, 1, 3, 2],
    [4, 3, 3, 2, 3, 3, 4],
    [4, 4, 2, 1, 3, 4, 3],
    [4, 2, 3, 1, 2, 3, 2],
    [4, 4, 3, 2, 1, 4, 2],
    [4, 2, 2, 1, 2, 3, 4],
    [4, 4, 5, 3, 2, 4, 5],
    [4, 2, 4, 2, 1, 2, 4],
    [4, 2, 3, 1, 2, 3, 4],
    [4, 2, 3, 2, 4, 3, 5],
    [4, 2, 4, 1, 4, 3, 5],
    [5, 1, 1, 1, 1, 1, 3],
    [5, 2, 2, 1, 1, 2, 4],
    [5, 2, 1, 2, 1, 1, 4],
    [5, 1, 2, 1, 1, 1, 4],
    [5, 1, 2, 2, 2, 2, 3],
    [5, 3, 2, 1, 2, 3, 2],
    [5, 2, 3, 2, 3, 3, 2],
    [5, 4, 3, 1, 1, 3, 2],
    [5, 3, 3, 2, 3, 3, 4],
    [5, 4, 2, 1, 3, 4, 3],
    [5, 2, 3, 1, 2, 3, 2],
    [5, 4, 3, 2, 1, 4, 2],
    [5, 2, 2, 1, 2, 3, 4],
    [5, 4, 5, 3, 2, 4, 5],
    [5, 2, 4, 2, 1, 2, 4],
    [5, 2, 3, 1, 2, 3, 4],
    [5, 2, 3, 2, 4, 3, 5],
    [5, 2, 4, 1, 4, 3, 5]]
).reshape((-1, 7))

# Classifications into groups
# Matches into 1 of 15 groups
Classifications = np.array([1, 1, 1, 1, 1, 1,
                            2, 2, 2, 2, 2, 2,
                            3, 3, 3, 3, 3, 3,
                            4, 4, 4, 4, 4, 4,
                            5, 5, 5, 5, 5, 5,
                            6, 6, 6, 6, 6, 6,
                            7, 7, 7, 7, 7, 7,
                            8, 8, 8, 8, 8, 8,
                            9, 9, 9, 9, 9, 9,
                            10, 10, 10, 10, 10, 10,
                            11, 11, 11, 11, 11, 11,
                            12, 12, 12, 12, 12, 12,
                            13, 13, 13, 13, 13, 13,
                            14, 14, 14, 14, 14, 14,
                            15, 15, 15, 15, 15, 15])

model = LinearRegression()
model.fit(Responses, Classifications)

r_sq = model.score(Responses, Classifications)

AnswerQuestion1=2
AnswerQuestion2=2
AnswerQuestion3=3
AnswerQuestion4=1
AnswerQuestion5=3
AnswerQuestion6=5
AnswerQuestion7=4


input = np.array([AnswerQuestion1, AnswerQuestion2, AnswerQuestion3, AnswerQuestion4, AnswerQuestion5, AnswerQuestion6, AnswerQuestion7]).reshape(-1, 7)
prediction = model.predict(input)

print(f"predicted response:\n{prediction}")

