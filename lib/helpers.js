export function formatDate(date) {
  return new Date(date).toLocaleString();
}

export function truncate(text, length = 100) {
  if (!text) return "";

  return text.length > length
    ? text.substring(0, length) + "..."
    : text;
}
