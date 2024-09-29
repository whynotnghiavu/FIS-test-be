import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import HomePage from "./components/HomePage";

import OtpPage from "./components/OtpPage";

function App() {
  return (
    <BrowserRouter>
      {/* <LayoutHeader /> */}
      <Routes>
        <Route path="/" element={<HomePage />}></Route>
        {/* <Route path="/register" element={<RegisterPage />}></Route> */}
        {/* <Route path="/login" element={<LoginPage />}></Route> */}
        <Route path="/otp" element={<OtpPage />}></Route>
        {/* <Route path="/setting" element={<SettingPage />}></Route> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
