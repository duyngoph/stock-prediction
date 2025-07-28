# Stock Prediction Project

This project aims to predict the movement of the US S&P 500 index for the next day using a combination of classical machine learning techniques and large language models (LLMs). The project incorporates ARIMA for time-series analysis and sentiment analysis, culminating in a chatbot that prompts users for stock names and provides predictions and explanations.

## Project Structure

```
stock-prediction
├── data
│   ├── raw
│   │   └── sp500.csv
│   └── processed
│       └── sentiment_data.csv
├── notebooks
│   ├── 01_data_collection.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_sentiment_analysis.ipynb
│   ├── 04_arima_modeling.ipynb
│   └── 05_model_evaluation.ipynb
├── src
│   ├── data
│   │   ├── collect.py
│   │   └── preprocess.py
│   ├── models
│   │   ├── arima.py
│   │   ├── sentiment.py
│   │   └── ensemble.py
│   ├── utils
│   │   ├── config.py
│   │   └── helpers.py
│   └── api
│       ├── chatbot.py
│       └── endpoints.py
├── tests
│   ├── test_data.py
│   ├── test_models.py
│   └── test_api.py
├── requirements.txt
├── config.yaml
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd stock-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Collection**: Use the Jupyter notebooks in the `notebooks` directory to collect and preprocess data.
2. **Modeling**: Implement and evaluate models using the provided scripts in the `src/models` directory.
3. **Chatbot**: Run the chatbot script to interact with users and provide stock predictions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.