
def CSVDataAnalyzer(**kwargs):
    import pandas as pd
    
    path = kwargs.get('path')
    if not path:
        raise ValueError("Path to the CSV file is required.")
    
    df = pd.read_csv(path)
    summary = {
        'columns': df.columns.tolist(),
        'shape': df.shape,
        'statistics': df.describe().to_dict()
    }
    return summary
