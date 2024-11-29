"use client";

import { useState } from "react";
import axios from "axios";

export default function VideoUpload() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState<any>(null);

  const handleUpload = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/videos/upload_youtube_link/",
        { url }
      );
      setResult(response.data);
    } catch (error) {
      console.error("Error processing video:", error);
      alert("Processing failed");
    }
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6 mb-4">
      <h2 className="text-xl font-semibold mb-2">Process YouTube Video</h2>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter YouTube video URL"
        className="border border-gray-300 rounded-md p-2 w-full mb-4"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white rounded-md px-4 py-2 hover:bg-blue-700 transition"
      >
        Process Video
      </button>
      {result && (
        <div className="mt-4">
          <h3 className="font-semibold">Result:</h3>
          <p>Answer: {result.answer}</p>
          <p>Timestamp: {result.timestamp} seconds</p>
        </div>
      )}
    </div>
  );
}
