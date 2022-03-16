import React from "react";
import DropZoneInput from "./DropZoneInput";

function DropZone() {
  return (
    <div className="flex flex-col items-center justify-center">
      <h1 className="my-4 text-3xl font-medium">Isro</h1>
      <div className="flex flex-col items-center justify-center bg-gray-800 shadow-xl w-96 rounded-xl">
        <DropZoneInput />
      </div>
    </div>
  );
}

export default DropZone;
