import { useQuery } from "@tanstack/react-query";
import { useSearchParams } from "react-router";
import axios from "axios";
import { Icon } from "@iconify/react";

import type { PubType } from "@/types";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Header } from "@/components/Header";
import { Spinner } from "@/components/ui/shadcn-io/spinner";
import { ErrorFetchingData } from "./ErrorFetchingData";

export const Crawl = () => {
  const [searchParams] = useSearchParams();

  const { error, isPending, data } = useQuery<PubType[]>({
    queryKey: ["crawl"],
    queryFn: async () => {
      const res = await axios.get(
        `http://localhost:8000/places/crawl/${searchParams.get(
          "lat"
        )}/${searchParams.get("lng")}/${searchParams.get(
          "end"
        )}/${searchParams.get("length")}`
      );

      return res.data;
    },
  });

  if (isPending) {
    return (
      <div className="flex flex-col w-dvw h-dvh justify-center">
        <div className="flex flex-col justify-start items-center">
          <Spinner />
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col w-dvw h-dvh justify-center items-center">
        <ErrorFetchingData />
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
