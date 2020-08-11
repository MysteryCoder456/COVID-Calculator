import sklearn
from sklearn import linear_model

feature_names = [
    "Age",
    "Gender(M=0, F=1)",
    "Heart Disease(0/1)",
    "Diabetes(0/1)",
    "Chronic Respitory Disease(0/1)",
    "Hypertension(0/1)",
    "Cancer(0/1)"
]

data = [
    [
        5,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        15,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        35,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        45,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        55,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        65,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        75,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        90,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        5,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        15,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        35,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        45,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        75,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        90,  # Age
        1,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],


    [
        25,  # Age
        1,  # Gender
        1,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        1,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        1,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        1,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        1,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        1,  # Chronic Respitory Disease
        1,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        1,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        1,  # Chronic Respitory Disease
        1,  # Hypertension
        1,  # Cancer
    ],


    [
        25,  # Age
        0,  # Gender
        1,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        0,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        0,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        1,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        0,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        1,  # Chronic Respitory Disease
        1,  # Hypertension
        0,  # Cancer
    ],
    [
        25,  # Age
        0,  # Gender
        1,  # Heart Disease
        1,  # Diabetes
        1,  # Chronic Respitory Disease
        1,  # Hypertension
        1,  # Cancer
    ],
]

# probability for not being infected
percentages = [
    1.0000,
    0.9992,
    0.9992,
    0.9984,
    0.9967,
    0.9934,
    0.9777,
    0.9340,
    0.8680,
    1.0000,
    0.9993,
    0.9993,
    0.9987,
    0.9973,
    0.9460,
    0.8920,
    0.9290,
    0.9044,
    0.8831,
    0.8628,
    0.8439,
    0.9132,
    0.8831,
    0.8571,
    0.8324,
    0.8093
]

reg = linear_model.LinearRegression()
reg.fit(data, percentages)

test = [
    [
        48,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        1,  # Hypertension
        0,  # Cancer
    ],
]

predictions = reg.predict(test)
print("Survive probability:", predictions)
