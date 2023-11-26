import { useState } from "react";

function Homepage({ showHomepage }: {showHomepage: () => void}) {
  const [selectedFile, setSelectedFile] = useState<File>();
  const [fileDownload, setFileDownload] = useState<string | undefined>();
  const [errorMsg, setErrorMsg] = useState<string | undefined>();
  const [uploadEffect, setUploadEffect] = useState(false);

  const handleUpload = (e: React.FormEvent) => {
    setUploadEffect(true);
    uploadVocab(e);
  }

  const uploadVocab = async(e: React.FormEvent) => {
    e.preventDefault();

    if (!selectedFile) {
      setErrorMsg("no file provided");
      return;
    }

    const data = new FormData();
    data.append("file", selectedFile, "vocab.db");

    fetch(import.meta.env.VITE_API, { 
      method: 'POST',
      body: data,
    })
    .then(response => {
      if (!response.ok) {
        throw new Error("oops some server issue occured or you chose a wrong file!");
      }
      return response.blob();
    })
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      setFileDownload(url);
      setErrorMsg("");
    })
    .catch(error => {
      setErrorMsg(error.message);
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
          <button 
            className={`${uploadEffect && "animate-wiggle-more animate-ease-out animate-thrice"} text-purple-700 hover:text-purple-800 active:animate-pulse`}
            type="submit" 
            onClick={handleUpload} 
            onAnimationEnd={() => setUploadEffect(false)}>
            Upload
          </button>
        </form>
        <span className="text-2xl">Don't know how to get it?</span>
        <span className="text-2xl">Visit&nbsp;
          <button onClick={showHomepage}>
            <span className="text-purple-700 underline hover:text-purple-800">Instructions</span>
          </button>
        </span>
        {fileDownload && <a className="text-purple-700 font-semibold my-3 hover:text-purple-800" href={fileDownload} download="words.csv">Download</a>}
      </div>
    </>
  )
}

export default Homepage;