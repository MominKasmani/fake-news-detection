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
