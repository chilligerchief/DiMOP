import Avatar from "@material-ui/core/Avatar";
import Box from "@material-ui/core/Box";
import Button from "@material-ui/core/Button";
import Container from "@material-ui/core/Container";
import CssBaseline from "@material-ui/core/CssBaseline";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import React, { useState } from "react";
import { useHistory } from "react-router";
import { authenticationService } from "../../services/authenticationService";
import colors from "../../variables/colors";

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      {new Date().getFullYear()}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export const Login = () => {
  const classes = useStyles();

  const history = useHistory();

  const [orga, setOrga] = useState("");
  const [password, setPassword] = useState("");
  const [showErrorText, setShowErrorText] = useState(false);

  const validateLogin = () => {
    const dummyLogins = [
      {
        orga: "Uni",
        password: "1234",
      },
      {
        orga: "SKZ",
        password: "1234",
      },
    ];

    authenticationService.login(orga, password).then(
      (user) => {
        //login valid
        history.push("/");
      },
      (error) => {
        //login invalid
        // TODO: show that input is wrong / change color to red
        console.log("ERROR");
      }
    );

    //! check orga and password
    // if (validation successful) {

    // console.log(orga, password);
    // if (
    //   dummyLogins.filter((e) => {
    //     return orga.toLowerCase() == e.orga.toLowerCase() && password == e.password;
    //   }).length > 0
    // ) {
    //   localStorage.setItem("auth", true);
    //   localStorage.setItem("orga", orga);
    //   login(orga);
    //   history.push("/home");
    // } else {
    //   setShowErrorText(true);
    // }

    // } else {
    //  handle wrong login
    // }
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5" align="center">
          Bitte melden Sie sich mit Ihrem Organisationskonto an
        </Typography>
        <form className={classes.form} noValidate>
          <TextField
            error={showErrorText}
            helperText={
              showErrorText ? "Bitte überprüfen Sie ihre Eingabe" : ""
            }
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Organisation"
            name="orga"
            // autoComplete="email"
            autoFocus
            onChange={(e) => setOrga(e.target.value)}
            value={orga}
          />
          <TextField
            error={showErrorText}
            helperText={
              showErrorText ? "Bitte überprüfen Sie ihre Eingabe" : ""
            }
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Passwort"
            type="password"
            id="password"
            // autoComplete="current-password"
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          />

          <Button
            // type="submit"
            fullWidth
            variant="contained"
            className={classes.submit}
            onClick={() => validateLogin()}
            style={{
              backgroundColor: colors.primaryGreen,
              color: colors.lightGrey,
            }}
          >
            Anmelden
          </Button>
        </form>
      </div>
      <p>testaccounts</p>
      <table>
        <tr>
          <td>uni</td>
          <td>1234</td>
        </tr>
        <tr>
          <td>skz</td>
          <td>1234</td>
        </tr>
      </table>
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
  );
};
