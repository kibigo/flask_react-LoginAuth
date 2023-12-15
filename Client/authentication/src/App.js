import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import LandingPage from './Components/LandingPage';
import Login from './Components/Login';

function App() {

  return(
    <BrowserRouter>

      <Routes>

        <Route path='/' element={<LandingPage/>}/>
        <Route path='/login' element = {<Login/>}/>

      </Routes>
      
    </BrowserRouter>
  )
}
export default App;
