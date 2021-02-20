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
  textfield: { margin: 10, padding: 0, background: "white" },
}));

const MaterialSearch = () => {
  const classes = useStyles();

  const [matDesc, setMatDesc] = useState("");
  const [campusFam, setCampusFam] = useState("");
  const [producer, setProducer] = useState("");
  const [method, setMethod] = useState("");
  const [zugmodul, setZugmodul] = useState("");
  const [bruchspannung, setBruchspannung] = useState("");
  const [bruchdehnung, setBruchdehnung] = useState("");
  const [mvr, setMvr] = useState("");
  const [dichte, setDichte] = useState("");
  const [belastung, setBelastung] = useState("");
  const [temperatur, setTemperatur] = useState("");

  const initiateSearch = () => {
    const filter = {
      mat_desc: matDesc,
      campus_fam: campusFam,
      producer: producer,
      verarbeitungsmethode: method,
      zugmodul: zugmodul,
      bruchspannung: bruchspannung,
      bruchdehnung: bruchdehnung,
      mvr: mvr,
      dichte: dichte,
      belastung: belastung,
      temperatur: temperatur,
    };
    console.log(filter);
  };

  const resetSearch = () => {
    setMatDesc("");
    setCampusFam("");
    setProducer("");
    setMethod("");
    setZugmodul("");
    setBruchspannung("");
    setBruchdehnung("");
    setMvr("");
    setDichte("");
    setBelastung("");
    setTemperatur("");
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
        <Grid item xs={6}>





      



        <Autocomplete
            id="zugmodul"
            options={autocompleteData.zugmodul}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={zugmodul}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Zugmodul"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="bruchspannung"
            options={autocompleteData.bruchspannung}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={bruchspannung}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Bruchspannung"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="bruchdehnung"
            options={autocompleteData.bruchdehnung}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={bruchdehnung}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Bruchdehnung"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="mvr"
            options={autocompleteData.mvr}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={mvr}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="MVR"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="dichte"
            options={autocompleteData.dichte}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={dichte}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Dichte"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="belastung"
            options={autocompleteData.belastung}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={Belastung}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Belastung"
                margin="normal"
              />
            )}
          />
          <Autocomplete
            id="temperatur"
            options={autocompleteData.temperatur}
            getOptionLabel={(option) => option}
            onChange={(event) => setMethod(event.target.textContent)}
            value={temperatur}
            renderInput={(params) => (
              <TextField
                {...params}
                className={classes.textfield}
                label="Temperatur"
                margin="normal"
              />
            )}
          />
        </Grid>
      </Grid>
      <Grid container item xs={12} justify="center">
        <Grid item xs={4}>
          <Button className={classes.buttons} onClick={resetSearch}>
            Zurücksetzen
          </Button>
        </Grid>
        <Grid item xs={4}></Grid>

        <Grid item xs={4}>
          <Button className={classes.buttons} onClick={initiateSearch}>
            Suche starten
          </Button>
        </Grid>
      </Grid>
    </div>
  );
};

export default MaterialSearch;
