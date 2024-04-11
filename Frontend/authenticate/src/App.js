import { BrowserRouter as Routes, Route } from 'react-router-dom';
import LoginPage from './pages/login';
import LogoutPage from './pages/logout';
import RegisterPage from './pages/register';

function App() {
  return (
    
    <div>
      <h1>TESTING</h1>
      <Routes>
          <Route path="/login" element={<LoginPage />}/>
          <Route path="logout" element={<LogoutPage/>}/>
          <Route path="register" element={<RegisterPage/>}/>
      </Routes>
    </div>
  );
}

export default App;
