import { useState } from "react";

export default function useOCR() {
  const [text, setText] = useState("");

  return {
    text,
    setText
  };
}
