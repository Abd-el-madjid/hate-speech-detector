import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import MainLayout from "./components/Layout"; // Update to your layout component
import ModelStatistics from "./pages/Home"; // Home Page Content
import Report from "./pages/Report"; // Report Page Content (with Tabs)

function App() {
  return (
    <Router>
      <MainLayout>
        <Routes>
          <Route path="/" element={<ModelStatistics />} />
          <Route path="/report" element={<Report />} />
        </Routes>
      </MainLayout>
    </Router>
  );
}

export default App;
