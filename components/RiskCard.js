export default function RiskCard({
  title,
  risk,
  description
}) {
  return (
    <div className="border rounded-xl p-5 shadow-sm">
      <h3 className="font-bold text-lg">
        {title}
      </h3>

      <p className="mt-2">
        Risk Level: {risk}
      </p>

      <p className="mt-3 text-sm">
        {description}
      </p>
    </div>
  );
}
