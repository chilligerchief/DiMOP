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

const DeleteConstructionDialog = () => {
  const classes = useStyles();

  const {
    delete_construction_open,
    constructions_updated,
    selected_construction_id,
  } = useContext(MainContext);

  const [
    selectedConstructionId,
    setSelectedConstructionId,
  ] = selected_construction_id;
  const [constructionsUpdated, setConstructionsUpdated] = constructions_updated;
  const [
    delecteConstructionOpen,
    setDeleteConstructionOpen,
  ] = delete_construction_open;

  const handleClickOpen = () => {
    setDeleteConstructionOpen(true);
  };

  const handleClose = () => {
    setDeleteConstructionOpen(false);
    setSelectedConstructionId([]);
  };

  const deleteConstructionEntry = (consId) => {
    var requestOptions = {
      method: "DELETE",
      redirect: "follow",
    };
    fetch("/cons/" + consId, requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));

    setConstructionsUpdated(!constructionsUpdated);
  };

  return (
    <div>
      <Button className={classes.buttons} onClick={handleClickOpen}>
        <DeleteIcon style={{ marginRight: 5 }}></DeleteIcon>
        Löschen
      </Button>
      <Dialog
        open={delecteConstructionOpen}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogActions>
          <HighlightOffIcon
            style={{ color: "#005000" }}
            onClick={handleClose}
          ></HighlightOffIcon>
        </DialogActions>
        <DialogTitle id="form-dialog-title">Konstruktion löschen</DialogTitle>
        <DialogContent>
          <Typography>Wollen Sie die Konstruktion wirklich löschen?</Typography>

          <Grid container item xs={12} justify="center">
            <Card className={classes.root_card} variant="outlined">
              <CardContent>
                <Typography
                  className={classes.title}
                  color="textSecondary"
                  gutterBottom
                  align="center"
                >
                  Ausgewählte Konstruktion:
                </Typography>
                <Typography variant="h5" component="h2" align="center">
                  {selectedConstructionId}
                </Typography>
              </CardContent>
            </Card>
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
                  console.log(typeof selectedConstructionId);
                  deleteConstructionEntry(selectedConstructionId);
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
export default DeleteConstructionDialog;
