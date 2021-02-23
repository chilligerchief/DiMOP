import React, { Fragment, useEffect, useState } from "react";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/lab/Autocomplete";
import { Button, Slider } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

// Data
import autocompleteData from "../../files/search_plast_data.json";

// devexpress
import {
  SelectionState,
  FilteringState,
  IntegratedFiltering,
} from "@devexpress/dx-react-grid";

import {
  Grid as GridDevExpress,
  Table,
  TableSelection,
  TableColumnVisibility,
  ColumnChooser,
  TableHeaderRow,
  TableFilterRow,
  Toolbar,
} from "@devexpress/dx-react-grid-material-ui";

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
  const [zugmodulSliderRange, setZugmodulSliderRange] = useState([0, 110000]);
  const [zugmodulSliderValue, setZugmodulSliderValue] = useState([
    zugmodulSliderRange[0],
    zugmodulSliderRange[1],
  ]);

  const [bruchspannung, setBruchspannung] = useState("");
  const [bruchspannungSliderRange, setBruchspannungSliderRange] = useState([
    6.0,
    1750.0,
  ]);
  const [bruchspannungSliderValue, setBruchspannungSliderValue] = useState([
    bruchspannungSliderRange[0],
    bruchspannungSliderRange[1],
  ]);

  const [bruchdehnung, setBruchdehnung] = useState("");
  const [bruchdehnungSliderRange, setBruchdehnungSliderRange] = useState([
    0.3,
    47000.0,
  ]);
  const [bruchdehnungSliderValue, setBruchdehnungSliderValue] = useState([
    bruchdehnungSliderRange[0],
    bruchdehnungSliderRange[1],
  ]);

  const [mvr, setMvr] = useState("");
  const [mvrSliderRange, setMvrSliderRange] = useState([0.1, 290.0]);
  const [mvrSliderValue, setMvrSliderValue] = useState([
    mvrSliderRange[0],
    mvrSliderRange[1],
  ]);

  const [dichte, setDichte] = useState("");
  const [dichteSliderRange, setDichteSliderRange] = useState([700.0, 3150.0]);
  const [dichteSliderValue, setDichteSliderValue] = useState([
    dichteSliderRange[0],
    dichteSliderRange[1],
  ]);

  const [belastung, setBelastung] = useState("");
  const [belastungSliderRange, setBelastungSliderRange] = useState([1.2, 21.6]);
  const [belastungSliderValue, setBelastungSliderValue] = useState([
    belastungSliderRange[0],
    belastungSliderRange[1],
  ]);

  const [temperatur, setTemperatur] = useState("");
  const [temperaturSliderRange, setTemperaturSliderRange] = useState([
    160.0,
    400.0,
  ]);
  const [temperaturSliderValue, setTemperaturSliderValue] = useState([
    temperaturSliderRange[0],
    temperaturSliderRange[1],
  ]);

  const initiateSearch = () => {

    const requestOptions = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        mat_desc: matDesc,
        campus_fam: campusFam,
        producer: producer,
        verarbeitungsmethode: method,
        zugmodul: zugmodul,
        zugmodul_min: zugmodulSliderValue[0],
        zugmodul_max: zugmodulSliderValue[1],
        bruchspannung: bruchspannung,
        bruchspannung_min: bruchspannungSliderValue[0],
        bruchspannung_max: bruchspannungSliderValue[1],
        bruchdehnung: bruchdehnung,
        bruchdehnung_min: bruchdehnungSliderValue[0],
        bruchdehnung_max: bruchdehnungSliderValue[1],
        mvr: mvr,
        mvr_min: mvrSliderValue[0],
        mvr_max: mvrSliderValue[1],
        dichte: dichte,
        dichte_min: dichteSliderValue[0],
        dichte_max: dichteSliderValue[1],
        belastung: belastung,
        belastung_min: belastungSliderValue[0],
        belastung_max: belastungSliderValue[1],
        temperatur: temperatur,
        temperatur_min: temperaturSliderValue[0],
        temperatur_max: temperaturSliderValue[1],
      }),
      redirect: "follow",
    };


    // ????
    fetch("/search", requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
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
    setZugmodulSliderValue([zugmodulSliderRange[0], zugmodulSliderRange[1]]);
    setBruchspannungSliderValue([
      bruchspannungSliderRange[0],
      bruchspannungSliderRange[1],
    ]);
    setBruchdehnungSliderValue([
      bruchdehnungSliderRange[0],
      bruchdehnungSliderRange[1],
    ]);
    setMvrSliderValue([mvrSliderRange[0], mvrSliderRange[1]]);
    setBelastungSliderValue([belastungSliderRange[0], belastungSliderRange[1]]);
    setDichteSliderValue([dichteSliderRange[0], dichteSliderRange[1]]);
    setTemperaturSliderValue([
      temperaturSliderRange[0],
      temperaturSliderRange[1],
    ]);
  };

  const [resultData, setResultData] = useState([]);

  const [selection, setSelection] = useState([]);

  const [resultColumns] = useState([
    { name: "id", title: "Konstr.Nr." },
    { name: "cons_title", title: "Konstr.Titel." },
    { name: "cons_desc", title: "Konstr.Beschr." },
    { name: "del_kz", title: "Lösch.Kennz." },
  ]);

  return (
    <div>
      <Grid container item xs={12}>
        <Grid item xs={3}>
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
            id="campus_fam"
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
            id="method"
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
          <Grid container item xs={12} justify="center">
            <Grid xs={6}>
              <Button className={classes.buttons} onClick={resetSearch}>
                Zurücksetzen
              </Button>
            </Grid>
            <Grid xs={6}>
              <Button className={classes.buttons} onClick={initiateSearch}>
                Suche starten
              </Button>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={1}></Grid>
        <Grid item xs={8}>
          <Grid container item xs={12}>
            <Grid item xs={5}>
              <Autocomplete
                id="zugmodul"
                options={autocompleteData.zugmodul}
                getOptionLabel={(option) => option}
                onChange={(event) => {
                  setZugmodul(event.target.textContent);
                }}
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
            </Grid>
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              <Typography id="range-slider" gutterBottom>
                Zugmodul
              </Typography>
              <Slider
                value={zugmodulSliderValue}
                onChange={(event, newValue) => {
                  setZugmodulSliderValue(newValue);
                }}
                min={zugmodulSliderRange[0]}
                max={zugmodulSliderRange[1]}
                step={10}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>
          <Grid container item xs={12}>
            <Grid item xs={5}>
              <Autocomplete
                id="bruchspannung"
                options={autocompleteData.bruchspannung}
                getOptionLabel={(option) => option}
                onChange={(event) => setBruchspannung(event.target.textContent)}
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
            </Grid>
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              <Typography id="range-slider" gutterBottom>
                Bruchspannung
              </Typography>
              <Slider
                value={bruchspannungSliderValue}
                onChange={(event, newValue) => {
                  setBruchspannungSliderValue(newValue);
                }}
                min={bruchspannungSliderRange[0]}
                max={bruchspannungSliderRange[1]}
                step={1}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>
          <Grid container item xs={12}>
            <Grid item xs={5}>
              <Autocomplete
                id="bruchdehnung"
                options={autocompleteData.bruchdehnung}
                getOptionLabel={(option) => option}
                onChange={(event) => setBruchdehnung(event.target.textContent)}
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
            </Grid>
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              <Typography id="range-slider" gutterBottom>
                Bruchdehnung
              </Typography>
              <Slider
                value={bruchdehnungSliderValue}
                onChange={(event, newValue) => {
                  setBruchdehnungSliderValue(newValue);
                }}
                min={bruchdehnungSliderRange[0]}
                max={bruchdehnungSliderRange[1]}
                step={10}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>

          <Grid container item xs={12}>
            <Grid item xs={5}>
              {" "}
              <Autocomplete
                id="mvr"
                options={autocompleteData.mvr}
                getOptionLabel={(option) => option}
                onChange={(event) => setMvr(event.target.textContent)}
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
            </Grid>
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              {" "}
              <Typography id="range-slider" gutterBottom>
                MVR
              </Typography>
              <Slider
                value={mvrSliderValue}
                onChange={(event, newValue) => {
                  setMvrSliderValue(newValue);
                }}
                min={mvrSliderRange[0]}
                max={mvrSliderRange[1]}
                step={1}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>

          <Grid container item xs={12}>
            <Grid item xs={5}>
              <Autocomplete
                id="dichte"
                options={autocompleteData.dichte}
                getOptionLabel={(option) => option}
                onChange={(event) => setDichte(event.target.textContent)}
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
            </Grid>
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              <Typography id="range-slider" gutterBottom>
                Dichte
              </Typography>
              <Slider
                value={dichteSliderValue}
                onChange={(event, newValue) => {
                  setDichteSliderValue(newValue);
                }}
                min={dichteSliderRange[0]}
                max={dichteSliderRange[1]}
                step={1}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>

          <Grid container item xs={12}>
            <Grid item xs={5}>
              {" "}
              <Autocomplete
                id="belastung"
                options={autocompleteData.belastung}
                getOptionLabel={(option) => option}
                onChange={(event) => setBelastung(event.target.textContent)}
                value={belastung}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    className={classes.textfield}
                    label="Belastung"
                    margin="normal"
                  />
                )}
              />
            </Grid>
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              {" "}
              <Typography id="range-slider" gutterBottom>
                Belastung
              </Typography>
              <Slider
                value={belastungSliderValue}
                onChange={(event, newValue) => {
                  setBelastungSliderValue(newValue);
                }}
                min={belastungSliderRange[0]}
                max={belastungSliderRange[1]}
                step={1}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>

          <Grid container item xs={12}>
            <Grid item xs={5}>
              <Autocomplete
                id="temperatur"
                options={autocompleteData.temperatur}
                getOptionLabel={(option) => option}
                onChange={(event) => setTemperatur(event.target.textContent)}
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
            <Grid item xs={1}></Grid>
            <Grid item xs={6}>
              {" "}
              <Typography id="range-slider" gutterBottom>
                Temperatur
              </Typography>
              <Slider
                value={temperaturSliderValue}
                onChange={(event, newValue) => {
                  setTemperaturSliderValue(newValue);
                }}
                min={temperaturSliderRange[0]}
                max={temperaturSliderRange[1]}
                step={1}
                valueLabelDisplay="auto"
              ></Slider>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
      <Grid container item xs={12}>
        <GridDevExpress rows={resultData} columns={resultColumns}>
          <SelectionState
            selection={selection}
            onSelectionChange={setSelection}
          />
          <FilteringState defaultFilters={[]} />
          <IntegratedFiltering />
          <Table />
          <TableSelection />
          <TableColumnVisibility />
          <Toolbar />
          <ColumnChooser />
          <TableFilterRow />
          <TableHeaderRow />
        </GridDevExpress>
      </Grid>
    </div>
  );
};

export default MaterialSearch;
