def get_combinations(strand, length):
  def combinations(base, array, current_depth):
    if current_depth < length:
      result = []
      for index, unit in enumerate(array):
        remaining = array[:index] + array[index+1:]
        result.extend(combinations(base + unit, remaining, current_depth + 1))
      return result
    return [base]

  strand_list = list(strand)
  result = []
  for index, unit in enumerate(strand_list):
    remaining = strand_list[:index] + strand_list[index+1:]
    result.extend(combinations(unit, remaining, 1))
  
  return result
