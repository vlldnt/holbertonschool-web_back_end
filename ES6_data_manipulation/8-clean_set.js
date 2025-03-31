export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  return Array.from(set)
    .filter((values) => values.startsWith(startString) && typeof values === 'string')
    .map((values) => values.slice(startString.length)).join('-');
}
