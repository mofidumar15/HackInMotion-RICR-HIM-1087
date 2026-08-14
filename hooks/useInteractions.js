import { useState } from "react";

export default function useInteractions() {
  const [interactions, setInteractions] = useState([]);

  return {
    interactions,
    setInteractions
  };
}
