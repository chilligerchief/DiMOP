import React, { Fragment, useEffect, useState } from "react";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/lab/Autocomplete";
import { Button } from "@material-ui/core";
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

  const [matDesc, setMatDesc] = useState("");
  const [campusFam, setCampusFam] = useState("");
  const [producer, setProducer] = useState("");
  const [method, setMethod] = useState("");

  const initiateSearch = () => {
    const filter = {
      mat_desc: matDesc,
      campus_fam: campusFam,
      producer: producer,
      verarbeitungsmethode: method,
    };
    console.log(filter);
  };

  const initiateSearch = () => {
    setMatDesc("");
    setCampusFam("");
    setProducer("");
    setMethod("");
    console.log(filter);
  };

  return (
    <div>
      <Grid container item xs={12}>
        <Grid item xs={6}>
          <Autocomplete
            id="mat_desc"
            options={autocompleteData.mat_desc}
            getOptionLabel={(option) => option}
            onChange={(event) => setMatDesc(event.target.textContent)}
            value={matDesc}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Materialbeschreibung"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="mat_desc"
            options={autocompleteData.campus_fam}
            getOptionLabel={(option) => option}
            onChange={(event) => setCampusFam(event.target.textContent)}
            value={campusFam}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Kunststofffamilie"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="producer"
            options={autocompleteData.producer}
            getOptionLabel={(option) => option}
            onChange={(event) => setProducer(event.target.textContent)}
            value={producer}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Hersteller"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="producer"
            options={autocompleteData.verarbeitungsmethode}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={method}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Verarbeitungsmethode"
                margin="normal"
              />
            )}
          />
        </Grid>
        <Grid item xs={6}></Grid>
      </Grid>
      <Grid container item xs={12}>
        <Button className={classes.buttons} onClick={initiateSearch}>
          Suchen
        </Button>
        <Button className={classes.buttons} onClick={resetSearch}>
          Reset
        </Button>
      </Grid>
    </div>
  );
};

export default MaterialSearch;
