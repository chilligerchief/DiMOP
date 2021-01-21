import "./index.css";

import * as serviceWorker from "./serviceWorker";

import React, { useContext } from "react";
import { Redirect, Route, Router, Switch, useHistory } from "react-router-dom";
import { UserContext, UserProvider } from "./contexts/UserContext";

import { APIProvider } from "./APIContext";
import ConstructionWrapper from "./views/Construction/ConstructionWrapper";
import { Home } from "./views/Home/Home";
import { Login } from "./views/Login/Login";
import MainWrapper from "./views/Main/MainWrapper";
import ReactDOM from "react-dom";
import Settings from "./views/Settings/Settings";
import { createBrowserHistory } from "history";

const hist = createBrowserHistory();

// using router and debugging API Context in all sources
const styleLink = document.createElement("link");
styleLink.rel = "stylesheet";
styleLink.href = "https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.min.css";
document.head.appendChild(styleLink);

const App = () => {
  const { user } = useContext(UserContext);

  return user.auth ? (
    <Router history={hist}>
      <APIProvider>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route path="/home" component={Home}></Route>
          <Route path="/construction" component={ConstructionWrapper}></Route>
          <Route path="/settings" component={Settings}></Route>
          <Route path="/main" component={MainWrapper}></Route>
          <Route path="/login" component={Login}></Route>
        </Switch>
      </APIProvider>
    </Router>
  ) : (
    <Router history={hist}>
      <Switch>
        <Route exact path="/login" component={Login}></Route>
        <Route component={Home} />
      </Switch>
    </Router>
  );
};

ReactDOM.render(
  <UserProvider>
    <App />
  </UserProvider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
