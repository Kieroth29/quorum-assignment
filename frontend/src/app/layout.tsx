import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Legislation data",
  description: "Informations about legislators and bills.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
