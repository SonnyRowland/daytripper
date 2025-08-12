import { useQuery } from "@tanstack/react-query";
import { useLocation } from "react-router";
import axios from "axios";
import { Icon } from "@iconify/react";

import type { PubType } from "@/types";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Header } from "@/components/Header";

export const Crawl = () => {
  const location = useLocation();
  const start_lat = location.state?.latitude;
  const start_lng = location.state?.longitude;
  const end = location.state?.end;
  const length = location.state?.length || 5;

  const {
    error: externalError,
    isPending: externalIsPending,
    data: externalData,
  } = useQuery({
    queryKey: ["locationService"],
    queryFn: async () => {
      const res = await axios.get(
        `https://nominatim.openstreetmap.org/search?q=${end},london&format=json`
      );

      return { end_lat: res.data[0].lat, end_lng: res.data[0].lon };
    },
  });

  const { error, isPending, data } = useQuery<PubType[]>({
    queryKey: ["crawl"],
    queryFn: async () => {
      const res = await axios.get(
        `http://localhost:8000/places/crawl/${start_lat}/${start_lng}/${externalData?.end_lat}/${externalData?.end_lng}/${length}`
      );

      return res.data;
    },
    enabled: !!externalData,
  });

  if (isPending || externalIsPending) {
    return (
      <div className="flex flex-col w-dvw h-dvh justify-center">
        <div className="flex flex-col justify-start items-center">
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (error || externalError) {
    return (
      <div className="flex flex-col w-full h-full justify-center items-center">
        <p className="text-center">
          We had a problem fetching your data. Please try again later
        </p>
      </div>
    );
  }

  return (
    <Header>
      <div className="flex flex-col h-full items-center gap-[16px] p-[16px]">
        {data.map((pub) => {
          return (
            <Card className="w-[80%]">
              <CardHeader>
                <CardTitle>{pub.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-col gap-[16px]">
                  {pub.address}

                  <div className="flex w-full justify-end">
                    <a
                      href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
                        `${pub.name} ${pub.postcode}`
                      )}`}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <Icon icon="line-md:map-marker" height="40px" />
                    </a>
                  </div>
                </div>
              </CardContent>
            </Card>
          );
        })}
      </div>
    </Header>
  );
};
