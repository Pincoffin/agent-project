
def summarize_data(data):
    # Calculate basic statistics
    mean = sum(data) / len(data)
    median = sorted(data)[len(data) // 2]
    return {
        'mean': mean,
        'median': median
    }
