
def get_median(arr):
    """Hàm tự viết để tìm trung vị của một mảng đã sắp xếp."""
    n = len(arr)
    if n == 0:
        return 0
    
    mid = n // 2
    if n % 2 != 0:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2.0

def robust_scaling(values):

    sorted_vals = sorted(values)
    n = len(sorted_vals)
    
    median = get_median(sorted_vals)
    
    mid = n // 2
    if n % 2 != 0:
        lower_half = sorted_vals[:mid]
        upper_half = sorted_vals[mid+1:]
    else:
        lower_half = sorted_vals[:mid]
        upper_half = sorted_vals[mid:]
        
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    
    iqr = q3 - q1
    
    if iqr == 0:
        values_scaled = [(x - median) for x in values]
    else:
        values_scaled = [(x - median) / iqr for x in values]
        
    return values_scaled
    
    
    
        