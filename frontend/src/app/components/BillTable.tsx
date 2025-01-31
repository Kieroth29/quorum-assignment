import React from "react";
import { DataTable } from "./DataTable";
import { IBill } from "../types/Bill";
import { ColumnDef } from "@tanstack/react-table";

const columns: ColumnDef<IBill>[] = [
  {
    accessorKey: "id",
    header: "ID",
  },
  {
    accessorKey: "bill",
    header: "Bill",
  },
  {
    accessorKey: "supporters",
    header: "Supporters",
  },
  {
    accessorKey: "opposers",
    header: "Opposers",
  },
  {
    accessorKey: "primarySponsor",
    header: "Primary sponsor",
  },
];

interface BillTableProps {
  data: IBill[];
}

export function BillTable({ data }: BillTableProps) {
  return <DataTable columns={columns} data={data} />;
}
