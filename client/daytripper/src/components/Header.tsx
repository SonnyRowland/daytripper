export const Header = ({ children }: { children: React.ReactNode }) => {
  return (
    <>
      <div className="flex justify-center items-center w-full h-[120px] ">
        <img src="/assets/crawla_logo.png" className="h-full" />
      </div>
      {children}
    </>
  );
};
