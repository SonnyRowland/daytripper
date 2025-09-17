import { useQuery } from "@tanstack/react-query";
import { useSearchParams } from "react-router";
import axios from "axios";
import { Icon } from "@iconify/react";

import type { PubType } from "@/types";
import { Card, CardContent } from "@/components/ui/card";
import { Header } from "@/components/Header";
import { Spinner } from "@/components/ui/shadcn-io/spinner";
import ImageCard from "@/components/ui/image-card";
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
        {data.map((pub, index) => {
          return (
            <Card className="w-[80%]" key={index}>
              <CardContent>
                <div className="flex flex-col gap-[16px] w-full">
                  <ImageCard
                    className="w-[200px] self-center"
                    caption={pub.name}
                    imageUrl={`/assets/images/${index + 1}.jpg`}
                  />
                  <div className="flex w-full justify-between">
                    <div className="flex flex-col justify-center">
                      Open until {`2${Math.floor(Math.random() * 3) + 1}:00`}
                    </div>
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
