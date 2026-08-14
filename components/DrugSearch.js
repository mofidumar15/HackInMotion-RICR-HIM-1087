"use client";

import { useState } from "react";
import useDrugSearch from "../hooks/useDrugSearch";

export default function DrugSearch() {
  const [query, setQuery] = useState("");
  const { results, search } = useDrugSearch();

  const handleSearch = async () => {
    await search(query);
  };

  return (
    <div className="space-y-4">
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search medicine..."
        className="w-full border p-3 rounded"
      />

      <button
        onClick={handleSearch}
        className="px-4 py-2 bg-blue-600 text-white rounded"
      >
        Search
      </button>

      <div className="space-y-2">
        {results.map((item) => (
          <div
            key={item.rxcui}
            className="border rounded p-3"
          >
            <div>{item.name}</div>
            <div>RxCUI: {item.rxcui}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
