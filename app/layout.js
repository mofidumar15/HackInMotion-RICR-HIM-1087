export const metadata = {
  title: "CureDrug",
  description:
    "Smart Medicine Safety Assistant"
};

export default function RootLayout({
  children
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
