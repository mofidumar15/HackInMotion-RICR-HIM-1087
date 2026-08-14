export function calculateRiskScore(interactions) {
  if (!interactions?.length) return 0;

  let score = 0;

  interactions.forEach(item => {
    if (item.severity === "Severe") score += 40;
    else if (item.severity === "Moderate") score += 20;
    else score += 10;
  });

  return Math.min(score, 100);
}

export function getRiskLabel(score) {
  if (score >= 70) return "High Risk";
  if (score >= 40) return "Moderate Risk";
  return "Low Risk";
}
