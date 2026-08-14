export function generateReportData(
  medicines,
  interactions
) {
  return {
    generatedAt: new Date(),
    medicines,
    interactions
  };
}
