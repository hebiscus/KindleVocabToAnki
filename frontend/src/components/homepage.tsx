import { useState } from "react";

function Homepage() {
  const [selectedFile, setSelectedFile] = useState<File>();

  const uploadVocab = async(e: React.FormEvent) => {
    e.preventDefault();

    const data = new FormData();
    data.append("file", selectedFile, "vocab.db");

    fetch("http://localhost:8000/upload", { 
      method: 'POST',
      body: data,
    })
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
  }

  return (
    <>
      <form >
        <input type="file" onChange={(e) => setSelectedFile(e.target.files[0])}/>
        <button onClick={uploadVocab}>yes</button>
      </form>
    </>
  )
}

export default Homepage;