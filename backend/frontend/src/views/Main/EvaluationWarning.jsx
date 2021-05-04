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
import Typography from "@material-ui/core/Typography";
import PlayCircleOutlineIcon from "@material-ui/icons/PlayCircleOutline";

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
    height: 60,
    width: 140,
  },
}));


const EvaluationWarningDialog = () => {
  const classes = useStyles();

  const { evaluation_warning_open} = useContext(MainContext);
  const [evaluationWarningOpen, setEvaluationWarningOpen] = evaluation_warning_open;

  const handleClickOpen = () => {
    setEvaluationWarningOpen(true);
  };

  const handleClose = () => {
    setEvaluationWarningOpen(false);
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
        open={evaluationWarningOpen}
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
            <div>
            <Grid container item xs={12} justify="center">
                  <Typography className={classes.instructions}>
                    Bitte ordnen Sie zuerst jeder atomaren Komponente einen Rohstoff zu.
                  </Typography>
                  <Button onClick={handleClose} className={classes.buttons2}>
                    Ok
                  </Button>
                </Grid>
            </div>
        </DialogContent>
      </Dialog>
    </div>
  );
};
export default EvaluationWarningDialog;
