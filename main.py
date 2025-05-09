import os
import sys

# Ensure GitHub Actions runner can find local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from apex_engine.main_engine import run_daily_predictions
from export_predictions import export_to_csv


if __name__ == '__main__':
    run_daily_predictions()
    export_to_csv()
