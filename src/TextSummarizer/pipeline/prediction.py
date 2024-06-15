from transformers import pipeline

from src.TextSummarizer.config.config_manager import ConfigManager


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_model_evaluation_config()

    def predict(self,text):
        """
        Predict the tex summarization for the given text.
        """
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        summarizer = pipeline("summarization", model=self.config.hub_model_name)

        print("document:")
        print(text)

        output = summarizer(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output
