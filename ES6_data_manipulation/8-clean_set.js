export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }
  return Array.from(set)
    .filter((values) => values.startsWith(startString))
    .map((values) => values
      .slice(startString.length));
}
