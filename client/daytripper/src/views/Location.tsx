import { useEffect, useState } from "react";
import { useNavigate } from "react-router";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

type CoordsType = {
  latitude: number;
  longitude: number;
};

export const Location = () => {
  const navigate = useNavigate();
  const [userLocation, setUserLocation] = useState<CoordsType | null>(null);

  const [length, setLength] = useState<string>("");
  const [end, setEnd] = useState<string>("");

  const isFormEmpty = !end.trim();

  const handleClick = () => {
    navigate(
      `/crawl?lat=${userLocation?.latitude}&lng=${
        userLocation?.longitude
      }&end=${end}&length=${length || 5}`
    );
  };

  const getUserLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setUserLocation({ latitude, longitude });
        },
        (error) => {
          // TODO: Make UI nice in this instance
          console.error(`Error getting client location: ${error}`);
        }
      );
    } else {
      // TODO: Make UI nice in this instance
      console.error("This browser does not support geolocation");
    }
  };

  useEffect(() => {
    getUserLocation();
  }, []);

  return (
    <div className="flex flex-col w-dvw h-dvh justify-center">
      <div className="flex flex-col justify-start items-center">
        <img src="/assets/crawla_logo.png" width="240px" />
        <div className="flex flex-col gap-[12px]">
          <Input
            className="w-[200px]"
            placeholder="Enter destination"
            onChange={(e) => {
              setEnd(e.target.value);
            }}
            value={end}
          />
          <Select onValueChange={(value) => setLength(value)} value={length}>
            <SelectTrigger className="w-[200px]">
              <SelectValue placeholder="Number of pubs" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                {Array.from({ length: 10 }, (_, i) => i + 3).map(
                  (value, index) => (
                    <SelectItem key={index} value={value.toString()}>
                      {value}
                    </SelectItem>
                  )
                )}
              </SelectGroup>
            </SelectContent>
          </Select>
          <form
            className="flex flex-col gap-[12px]"
            onSubmit={(e) => {
              e.preventDefault();
              handleClick();
            }}
          >
            <Button type="submit" disabled={isFormEmpty}>
              Crawl
            </Button>
          </form>
        </div>
      </div>
    </div>
  );
};
