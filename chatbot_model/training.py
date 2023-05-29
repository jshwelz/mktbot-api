# importing the libraries
import json
import numpy as np
import string
import pandas as pd
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import (
    Input,
    Embedding,
    LSTM,
    Dense,
    Flatten,
)
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

# Read intents from JSON file
with open("intents.json") as content:
    data1 = json.load(content)
# getting all the data to lists
tags = []
inputs = []
responses = {}
for intent in data1["intents"]:
    responses[intent["tag"]] = intent["responses"]
    for lines in intent["patterns"]:
        inputs.append(lines)
        tags.append(intent["tag"])

# converting to dataframe
data = pd.DataFrame({"patterns": inputs, "tags": tags})


# removing punctuations
data["patterns"] = data["patterns"].apply(
    lambda wrd: [ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation]
)
data["patterns"] = data["patterns"].apply(lambda wrd: "".join(wrd))
# tokenize the data


tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(data["patterns"])
train = tokenizer.texts_to_sequences(data["patterns"])

# apply padding
x_train = pad_sequences(train)

# encoding the outputs


le = LabelEncoder()
y_train = le.fit_transform(data["tags"])

# input length
input_shape = x_train.shape[1]

# define vocabulary
vocabulary = len(tokenizer.word_index)

# output length
output_length = le.classes_.shape[0]


# creating the model
i = Input(shape=(input_shape,))
x = Embedding(vocabulary + 1, 10)(i)
x = LSTM(10, return_sequences=True)(x)
x = Flatten()(x)
x = Dense(output_length, activation="softmax")(x)
model = Model(i, x)
# compiling the model
model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer=keras.optimizers.Adam(),
    metrics=["accuracy"],
)
# training the model
train = model.fit(x_train, y_train, epochs=200)

model.save("chatbot_model.keras")
