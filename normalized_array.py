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
import numpy as np

def normalize_array(data):
    # המרה למערך NumPy כדי שנוכל להשתמש בתכונות שלו
    data = np.asanyarray(data)
    
    # בדיקה שהמערך הוא חד-ממדי (לפי הדרישה)
    if data.ndim != 1:
        raise ValueError("Input must be a 1D NumPy array")
    
    min_val = np.min(data)
    max_val = np.max(data)
    diff = max_val - min_val
    
    # טיפול במקרה שכל הערכים זהים (כדי למנוע חלוקה באפס)
    if diff == 0:
        return np.zeros_like(data, dtype=float)
    
    # החזרת המערך המנורמל (ערכים בין 0 ל-1)
    return (data - min_val) / diff

# ==========================================
# דוגמאות שימוש
# ==========================================
if __name__ == "__main__":
    # דוגמה 1: מערך רגיל עם מספרים חיוביים
    arr1 = [10, 20, 30, 40, 50]
    print("--- Example 1 ---")
    print(f"Original:   {arr1}")
    print(f"Normalized: {normalize_array(arr1)}\n")
    
    # דוגמה 2: מערך שמכיל מספרים שליליים
    arr2 = np.array([-50, 0, 50, 100])
    print("--- Example 2 ---")
    print(f"Original:   {arr2}")
    print(f"Normalized: {normalize_array(arr2)}\n")
    
    # דוגמה 3: מקרה קצה - כל הערכים זהים
    arr3 = [7, 7, 7, 7]
    print("--- Example 3 ---")
    print(f"Original:   {arr3}")
    print(f"Normalized: {normalize_array(arr3)}\n")
