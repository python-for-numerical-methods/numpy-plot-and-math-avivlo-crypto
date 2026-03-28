import numpy as np

def normalize_array(data):
    # המרה למערך NumPy כדי שנוכל להשתמש בתכונות שלו
    data = np.asanyarray(data)
    
    # בדיקה שהמערך הוא חד-ממדי (לפי הדרישה במשימה)
    if data.ndim != 1:
        raise ValueError("Input must be a 1D NumPy array")
    
    min_val = np.min(data)
    max_val = np.max(data)
    diff = max_val - min_val
    
    # טיפול במקרה שכל הערכים זהים
    if diff == 0:
        return np.zeros_like(data, dtype=float)
    
    # החזרת המערך המנורמל
    return (data - min_val) / diff
