import html
import json
import logging
import os
import os.path as pth
import re
import spacy

from sklearn.model_selection import train_test_split
from spacy.util import filter_spans
from spacy.tokens import DocBin
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)

def trim_entity_spans(data: list) -> list:
    """Removes leading and trailing white spaces from entity spans.

    Args:
        data (list): The data to be cleaned in spaCy JSON format.

    Returns:
        list: The cleaned data.
    """
    invalid_span_tokens = re.compile(r'\s')

    cleaned_data = []
    for text, annotations in data:
        entities = annotations['entities']
        valid_entities = []
        for start, end, label in entities:
            valid_start = start
            valid_end = end
            while valid_start < valid_end and invalid_span_tokens.match(
                    text[valid_start]):
                valid_start += 1
            while valid_end > valid_start and invalid_span_tokens.match(
                    text[valid_end - 1]):
                valid_end -= 1
            if valid_start == valid_end:
                continue
            valid_entities.append([valid_start, valid_end, label])
        cleaned_data.append([text, {'entities': valid_entities}])

    return cleaned_data


def convert_dataturks_to_spacy(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines = []
        with open(dataturks_JSON_FilePath, 'r', encoding="utf8") as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            text = html.unescape(data['content'])
            entities = []
            if data['annotation'] is not None:
                for annotation in data['annotation']:
                    # only a single point in text annotation.
                    point = annotation['points'][0]
                    labels = annotation['label']
                    # handle both list of labels or a single label.
                    if not isinstance(labels, list):
                        labels = [labels]

                    for label in labels:
                        # dataturks indices are both inclusive [start, end]
                        # but spacy is not [start, end)
                        entities.append((
                            point['start'],
                            point['end'] + 1,
                            label
                        ))

            training_data.append((text, {"entities": entities}))
        return training_data
    except Exception:
        logging.exception("Unable to process " + dataturks_JSON_FilePath)
        return None


def get_train_data(path: str = "traindata.json"):
    return trim_entity_spans(convert_dataturks_to_spacy(path))


def save_as_spacy_corpus(
    data: list, dest: str = '', dev_size: float = 0.20) -> list:
    os.makedirs(dest, exist_ok=True)
    nlp = spacy.load('en_core_web_sm')
    db_train = DocBin()
    db_dev = DocBin()
    docs = []
    for text, entities in tqdm(data, desc='Processing resumes'):
        spans = []
        doc = nlp(text)
        for start, end, label in entities['entities']:
            span = doc.char_span(start, end, label)
            if span is None:
                continue
            spans.append(doc.char_span(start, end, label))
        doc.set_ents(filter_spans(spans))
        docs.append(doc)
    train, dev, _, _ = train_test_split(docs, docs, test_size=dev_size)
    for doc in train:
        db_train.add(doc)
    for doc in dev:
        db_dev.add(doc)
    db_train.to_disk(pth.join(dest, f'train.spacy'))
    db_dev.to_disk(pth.join(dest, f'dev.spacy'))
        

if __name__ == "__main__":
    logging.info('Loading dataturks data...')
    data = get_train_data(pth.join(pth.dirname(__file__), 'traindata.json'))
    save_as_spacy_corpus(data, dest=pth.join(pth.dirname(__file__), 'data'))
