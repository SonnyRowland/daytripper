import axios from "axios";
import { useQuery } from "@tanstack/react-query";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

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

  return (
    <Card className="w-full max-w-sm">
      <CardHeader>
        <CardTitle>Pub number 1984</CardTitle>
        <CardDescription>{data?.name}</CardDescription>
      </CardHeader>
      <CardContent>Hello</CardContent>
      <CardFooter>Hello</CardFooter>
    </Card>
  );
}

export default App;
