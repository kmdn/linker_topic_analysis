#!which python
from trainer import Trainer
import constants

import json
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import random
from top2vec import Top2Vec
random.seed(42)
np.random.seed(42)


def populate_embeddings_labels_rawtext():
    embeddings = {}
    text_labels = []
    raw_text_labels_files = []

    for file_path in constants.file_paths:
        with open(file_path + "_embeddings_.json", "r") as f:
            embeddings_objects = json.load(f)
            for emb_obj in embeddings_objects:
                embeddings[emb_obj["hash"]] = np.array(emb_obj["embeddings"])

        with open(file_path + "_labeled_fewer_classes.json", "r") as f:
            text_labels_file = json.load(f)
            raw_text_labels_files.append({'ds': file_path, 'raw': text_labels_file})
            for text_hash, doc_info in text_labels_file.items():
                labels_list = [label["system"] for label in doc_info["label"]]
                text_labels.append((text_hash, labels_list))

    return embeddings, text_labels, raw_text_labels_files



def filtered_embeddings_textlabels_docvalues():
    embeddings, text_labels, raw_text_labels_files = populate_embeddings_labels_rawtext()
    # Assuming your initial data processing steps
    filtered_embeddings = []
    filtered_text_labels = []
    doc_values_initial = []
    doc_values = []

    for item in raw_text_labels_files:
        raw_data = item.get('raw', {})
        for key, value in raw_data.items():
            doc_value = value.get('doc')
            if doc_value:
                doc_values_initial.append(doc_value)

    for i, (sample_id, classes) in enumerate(text_labels):
        if classes:
            for label in classes:
                filtered_embeddings.append(embeddings[sample_id])
                filtered_text_labels.append(label)
                doc_values.append(doc_values_initial[i])

    return filtered_embeddings, filtered_text_labels, doc_values

#import nltk
#nltk.download('stopwords')


def remove_stopwords(text):
    text = [word for word in text if word not in constants.stopwords]
    return text

def tok(text):
    import gensim
    text = gensim.utils.simple_preprocess(text)
    text = remove_stopwords(text)
    return text


filtered_embeddings, filtered_text_labels, doc_values = filtered_embeddings_textlabels_docvalues()

print(f"Number of documents: {len(doc_values)}")
print("Running topic modeling...")
topic_model = Top2Vec(
    doc_values,
    #    embedding_model="doc2vec",#"all-MiniLM-L6-v2",#"universal-sentence-encoder",
    #embedding_model="universal-sentence-encoder",
    embedding_model="distiluse-base-multilingual-cased",
    speed="deep-learn",
    tokenizer=tok,
    ngram_vocab=True,
    ngram_vocab_args={"connector_words": "phrases.ENGLISH_CONNECTOR_WORDS"},
)

model_path = constants.model_path
print(f"Saving model to {model_path}")
topic_model.save(model_path)
print("Model saved successfully.")