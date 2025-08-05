import { Route, Routes } from "react-router";

import { LandingPage } from "./views/LandingPage";
import { Location } from "./views/Location";
import { Crawl } from "./views/Crawl";

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/location" element={<Location />} />
      <Route path="/crawl" element={<Crawl />} />
    </Routes>
  );
};

export default App;
