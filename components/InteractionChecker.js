"use client";

import { useState } from "react";
import { apiPost } from "../lib/apiClient";

export default function InteractionChecker() {
  const [medicines, setMedicines] = useState("");
  const [result, setResult] = useState(null);

  const handleCheck = async () => {
    const data = await apiPost(
      "/api/check-interactions",
      {
        medicines: medicines
          .split("\n")
          .filter(Boolean)
      }
    );

    setResult(data);
  };

  return (
    <div className="space-y-4">
      <textarea
        rows={6}
        value={medicines}
        onChange={(e) =>
          setMedicines(e.target.value)
        }
        placeholder="Enter medicines..."
        className="w-full border p-3 rounded"
      />

      <button
        onClick={handleCheck}
        className="px-4 py-2 bg-red-600 text-white rounded"
      >
        Check Interactions
      </button>

      {result && (
        <pre className="border p-4 rounded">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}
