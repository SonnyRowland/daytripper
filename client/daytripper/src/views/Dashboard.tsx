import { useState } from "react";
import { Header } from "@/components/Header";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";

export const Dashboard = () => {
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const handleAddPub = () => {
    // TODO: add API call here

    setIsDialogOpen(false);
  };

  return (
    <Header>
      <div className="flex flex-col h-full items-center gap-[16px] p-[16px]">
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <form>
            <DialogTrigger asChild>
              <Button>Add Pub</Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-[425px]">
              <DialogHeader>
                <DialogTitle>Add Pub</DialogTitle>
                <DialogDescription>
                  Add details of a new pub to be added to the database
                </DialogDescription>
              </DialogHeader>
              <div className="grid gap-4">
                <div className="grid gap-3">
                  <Label htmlFor="name-1">Name</Label>
                  <Input
                    name="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    autoComplete="off"
                  />
                </div>
                <div className="grid gap-3">
                  <Label htmlFor="address-1">Address</Label>
                  <Input
                    name="address"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    autoComplete="off"
                  />
                </div>
              </div>
              <DialogFooter>
                <DialogClose asChild>
                  <Button variant="neutral">Cancel</Button>
                </DialogClose>
                <Button type="submit" onClick={() => handleAddPub()}>
                  Save changes
                </Button>
              </DialogFooter>
            </DialogContent>
          </form>
        </Dialog>
      </div>
    </Header>
  );
};
