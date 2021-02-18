import React, { useContext, useState } from "react";

//Components
import { MainContext } from "./MainContext.jsx";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import Tooltip from "@material-ui/core/Tooltip";
import Typography from "@material-ui/core/Typography";
import HelpIcon from "@material-ui/icons/Help";


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
    height: 60,
    width: 120,
  },
}));

const MaterialSearch = (saveItem) => {

  const classes = useStyles();

  const initial_filter = {
    mat_desc: "",
    campus_fam: "",
    producer: "",
    verarbeitungsmethode: "",
  };

  const [filter, setFilter] = useState(initial_filter);

  return (
    <div>
      <p>
        Swaggger.
      </p>

    </div>
  );

  export default MaterialSearch;





}