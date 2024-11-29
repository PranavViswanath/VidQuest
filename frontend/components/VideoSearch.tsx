import { useState } from "react";
import axios from "axios";

export default function VideoSearch() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<any>(null);

  const handleSearch = async () => {
    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/api/videos/1/search/`,
        { query }
      );
      setResult(response.data);
    } catch (error) {
      console.error("Error searching video:", error);
      alert("Search failed");
    }
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-2">Search Video</h2>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter search query"
        className="border border-gray-300 rounded-md p-2 w-full mb-4"
      />
      <button
        onClick={handleSearch}
        className="bg-blue-600 text-white rounded-md px-4 py-2 hover:bg-blue-700 transition"
      >
        Search
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
