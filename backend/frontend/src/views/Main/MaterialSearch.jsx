import React, { Fragment, useEffect, useState } from "react";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from '@material-ui/lab/Autocomplete';
import {Button} from "@material-ui/core";
import Grid from "@material-ui/core/Grid";

// Data
//import autocompleteData from "../../files/search_plast_data.json";
import autocompleteData from "../../files/autocomplete.json";


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
    mat_desc: "default",
    campus_fam: "default",
    producer: "default",
    verarbeitungsmethode: "default",
  };
  
  const [filter, setFilter] = useState(initial_filter);


  materials = [
    "swaggy",
    "lordy",
    "deluxe"
  ]

  return (
    <div>
      <Grid container item xs={12}>
        <Grid item xs={6}>
          <Autocomplete
              id="mat_desc"
              options={materials}
              getOptionLabel={(option) => option}
              onChange={(newValue) => setFilter({ ...filter, mat_desc: newValue })}
              renderInput={(params) => <TextField {...params} label="Materialbeschreibung" margin="normal" />}
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





