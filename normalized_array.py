import numpy as np

def normalized_array(arr_in):
    # המרה למערך מסוג float
    arr = np.array(arr_in, dtype=float)
    
    # חומת מגן: טיפול במקרה של מערך ריק
    if len(arr) == 0:
        return np.array([])
        
    # חישוב הערך המינימלי והמקסימלי פעם אחת בלבד
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # אם המינימום שווה למקסימום, כל האיברים זהים
    if min_val == max_val:
        return np.zeros_like(arr)
        
    # ביצוע הנרמול (שימוש במשתנים שכבר חישבנו חוסך פעולות כפולות)
    result_arr = (arr - min_val) / (max_val - min_val)
    
    return result_arr

if __name__ == "__main__":
    # נתוני בדיקה
    sample_list = [10, 20, 30, 40, 50]
    print(f"Before normalization: {sample_list}")
    print(f"After normalization:  {normalized_array(sample_list)}")
