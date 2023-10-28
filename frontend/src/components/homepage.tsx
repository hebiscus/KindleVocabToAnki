import { useState } from "react";

function Homepage() {
  const [selectedFile, setSelectedFile] = useState<File>();
  const [fileDownload, setFileDownload] = useState<string | undefined>();
  const [errorMsg, setErrorMsg] = useState();

  const uploadVocab = async(e: React.FormEvent) => {
    e.preventDefault();

    const data = new FormData();
    if (!selectedFile) return;
    data.append("file", selectedFile, "vocab.db");

    fetch(import.meta.env.VITE_API, { 
      method: 'POST',
      body: data,
    })
      .then(response => {
        if (!response.ok) {
          throw new Error("oops some server issue occured or you chose a wrong file!");
        }
        return response.blob()
      })
      .then(blob => {
        const url = window.URL.createObjectURL(blob);
        setFileDownload(url)
        })
      .catch(error => {
        setErrorMsg(error.message)
      });
  }

  return (
    <>
      <div className="absolute top-1/2 -translate-y-2/3 max-w-lg self-center text-3xl flex flex-col items-center gap-3">
        <span>Upload your vocab.db file:</span>
        {errorMsg && <span className="text-red-700 text-2xl text-center">{errorMsg}</span>}
        <form className="flex w-full justify-center gap-3">
          <label className="px-1.5 py-3.5 rounded-xl shadow-md shadow-purple-300 border-black border border-solid hover:cursor-pointer hover:scale-110" htmlFor="dbFile">Choose a file</label>
          <input className="hidden" type="file" id="dbFile" onChange={(e) => setSelectedFile(e.target!.files?.[0])}/>
          <button className="text-purple-700 hover:text-purple-800" type="submit" onClick={uploadVocab}>Upload</button>
        </form>
        <span className="text-2xl">Don't know how to get it?</span>
        <span className="text-2xl">Visit <a className="text-purple-700 underline hover:text-purple-800" href="">Instructions</a></span>
        {fileDownload && <a className="text-purple-700 font-semibold my-3 hover:text-purple-800" href={fileDownload} download="words.csv">Download</a>}
      </div>
    </>
  )
}

export default Homepage;