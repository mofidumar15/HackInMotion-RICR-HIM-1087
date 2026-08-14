export function removeDuplicateMedicines(list) {
  const unique = new Map();

  list.forEach(item => {
    unique.set(item.rxcui, item);
  });

  return [...unique.values()];
}
