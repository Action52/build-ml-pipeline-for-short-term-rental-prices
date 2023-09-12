# ML Pipeline for Short-Term Rental Prices in NYC

## Overview
This project aims to provide an end-to-end pipeline to estimate the typical price for a given property based on similar properties' prices. As the property management company receives new data every week, the model is designed to be retrained on this cadence, ensuring the predictions remain accurate and up-to-date. The primary focus is on properties and rooms rented for short periods on various platforms in New York City.

## Features
- Automated data ingestion and preprocessing.
- Training of a prediction model based on historical prices of similar properties.
- Regular retraining capabilities with new data.
- Easily reusable for weekly data updates.

The project is implemented using MLFlow and Weights and Biases to version and control the pipeline.

## Dependencies
- Since the project is executed with mlflow, you need a working mlflow version.

## Usage
Simply run, as an example:
```bash
mlflow run  https://github.com/Action52/build-ml-pipeline-for-short-term-rental-prices.git -v 1.0.1 -P hydra_options="etl.sample='sample2.csv'"
```
Feel free to modify the parameters of the run as needed.


## W&B Project Dashboard
For a comprehensive overview of the model training, evaluation, and other insightful metrics, visit the W&B dashboard at the following link:

[https://wandb.ai/leonvillapun/nyc_airbnb/overview?workspace=user-leonvillapun](https://wandb.ai/leonvillapun/nyc_airbnb/overview?workspace=user-leonvillapun)

## Note
This project is a solution for the Udacity Machine Learning DevOps nanodegree, specifically in the Building Reproducible ML Workflows course. 
Most of the code has already been provided. The modifications include my solution to the posted problem.
