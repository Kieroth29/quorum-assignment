import React from "react";
import { DataTable } from "./DataTable";
import { ILegislator } from "../types/Legislator";
import { ColumnDef } from "@tanstack/react-table";

const columns: ColumnDef<ILegislator>[] = [
  {
    accessorKey: "id",
    header: "ID",
  },
  {
    accessorKey: "legislator",
    header: "Legislator",
  },
  {
    accessorKey: "supportedBills",
    header: "Supported Bills",
  },
  {
    accessorKey: "opposedBills",
    header: "Opposed Bills",
  },
];

interface LegislatorTableProps {
  data: ILegislator[];
}

export function LegislatorTable({ data }: LegislatorTableProps) {
  return <DataTable columns={columns} data={data} />;
}
