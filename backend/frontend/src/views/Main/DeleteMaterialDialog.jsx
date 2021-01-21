import React from "react";
import { useContext } from "react";

//Components
import { MainContext } from "./MainContext.jsx";

//Material UI
import Button from "@material-ui/core/Button";
import { makeStyles } from "@material-ui/core/styles";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogTitle from "@material-ui/core/DialogTitle";
import Grid from "@material-ui/core/Grid";
import HighlightOffIcon from "@material-ui/icons/HighlightOff";
import { Typography } from "@material-ui/core";
import DeleteIcon from "@material-ui/icons/Delete";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import WarningIcon from "@material-ui/icons/Warning";

// css theme
const useStyles = makeStyles((theme) => ({
  root: {
    "& > *": {
      margin: theme.spacing(1),
      width: "25ch",
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
}));

const DeleteMaterialDialog = () => {
  const classes = useStyles();

  const { delete_component_open, bom_updated, delete_material } = useContext(
    MainContext
  );

  const [deleteComponentOpen, setDeleteComponentOpen] = delete_component_open;
  const [deleteMaterial, setDeleteMaterial] = delete_material;
  const [bomUpdated, setBomUpdated] = bom_updated;

  const handleClickOpen = () => {
    setDeleteComponentOpen(true);
  };

  const handleClose = () => {
    setDeleteMaterial([]);
    setDeleteComponentOpen(false);
  };

  const deleteBomEntry = (compId) => {
    var requestOptions = {
      method: "DELETE",
      redirect: "follow",
    };
    fetch("http://localhost:5000/bom/" + compId, requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));

    setBomUpdated(true);
  };

  return (
    <div>
      <Button className={classes.buttons} onClick={handleClickOpen}>
        <DeleteIcon style={{ marginRight: 5 }}></DeleteIcon>
        Löschen
      </Button>
      <Dialog
        open={deleteComponentOpen}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogActions>
          <HighlightOffIcon
            style={{ color: "#005000" }}
            onClick={handleClose}
          ></HighlightOffIcon>
        </DialogActions>
        <DialogTitle id="form-dialog-title">Komponente löschen</DialogTitle>
        <DialogContent>
          <Typography>Wollen Sie die Komponente wirklich löschen?</Typography>
          <Grid container item xs={12} justify="center">
            <Card className={classes.root_card} variant="outlined">
              <CardContent>
                <Typography
                  className={classes.title}
                  color="textSecondary"
                  gutterBottom
                  align="center"
                >
                  Ausgewähltes Material:
                </Typography>
                <Typography variant="h5" component="h2" align="center">
                  {deleteMaterial}
                </Typography>
              </CardContent>
            </Card>
            {!deleteMaterial ? (
              <div style={{ color: "red", marginTop: 10, marginBottom: 10 }}>
                <WarningIcon
                  style={{
                    fontSize: "small",
                    marginRight: 10,
                  }}
                ></WarningIcon>{" "}
                Sie müssen ein Unterkomponente auswählen, um diese zu Löschen.
              </div>
            ) : (
              <div />
            )}
          </Grid>

          <Grid container item xs={12}>
            <Grid item xs={6}>
              <Button
                color="primary"
                className={classes.buttons}
                variant="outlined"
                onClick={handleClose}
              >
                Nein
              </Button>
            </Grid>

            <Grid item xs={6}>
              <Button
                color="primary"
                className={classes.buttons}
                variant="outlined"
                onClick={() => {
                  deleteBomEntry(deleteMaterial);
                  handleClose();
                }}
              >
                Ja
              </Button>
            </Grid>
          </Grid>
        </DialogContent>
      </Dialog>
    </div>
  );
};
export default DeleteMaterialDialog;
