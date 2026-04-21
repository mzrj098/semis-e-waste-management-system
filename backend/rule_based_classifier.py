def classify_waste(fill_percent, temperature):
    """
    Simple rule-based classification (as described in Chapter 4.3 and 4.6 of the thesis)
    No Machine Learning - only rules (because we used synthetic data)
    """
    if temperature > 45:
        return "Hazardous"
    elif fill_percent > 80:
        return "Recyclable - Full Bin"
    else:
        return "Reusable / Recyclable"
