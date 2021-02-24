import React from "react";
import { useContext } from "react";

// Component
import { MainContext } from "./MainContext.jsx";

import MaterialSearch from "./MaterialSearch.jsx";

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

const MaterialSearchDialog = () => {
  const classes = useStyles();

  const { add_plast_open } = useContext(MainContext);

  const [addPlastOpen, setAddPlastOpen] = add_plast_open;

  handleClickPlastOpen = () => {
    setAddPlastOpen(true);
  };

  handleClickPlastClose = () => {
    setAddPlastOpen(false);
  };

  return (
    <div>
      <Button className={classes.buttons} onClick={handleClickBomOpen}>
        <CreateIcon style={{ marginRight: 5 }}></CreateIcon>
        Erstellen
      </Button>
      <Dialog
        open={addPlastOpen}
        onClose={handleClickPlastClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogActions>
          <HighlightOffIcon
            style={{ color: "#005000" }}
            onClick={handleClickPlastClose}
          ></HighlightOffIcon>
        </DialogActions>
        <DialogTitle id="form-dialog-title">Materialsuche</DialogTitle>
        <DialogContent>
          <MaterialSearch></MaterialSearch>
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default MaterialSearchDialog;