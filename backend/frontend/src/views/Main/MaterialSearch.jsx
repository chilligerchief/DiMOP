import React, { Fragment, useEffect, useState } from "react";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from '@material-ui/lab/Autocomplete';
import {Button} from "@material-ui/core";

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
    { title: 'The Shawshank Redemption', year: 1994 },
    { title: 'The Godfather', year: 1972 },
    { title: 'The Godfather: Part II', year: 1974 },
    { title: 'The Dark Knight', year: 2008 }
  ]


  return (
    <div>
      <Autocomplete
          id="mat_desc"
          options={autocompleteData.mat_desc}
          getOptionLabel={(option) => option}
          onChange={(newValue) => setFilter({ ...filter, mat_desc: newValue })}
          renderInput={(params) => <TextField {...params} label="Materialbeschreibung" variant="outlined" />}
        />
      <Button
      onClick={console.log(filter)}
      >
        Print
        </Button>
    </div>
  );
};

export default MaterialSearch;





