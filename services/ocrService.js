export async function extractPrescriptionText(file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    "/api/ocr",
    {
      method: "POST",
      body: formData
    }
  );

  return response.json();
}
