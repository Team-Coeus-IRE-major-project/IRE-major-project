import pandas as pd
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--out_preds', type=Path,
                    help='predictions for each test entry')
parser.add_argument('--test_file', type=Path,
                    help='location of test csv')
parser.add_argument('--dest_file', type=Path, default=Path('results.csv'),
                    help='destination csv file to write results to',
                    required=False)


if __name__ == '__main__':
    args = parser.parse_args()

    test_data = pd.read_csv(args.test_file)
    with open(args.out_preds, 'r') as f:
        preds = f.readlines()

    test_data["predictions"] = preds
    req_cols = ['plot_synopsis', 'tagline', 'predictions']
    test_data[req_cols].to_csv(args.dest_file)
