import { useState } from "react";

function Homepage() {
  const [selectedFile, setSelectedFile] = useState<File>();
  const [fileDownload, setFileDownload] = useState<string | undefined>();

  const uploadVocab = async(e: React.FormEvent) => {
    e.preventDefault();

    const data = new FormData();
    if (!selectedFile) return;
    data.append("file", selectedFile, "vocab.db");

    fetch(import.meta.env.VITE_API, { 
      method: 'POST',
      body: data,
    })
      .then(response => response.blob())
      .then(blob => {
        const url = window.URL.createObjectURL(blob);
        setFileDownload(url)
        })
      .catch(error => console.log('error', error));
  }

  return (
    <>
      <div className="absolute top-1/2 -translate-y-2/3 max-w-lg self-center text-3xl flex flex-col items-center gap-3">
        <span>Upload your vocab.db file:</span>
        <form className="flex w-full justify-around">
          <label className="px-1.5 py-3.5 rounded-xl shadow-md shadow-purple-300 border-black border border-solid hover:cursor-pointer" htmlFor="dbFile">Choose a file</label>
          <input className="hidden" type="file" id="dbFile" onChange={(e) => setSelectedFile(e.target!.files?.[0])}/>
          <button className="" type="submit" onClick={uploadVocab}>Upload</button>
        </form>
        <span className="text-2xl">Don't know how to get it?</span>
        <span className="text-2xl">Visit <a className="text-purple-700 underline" href="">Instructions</a></span>
      </div>
      {fileDownload && <a href={fileDownload} download="words.csv">Download</a>}
    </>
  )
}

export default Homepage;