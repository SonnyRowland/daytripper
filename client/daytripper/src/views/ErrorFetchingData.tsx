import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Icon } from "@iconify/react";
import { Link } from "react-router";

export const ErrorFetchingData = () => {
  return (
    <>
      <img src="/assets/crawla_logo.png" width="240px" />
      <Card className="w-[80%]">
        <CardContent>
          <div className="flex flex-col h-full items-center text-center gap-[12px]">
            <Icon icon="line-md:alert-circle" height="40px" />
            <p>We had trouble fetching your data. Please try again later!</p>
            <Link to="/">
              <Button className="w-[200px]">Go home</Button>
            </Link>
          </div>
        </CardContent>
      </Card>
    </>
  );
};
