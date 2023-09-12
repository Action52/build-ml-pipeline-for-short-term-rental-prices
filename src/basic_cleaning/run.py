#!/usr/bin/env python
"""
Downloads the dataset from weights and biases, applies basic data cleaning,
and exports the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    logging.info("Initiating the basic cleaning job.")
    run = wandb.init(job_type="basic_cleaning", save_code=True)
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    # Get the latest sample artifact filepath
    logging.info("Extracting artifact from W&B.")
    local_path = run.use_artifact(args.input_artifact).file()

    # Load the df
    logging.info("Loading artifact into DataFrame.")
    df = pd.read_csv(local_path)

    # Perform data cleaning
    logging.info("Performing data cleaning steps.")
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()
    df['last_review'] = pd.to_datetime(df['last_review'])

    # Save the clean df and upload to W&B
    logging.info("Saving clean sample into csv.")
    df.to_csv(args.output_artifact, index=False)

    logging.info("Uploading artifact to W&B.")
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description
    )
    artifact.add_file(args.output_artifact)
    run.log_artifact(artifact)

    # Terminate the run
    run.finish()
    logging.info("SUCCESS.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="The artifact that we will process as input. "
             "For example: sample.csv:latest",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="The name of the resulting artifact. i.e: sample_cleaned.csv.",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="Type for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="The resulting artifact will be a cleaned version of the original "
             "input artifact",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Minimum price to restrict the artifact. i.e: 10",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Maximum price to restrict the artifact. i.e: 350",
        required=True
    )

    args = parser.parse_args()

    go(args)
