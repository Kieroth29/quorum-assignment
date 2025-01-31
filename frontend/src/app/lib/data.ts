import { IBill } from "../types/Bill";
import { ILegislator } from "../types/Legislator";

export async function fetchLegislators(): Promise<Array<ILegislator>> {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_BACKEND_HOST}/legislation/legislators`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch data");
  }

  return response.json();
}

export async function fetchBills(): Promise<Array<IBill>> {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_BACKEND_HOST}/legislation/bills`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch data");
  }

  return response.json();
}
