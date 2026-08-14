"use client";

export default function Navbar() {
  return (
    <nav className="w-full border-b bg-white">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold">
          CureDrug
        </h1>

        <div className="flex gap-6">
          <a href="#">Home</a>
          <a href="#">Drug Search</a>
          <a href="#">Interactions</a>
          <a href="#">OCR</a>
        </div>
      </div>
    </nav>
  );
}
