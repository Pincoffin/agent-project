import statistics
def calculate_statistics(numbers):
    return {
        'mean': statistics.mean(numbers),
        'median': statistics.median(numbers),
        'mode': statistics.mode(numbers)
    }