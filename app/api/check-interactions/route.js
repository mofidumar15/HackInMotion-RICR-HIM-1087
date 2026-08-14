import { NextResponse } from "next/server";

export async function POST(request) {
  try {
    const body = await request.json();

    const medicines =
      body.medicines || [];

    return NextResponse.json({
      success: true,
      medicines,
      interactionCount: 0,
      risk: "Low Risk",
      interactions: []
    });
  } catch (error) {
    return NextResponse.json(
      {
        success: false,
        error: error.message
      },
      {
        status: 500
      }
    );
  }
}
