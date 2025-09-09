def in_range(value, lo, hi) -> bool:
    """数値を前提に閉区間 [lo, hi] 判定。"""
    return lo <= value <= hi

def add(a, b, c=0):
  nums = (a, b, c)
  if any(not isinstance(v, (int, float)) for v in nums):
     return -1
  if any(not in_range(v, 0, 10) for v in nums):
     return -2
  
  try:
    return int(a + b) + int(c)
  except:
      return "error"

