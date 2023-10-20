import { useState } from 'react'
import './App.css'
import Footer from './components/footer'
import Navbar from './components/navbar'
import Homepage from './components/homepage'
import InfoPage from './components/info'

function App() {
  const [homepage, setHomepage] = useState(true)
  
  const showHomepage = () => setHomepage(!homepage)

  return (
    <>
      <Navbar showHomepage={showHomepage} homepage={homepage}/>
      {homepage ? <Homepage /> : <InfoPage />}
      <Footer />
    </>
  )
}

export default App
