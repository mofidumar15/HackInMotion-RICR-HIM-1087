import DrugSearch from "../components/DrugSearch";
import InteractionChecker from "../components/InteractionChecker";
import PrescriptionOCR from "../components/PrescriptionOCR";

export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-8">
        CureDrug
      </h1>

      <div className="grid gap-8">
        <DrugSearch />

        <InteractionChecker />

        <PrescriptionOCR />
      </div>
    </main>
  );
}
