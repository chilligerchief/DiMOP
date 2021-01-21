import React from "react";

//Components
import { MainProvider } from "./MainContext";
import Main from "./Main";

// import provider for wrapping and state management in construction Info
function MainWrapper() {
  return (
    <MainProvider>
      <div>
        <Main></Main>
      </div>
    </MainProvider>
  );
}

export default MainWrapper;