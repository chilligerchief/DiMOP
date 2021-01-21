import React from "react";

import { ConstructionProvider } from "./ConstructionContext";
import Construction from "./Construction";

// import provider for wrapping and state management in construction Info
function ConstructionWrapper() {
  return (
    <ConstructionProvider>
      <div>
        <Construction></Construction>
      </div>
    </ConstructionProvider>
  );
}

export default ConstructionWrapper;
