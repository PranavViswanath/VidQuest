import VideoUpload from "../components/VideoUpload";
import VideoSearch from "../components/VideoSearch";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <header className="bg-blue-600 text-white w-full p-6 text-center mb-8">
        <h1 className="text-3xl font-bold">Welcome to VideoQuest</h1>
        <p className="mt-2 text-lg">Search for answers within YouTube videos</p>
      </header>

      <main className="flex flex-col items-center w-full max-w-2xl px-4">
        <VideoUpload />
        <VideoSearch />
      </main>

      <footer className="mt-auto p-4 text-center text-gray-600">
        <p>Powered by Next.js and Django</p>
      </footer>
    </div>
  );
}
