const RXNORM_BASE_URL = "https://rxnav.nlm.nih.gov/REST";

export async function searchMedicine(query) {
  if (!query?.trim()) return [];

  try {
    const response = await fetch(
      `${RXNORM_BASE_URL}/drugs.json?name=${encodeURIComponent(query)}`
    );

    const data = await response.json();

    const groups = data?.drugGroup?.conceptGroup || [];

    const medicines = [];

    groups.forEach(group => {
      if (group.conceptProperties) {
        medicines.push(...group.conceptProperties);
      }
    });

    return medicines;
  } catch (error) {
    console.error(error);
    return [];
  }
}

export async function getDrugProperties(rxcui) {
  try {
    const response = await fetch(
      `${RXNORM_BASE_URL}/rxcui/${rxcui}/properties.json`
    );

    const data = await response.json();

    return data.properties || null;
  } catch {
    return null;
  }
}
