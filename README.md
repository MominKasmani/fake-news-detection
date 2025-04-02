# fake-news-detection

# LLM-Based Fake News Detection

A fake news detection system using OpenAI's GPT models with prompt engineering.

## Repository Structure

- `main.py`: Main execution script
- `preprocessing.py`: Data loading and text processing functions
- `prompts.py`: Templates for zero-shot and few-shot classification
- `classification.py`: OpenAI API interaction for classification
- `evaluation.py`: Results calculation and visualization

## Setup

1. Clone this repository
2. Install required packages: `pip install -r requirements.txt`
3. Set your OpenAI API key: `export OPENAI_API_KEY="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"`

## Usage

1. Download the FakeNewsNet dataset
2. Run: `python main.py --dataset_path /path/to/fakenewsnet`

Results will be saved to the `results/` directory.
