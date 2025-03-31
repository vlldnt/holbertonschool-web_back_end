export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [keys, value] of map.entries()) {
    if (value === 1) {
      map.set(keys, 100);
    }
  }
}
