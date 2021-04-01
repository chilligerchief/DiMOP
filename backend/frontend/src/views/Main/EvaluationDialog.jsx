import React from "react";
import { useContext, useState, useEffect } from "react";

//Components
import { MainContext } from "./MainContext.jsx";

//Material UI
import Button from "@material-ui/core/Button";
import { makeStyles } from "@material-ui/core/styles";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogTitle from "@material-ui/core/DialogTitle";
import HighlightOffIcon from "@material-ui/icons/HighlightOff";
import Grid from "@material-ui/core/Grid";
import Stepper from "@material-ui/core/Stepper";
import Step from "@material-ui/core/Step";
import StepLabel from "@material-ui/core/StepLabel";
import Typography from "@material-ui/core/Typography";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import {
  withStyles,
  MuiThemeProvider,
  createMuiTheme,
} from "@material-ui/core/styles";
import PlayCircleOutlineIcon from "@material-ui/icons/PlayCircleOutline";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";

// css theme
const useStyles = makeStyles((theme) => ({
  root: {
    "& > *": {
      margin: theme.spacing(1),
    },
  },
  buttons: {
    borderColor: "#005000",
    color: "#005000",
    textTransform: "none",
    margin: 20,
    height: 30,
    width: 120,
  },
  buttons2: {
    borderColor: "#005000",
    color: "#005000",
    textTransform: "none",
    margin: 20,
    height: 30,
    width: 120,
  },
  stepdiv: {
    height: 150,
    width: 400,
  },
}));

const muiTheme = createMuiTheme({
  overrides: {
    MuiStepIcon: {
      root: {
        color: "lightgrey",
        "&$active": {
          color: "grey",
        },
        "&$completed": {
          color: "#005000",
        },
      },
    },
  },
});

const GreenRadio = withStyles({
  root: {
    color: "#005000",
    "&$checked": {
      color: "#005000",
    },
  },
  checked: {},
})((props) => <Radio color="default" {...props} />);

const EvaluationDialog = () => {
  const classes = useStyles();

  const { evaluation_open, data_backend } = useContext(MainContext);

  const [dataBackend, setDataBackend] = data_backend;
  const [evaluationOpen, setEvaluationOpen] = evaluation_open;
  const [evaluationData, setEvaluationData] = useState(1.0);
  const [isDangerous, setIsDangerous] = useState(0);

  const initiateEvaluation = () => {
    const requestOptions = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        isDangerous,
        dataBackend
      }),
      redirect: "follow",
    };

    fetch("/evaluation", requestOptions)
      .then((res) => {
        return res.json();
      })
      .then((d) => {
        setEvaluationData(d);
      });
  };

  const handleChangeDangerous = (event) => {
    setIsDangerous(event.target.value);
  };

  function getSteps() {
    return ["", "", ""];
  }

  function getStepContent(step) {
    switch (step) {
      case 0:
        return (
          <div className={classes.stepdiv}>
            <Grid container item xs={12}>
              Bitte beantworten Sie die nachfolgende Frage zu Ihrem geplanten
              Produkt.{" "}
            </Grid>
          </div>
        );
      case 1:
        return (
          <div className={classes.stepdiv}>
            <Grid container item xs={12}>
              Enthält Ihr Produkt umwelt- oder gesundheitsgefährdende Stoffe?
            </Grid>
            <Grid container item xs={12}>
              <FormControl component="fieldset">
                <FormLabel component="legend"></FormLabel>
                <RadioGroup
                  aria-label="is-dangerous"
                  value={isDangerous}
                  onChange={handleChangeDangerous}
                >
                  <FormControlLabel
                    value="1"
                    control={<GreenRadio />}
                    label="Ja"
                  />
                  <FormControlLabel
                    value="0"
                    control={<GreenRadio />}
                    label="Nein"
                  />
                </RadioGroup>
              </FormControl>
            </Grid>
          </div>
        );
      case 2:
        return (
          <div className={classes.stepdiv}>
            <Grid container item xs={12}>
              <Button onClick={initiateEvaluation} className={classes.buttons2}>
                Send to backend
              </Button>
              <Card className={classes.root_card} variant="outlined">
              <CardContent>
                <Typography
                  className={classes.title}
                  color="textSecondary"
                  gutterBottom
                  align="center"
                >
                  Recyclingwert:
                </Typography>
                <Typography variant="h5" component="h2" align="center">
                  {evaluationData}
                </Typography>
              </CardContent>
            </Card>



            </Grid>
          </div>
        );
      default:
        return (
          <div className={classes.stepdiv}>
            <Grid container item xs={12}></Grid>
          </div>
        );
    }
  }

  const handleClickOpen = () => {
    setEvaluationOpen(true);
  };

  const handleClose = () => {
    setEvaluationOpen(false);
  };

  const [activeStep, setActiveStep] = useState(0);
  const steps = getSteps();

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleReset = () => {
    setActiveStep(1);
  };

  return (
    <div>
      <Button className={classes.buttons} onClick={handleClickOpen}>
        <PlayCircleOutlineIcon
          style={{ marginRight: 5 }}
        ></PlayCircleOutlineIcon>
        Bewerten
      </Button>
      <Dialog
        open={evaluationOpen}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogActions>
          <HighlightOffIcon
            style={{ color: "#005000" }}
            onClick={handleClose}
          ></HighlightOffIcon>
        </DialogActions>
        <DialogTitle id="form-dialog-title">Stückliste bewerten</DialogTitle>

        <DialogContent>
          <MuiThemeProvider theme={muiTheme}>
            <div>
              <Stepper activeStep={activeStep}>
                {steps.map((label, index) => {
                  const stepProps = {};
                  const labelProps = {};

                  return (
                    <Step key={label} {...stepProps}>
                      <StepLabel {...labelProps}>{label}</StepLabel>
                    </Step>
                  );
                })}
              </Stepper>
              <div>
                {activeStep === steps.length ? (
                  <div>
                    <Typography className={classes.instructions}>
                      Vielen Dank für Ihre Eingaben. Sie können Ihre Ergebnisse
                      jetzt speichern, indem Sie die Bewertung "Abschließen".
                    </Typography>

                    <Grid container item xs={12} justify="center">
                      <Button
                        onClick={handleReset}
                        className={classes.buttons2}
                      >
                        Eingaben ändern
                      </Button>
                      <Button
                        onClick={() => {
                          handleReset();
                          handleClose();
                        }}
                        className={classes.buttons2}
                      >
                        Abschließen
                      </Button>
                    </Grid>
                  </div>
                ) : (
                  <div>
                    <Typography className={classes.instructions}>
                      {getStepContent(activeStep)}
                    </Typography>
                    <div>
                      <Grid container item xs={12} justify="center">
                        <Button
                          disabled={activeStep === 0}
                          onClick={handleBack}
                          className={classes.buttons2}
                        >
                          Zurück
                        </Button>
                        <Button
                          onClick={handleNext}
                          className={classes.buttons2}
                        >
                          Weiter
                        </Button>
                      </Grid>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </MuiThemeProvider>
        </DialogContent>
      </Dialog>
    </div>
  );
};
export default EvaluationDialog;
