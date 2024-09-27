import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import LayoutHeader from "./components/LayoutHeader";
import HomePage from "./components/HomePage";

import RegisterPage from "./components/RegisterPage";
import LoginPage from "./components/LoginPage";

import OtpPage from "./components/OtpPage";

import SettingPage from "./components/SettingPage";

function App() {
  return (
    <BrowserRouter>
      <LayoutHeader />
      <Routes> 
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/register" element={<RegisterPage />}></Route>
        <Route path="/login" element={<LoginPage />}></Route>
        <Route path="/otp" element={<OtpPage />}></Route>
        <Route path="/setting" element={<SettingPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
