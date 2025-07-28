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