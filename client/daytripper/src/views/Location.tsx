import { useState } from "react";
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

export const Location = () => {
  const navigate = useNavigate();

  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");

  const [length, setLength] = useState<string>("");

  const handleClick = () => {
    navigate("/crawl", { state: { start, end, length } });
  };

  return (
    <div className="flex flex-col w-dvw h-dvh justify-center">
      <div className="flex flex-col justify-start items-center">
        <div className="flex flex-col gap-[12px]">
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
          <Input
            className="w-[200px]"
            placeholder="Start postcode"
            onChange={(e) => setStart(e.target.value)}
          />
          <Input
            className="w-[200px]"
            placeholder="End postcode"
            onChange={(e) => setEnd(e.target.value)}
          />
          <Button onClick={() => handleClick()}>Crawl</Button>
        </div>
      </div>
    </div>
  );
};
