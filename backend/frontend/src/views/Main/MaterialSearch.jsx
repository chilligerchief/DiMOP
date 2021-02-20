import React, { Fragment, useEffect, useState } from "react";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/core/TextField";


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

const MaterialSearch = () => {
  const classes = useStyles();


  const initial_filter = {
    mat_desc: "",
    campus_fam: "",
    producer: "",
    verarbeitungsmethode: "",
  };
  
  const [filter, setFilter] = useState(initial_filter);


  const materials = [
    "Eins", 
    "Zwei",
    "Drei"
  ]

  const handleFilterInputs = (event) => {
    setFilter({ ...filter, [event.target.id]: event.target.value });
  };

  return (
    <div>
      <form className={classes.root} noValidate autoComplete="off">
      <Autocomplete
          id="mat_desc"
          label="Materialbeschreibung"
          options={materials}
          getOptionLabel={materials}
          // value={initial_filter.mat_desc}
          // onChange={handleFilterInputs}
          margin="normal"
          renderInput={(params) => <TextField {...params} label="Combo box" variant="outlined" />}
        />
      </form>
      <p>
        Swaggger.
      </p>
    </div>
  );
};

export default MaterialSearch;





