import axios from "axios";
import { useQuery } from "@tanstack/react-query";

type PubType = {
  id: number;
  name: string;
  address: string;
  postcode: string;
  lat: number;
  lng: number;
};

function App() {
  const { data } = useQuery<PubType>({
    queryKey: ["pubs"],
    queryFn: async () => {
      const res = await axios.get("http://localhost:8000/places/1984");

      return res.data;
    },
  });

  return <p>Pub number 1984: {JSON.stringify(data?.name)}</p>;
}

export default App;
