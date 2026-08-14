export function isValidMedicine(value) {
  return value && value.trim().length > 1;
}

export function isValidImage(file) {
  if (!file) return false;

  return file.type.startsWith("image/");
}
