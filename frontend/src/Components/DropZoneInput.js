import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";

const DropZoneInput = () => {
  const onDrop = useCallback((acceptedFiles) => {
    console.log(acceptedFiles);
  }, []);

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    multiple: false,
  });
  return (
    <div>
      <div
        {...getRootProps()}
        className="h-80 w-full flex justify-center items-center text-white"
      >
        <input {...getInputProps()} />
        <p>Drag and drop files</p>
      </div>
    </div>
  );
};

export default DropZoneInput;
