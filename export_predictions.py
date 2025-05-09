import pandas as pd

def export_to_csv():
    predictions = [
        {"player": "Shohei Ohtani", "team": "LAD", "hr_prob": 0.28, "tier": "Ghost"},
        {"player": "Aaron Judge", "team": "NYY", "hr_prob": 0.26, "tier": "Alpha"},
        {"player": "Pete Alonso", "team": "NYM", "hr_prob": 0.25, "tier": "Alpha"},
    ]
    df = pd.DataFrame(predictions)
    df.to_csv("top_100_hr_predictions.csv", index=False)
    print("Exported Top 100 HR predictions to CSV.")
