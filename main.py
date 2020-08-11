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
    [
        14,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
    ],
    [
        13,  # Age
        0,  # Gender
        0,  # Heart Disease
        0,  # Diabetes
        0,  # Chronic Respitory Disease
        0,  # Hypertension
        0,  # Cancer
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
    0.8093,
    1.0000,
    1.0000,
]

if len(data) != len(percentages):
    print("Bad dataset")
    quit()

reg = linear_model.LinearRegression()
reg.fit(data, percentages)

age = int(input("Enter Age: "))
gender = input("Enter Gender (m/f): ")

heart = input("Do you have heart disease (y/n): ").lower()
diab = input("Do you have diabetes (y/n): ").lower()
chron = input("Do you have Chronic Respiratory Disease (y/n): ").lower()
hyper = input("Do you have Hypertension (y/n): ").lower()
cancer = input("Do you have cancer (y/n): ").lower()

if gender == "m":
    gender = 0
elif gender == "f":
    gender = 1

if heart == "y":
    heart = 1
elif heart == "n":
    heart = 0

if diab == "y":
    diab = 1
elif diab == "n":
    diab = 0

if chron == "y":
    chron = 1
elif chron == "n":
    chron = 0

if hyper == "y":
    hyper = 1
elif hyper == "n":
    hyper = 0

if cancer == "y":
    cancer = 1
elif cancer == "n":
    cancer = 0


test = [
    [
        age,  # Age
        gender,  # Gender
        heart,  # Heart Disease
        diab,  # Diabetes
        chron,  # Chronic Respitory Disease
        hyper,  # Hypertension
        cancer  # Cancer
    ],
]

predictions = reg.predict(test)

if predictions[0] < 0:
    predictions[0] = 0.0
elif predictions[0] > 1:
    predictions[0] = 1.0

print("Survive probability:", predictions)
