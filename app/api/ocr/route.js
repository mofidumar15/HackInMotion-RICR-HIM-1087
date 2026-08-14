import { NextResponse } from "next/server";

export async function POST() {
  return NextResponse.json({
    success: true,
    text:
      "Paracetamol 500mg\nAmoxicillin 250mg"
  });
}
