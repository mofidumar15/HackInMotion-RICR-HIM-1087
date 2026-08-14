"use client";

import { useState } from "react";
import { extractPrescriptionText } from "../services/ocrService";

export default function PrescriptionOCR() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const response =
      await extractPrescriptionText(file);

    setResult(response.text || "");
  };

  return (
    <div className="space-y-4">
      <input
        type="file"
        onChange={(e) =>
          setFile(e.target.files?.[0])
        }
      />

      <button
        onClick={handleUpload}
        className="px-4 py-2 bg-green-600 text-white rounded"
      >
        Extract Medicines
      </button>

      <div className="border p-4 rounded">
        {result}
      </div>
    </div>
  );
}
