import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/login';
import LogoutPage from './pages/logout';
import RegisterPage from './pages/register';
import DashboardPage from './pages/dashboard';

function App() {
  return (
    
    <div>
      <h1>TESTING</h1>
      <BrowserRouter>
        <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/logout" element={<LogoutPage/>} />
            <Route path="/register" element={<RegisterPage/>} />
            <Route path="/dashboard" element={<DashboardPage/>} />
          </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
