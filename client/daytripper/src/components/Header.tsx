import { useEffect, useState } from "react";
import { Icon } from "@iconify/react";
import { useNavigate, useLocation } from "react-router";

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuGroup,
  DropdownMenuSeparator,
} from "../components/ui/dropdown-menu";
import { Button } from "./ui/button";

export const Header = ({ children }: { children: React.ReactNode }) => {
  const navigate = useNavigate();
  const routerLocation = useLocation();

  const [isOnCrawlPage, setIsOnCrawlPage] = useState<boolean>(false);

  useEffect(() => {
    setIsOnCrawlPage(routerLocation.pathname == "/crawl");
  }, [routerLocation.pathname]);

  const copyToClipboard = async () => {
    await navigator.clipboard.writeText(location.href);
  };

  return (
    <>
      <div className="flex items-center w-full h-[120px] p-[52px]">
        <div className="flex-1 justify-start">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant={"noShadow"}>
                <Icon icon="line-md:menu" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-30">
              <DropdownMenuGroup>
                <DropdownMenuItem onClick={() => navigate("/location")}>
                  New Crawl
                </DropdownMenuItem>
                <DropdownMenuItem onClick={() => navigate("/dashboard")}>
                  Dashboard
                </DropdownMenuItem>
                {isOnCrawlPage && (
                  <>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem onClick={copyToClipboard}>
                      Copy link
                    </DropdownMenuItem>
                  </>
                )}
              </DropdownMenuGroup>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
        <div className="flex h-[120px]">
          <img src="/assets/crawla_logo.png" className="h-full" />
        </div>
        <div className="flex-1" />
      </div>
      {children}
    </>
  );
};
