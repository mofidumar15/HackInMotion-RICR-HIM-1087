export async function generateAISummary(interactions) {
  try {
    const response = await fetch("/api/gemini-summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ interactions })
    });

    return await response.json();
  } catch (error) {
    console.error(error);

    return {
      summary:
        "Unable to generate AI summary."
    };
  }
}
