import React, { Fragment, useEffect, useState } from "react";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from '@material-ui/lab/Autocomplete';
import {Button} from "@material-ui/core";
import Grid from "@material-ui/core/Grid";

// Data
import autocompleteData from "../../files/search_plast_data.json";


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
  textfield: { margin: 0, padding: 0, background: "white" },
  root_card: {
    marginTop: 15,
    marginBottom: 0,
  },
}));

const MaterialSearch = () => {
  const classes = useStyles();


  const initial_filter = {
    mat_desc: "default",
    campus_fam: "default",
    producer: "default",
    verarbeitungsmethode: "default",
  };
  
  const [filter, setFilter] = useState(initial_filter);


  const materials = [
    "swaggy",
    "lordy",
    "deluxe"
  ]

  const handleNewFilterInputs = (event) => {
    setFilter({ ...filter, [event.target.id]: event.target.textContent });
  };

  return (
    <div>
      <Grid container item xs={12}>
        <Grid item xs={6}>
          <Autocomplete
              id="mat_desc"
              options={materials}
              onChange={handleNewFilterInputs}
              disableClearable
              value={filter.mat_desc}
              renderInput={(params) => <TextField {...params} 
              className={classes.textfield}
              label="Materialbeschreibung" margin="normal" />}
            />
          <Button
          onClick={ () => {
            console.log(filter);
            console.log(filter.mat_desc);
            console.log(typeof filter.mat_desc);
            }
          }
          >
            Print
            </Button>
        </Grid>
          <Grid item xs={6}>
          </Grid>
        </Grid>
    </div>
  );
};

export default MaterialSearch;





