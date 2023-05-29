import json
import numpy as np
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder
import string
from tensorflow import keras
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


class MktBotModel:
    def __init__(self):
        self.responses = {}
        self.data = None
        self.train = None
        self.tokenizer = None
        self.input_shape = None
        self.x_train = None
        self.y_train = None
        self.le = LabelEncoder()

    def preprocessing(self):
        with open("./chatbot_model/intents.json") as content:
            data1 = json.load(content)
        # getting all the data to lists
        tags = []
        inputs = []
        responses = {}
        for intent in data1["intents"]:
            self.responses[intent["tag"]] = intent["responses"]
            for lines in intent["patterns"]:
                inputs.append(lines)
                tags.append(intent["tag"])

        # converting to dataframe
        self.data = pd.DataFrame({"patterns": inputs, "tags": tags})

        # removing punctuations
        self.data["patterns"] = self.data["patterns"].apply(
            lambda wrd: [ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation]
        )
        self.data["patterns"] = self.data["patterns"].apply(lambda wrd: "".join(wrd))
        # tokenize the data

        self.tokenizer = Tokenizer(num_words=2000)
        self.tokenizer.fit_on_texts(self.data["patterns"])
        self.train = self.tokenizer.texts_to_sequences(self.data["patterns"])
        # apply padding
        self.x_train = pad_sequences(self.train)

        # encoding the outputs
        self.y_train = self.le.fit_transform(self.data["tags"])

        # input length
        self.input_shape = self.x_train.shape[1]

    def compute_model(self):
        # define vocabulary
        vocabulary = len(self.tokenizer.word_index)

        # output length
        output_length = self.le.classes_.shape[0]

        # creating the model
        i = Input(shape=(self.input_shape,))
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
        train = model.fit(self.x_train, self.y_train, epochs=200)
        model.save("chatbot_model.keras")
        

    def compute_prediction(self, query_input):
        loaded_model = keras.models.load_model("./chatbot_model/chatbot_model.keras", compile=False)
        texts_p = []
        # removing punctuation and converting to lowercase
        prediction_input = [
            letters.lower()
            for letters in query_input
            if letters not in string.punctuation
        ]

        prediction_input = "".join(prediction_input)

        texts_p.append(prediction_input)
        # getting all the data to liststy

        # tokenizing and padding
        prediction_input = self.tokenizer.texts_to_sequences(texts_p)

        prediction_input = np.array(prediction_input).reshape(-1)
        prediction_input = pad_sequences([prediction_input], self.input_shape)
        # getting output from model

        output = loaded_model.predict(prediction_input)
        output = output.argmax()
        # finding the right tag and predicting
        response_tag = self.le.inverse_transform([output])[0]
        return {"tag":response_tag,"response":random.choice(self.responses[response_tag])}
