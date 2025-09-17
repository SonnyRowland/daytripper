import { Route, Routes } from "react-router";

import { LandingPage } from "./views/LandingPage";
import { Location } from "./views/Location";
import { Crawl } from "./views/Crawl";
import { Dashboard } from "./views/Dashboard";

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/location" element={<Location />} />
      <Route path="/crawl" element={<Crawl />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  );
};

export default App;
