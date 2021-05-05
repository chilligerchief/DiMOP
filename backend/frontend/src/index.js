import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { Route, Router, Switch } from "react-router-dom";
import { APIProvider } from "./APIContext";
import { PrivateRoute } from "./components/PrivateRoute/PrivateRoute";
import { UserProvider } from "./contexts_OUTDATED/UserContext_OUTDATED";
import { history } from "./helpers/history";
import "./index.css";
import { authenticationService } from "./services/authenticationService";
import * as serviceWorker from "./serviceWorker";
import ConstructionWrapper from "./views/Construction_OUTDATED/ConstructionWrapper_OUTDATED";
import { Home } from "./views/Home/Home";
import { Login } from "./views/Login/Login";
import MainWrapper from "./views/Main/MainWrapper";
import Settings from "./views/Settings/Settings";

// using router and debugging API Context in all sources
const styleLink = document.createElement("link");
styleLink.rel = "stylesheet";
styleLink.href =
  "https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.min.css";
document.head.appendChild(styleLink);

const App = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    authenticationService.currentUser.subscribe((x) =>
      setUser({ currentUser: x })
    );
  }, []);

  const logout = () => {
    authenticationService.logout();
    history.push("/login");
  };

  return (
    <Router history={history}>
      <APIProvider>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <PrivateRoute path="/home" component={Home}></PrivateRoute>
          {/*
          <PrivateRoute
            path="/construction"
            component={ConstructionWrapper}
          ></PrivateRoute>
          <PrivateRoute path="/settings" component={Settings}></PrivateRoute>
          */}
          <PrivateRoute path="/main" component={MainWrapper}></PrivateRoute>
          <Route path="/login" component={Login}></Route>
        </Switch>
      </APIProvider>
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
