"""
Module which represents to the data validation step.
"""

import os

from datasets import load_dataset, load_from_disk
from transformers import AutoTokenizer

from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class DataTransformation:
    def __init__(self, config: entities.DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        """
        Convert the examples to features.
        """
        input_encodings = self.tokenizer(example_batch['document'] , max_length = 800, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        """
        Tokenzie the dataset and store it to the disk.
        """
        backend_logger.info("Converting text to tokens....")
        dataset = load_from_disk(self.config.data_path)
        dataset = dataset.map(self.convert_examples_to_features, batched = True)
        dataset.save_to_disk(os.path.join(self.config.root_dir,"dataset"))
        backend_logger.info("Converted text to tokens.")
