import { Link } from "react-router";
import { Icon } from "@iconify/react";

import { Button } from "@/components/ui/button";

export const LandingPage = () => {
  return (
    <div className="flex flex-col w-dvw h-dvh justify-center">
      <div className="flex flex-col justify-start items-center">
        <img src="/assets/crawla_logo.png" width="240px" />
        <Link to="/location">
          <Button className="w-[200px]">
            Let's crawl
            <Icon icon="line-md:arrow-small-right" height="40px" />
          </Button>
        </Link>
      </div>
    </div>
  );
};
