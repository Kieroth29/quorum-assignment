import { fetchBills, fetchLegislators } from "./lib/data";
import { LegislatorTable } from "./components/LegislatorTable";
import { BillTable } from "./components/BillTable";

export default async function Home() {
  const legislatorsData = await fetchLegislators();
  const billsData = await fetchBills();

  return (
    <div>
      <main className="bg-white dark:bg-gray-800 text-gray-900 dark:text-white">
        <div className="container mx-auto p-4">
          <h1 className="text-2xl font-bold mb-4">Legislators</h1>
          <LegislatorTable data={legislatorsData} />

          <h1 className="text-2xl font-bold my-4">Bills</h1>
          <BillTable data={billsData} />
        </div>
      </main>
    </div>
  );
}
