const getCombinations = (strand, length) => {
  const depth = 1;
  
  const combinations = (base, array, currentDepth) => array
    .flatMap((unit, index, arr) => currentDepth < length
      ? combinations(base + unit, arr.toSpliced(index, 1), currentDepth + 1)
      : base + unit)

  return strand
    .split('')
    .flatMap((unit, index, array) => combinations(unit, array.toSpliced(index, 1), depth + 1));
}

const result = getCombinations('hack', 3)
console.log(result)
