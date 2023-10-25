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
      <form>
        <input type="file" onChange={(e) => setSelectedFile(e.target!.files?.[0])}/>
        <button type="submit" onClick={uploadVocab}>Upload</button>
      </form>
      {fileDownload && <a href={fileDownload} download="words.csv">Download</a>}
    </>
  )
}

export default Homepage;