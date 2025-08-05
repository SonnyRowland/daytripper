import { useQuery } from "@tanstack/react-query";
import { useLocation } from "react-router";
import axios from "axios";
import { Icon } from "@iconify/react";

import type { PubType } from "@/types";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Header } from "@/components/Header";

export const Crawl = () => {
  const location = useLocation();
  const start = location.state?.start;
  const end = location.state?.end;

  const { error, isPending, data } = useQuery<PubType[]>({
    queryKey: ["crawl"],
    queryFn: async () => {
      const res = await axios.get(
        `http://localhost:8000/places/walk/postcode/${start}/${end}/6`
      );

      return res.data;
    },
  });

  if (isPending) {
    return (
      <div className="flex flex-col w-dvw h-dvh justify-center">
        <div className="flex flex-col justify-start items-center">
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (error) {
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
