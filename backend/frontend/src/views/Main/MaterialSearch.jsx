import React, { useContext, useState } from "react";
import { MainContext } from "./MainContext.jsx";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/lab/Autocomplete";
import { Button, Slider } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import PolymerIcon from "@material-ui/icons/Polymer";
import SearchIcon from "@material-ui/icons/Search";
import LoopIcon from "@material-ui/icons/Loop";

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
    margin: 5,
    height: 60,
    width: 120,
  },
  textfield: { margin: 10, padding: 0, background: "white" },
}));

const MaterialSearch = () => {
  const classes = useStyles();

  const { search_dialog_open, parent_material, bom_updated } = useContext(
    MainContext
  );

  const [searchDialogOpen, setSearchDialogOpen] = search_dialog_open;
  const [parentMaterial, setParentMaterial] = parent_material;
  const [bomUpdated, setBomUpdated] = bom_updated;

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

  const [resultData, setResultData] = useState([]);
  const [resultCount, setResultCount] = useState(0);
  const [resultsReturned, setResultsReturned] = useState(false);

  const [selection, setSelection] = useState([]);

  const addPlast = () => {
    if (selection.length == 1) {
      var requestOptions = {
        method: "PUT",
        redirect: "follow",
      };

      fetch(
        "/mat/" + parentMaterial + "?mara_plast_id=" + resultData[selection].id,
        requestOptions
      )
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));

      setBomUpdated(true);
    } else {
      console.log("Nope");
    }
  };

  const handleClickPlastClose = () => {
    setSearchDialogOpen(false);
  };

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

    fetch("/search", requestOptions)
      .then((res) => {
        return res.json();
      })
      .then((d) => {
        setResultData(d);
        setResultCount(Object.keys(d).length);
        setResultsReturned(true);
      });
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
    setResultData([]);
  };

  const [resultColumns] = useState([
    { name: "id", title: "ID" },
    { name: "mat_desc", title: "Mat.Beschreibung" },
    { name: "mat_int_desc", title: "Mat.Beschreibung(Intern)" },
    { name: "campus_fam", title: "Kunstst.Fam." },
    { name: "producer", title: "Hersteller" },
    { name: "Verarbeitungsmethode", title: "Verarbeitungsmeth." },
    { name: "dichte_trocken", title: "Dichte(trocken)" },
    { name: "dichte_konditioniert", title: "Dichte(kond.)" },
    { name: "Belastung_trocken", title: "Belastung(trocken)" },
    { name: "Belastung_konditioniert", title: "Belastung(kond.)" },
    { name: "Temperatur_trocken", title: "Temperatur(trocken)" },
    { name: "Temperatur_konditioniert", title: "Temperatur(kond.)" },
    { name: "MVR_trocken", title: "MVR(trocken)" },
    { name: "MVR_konditioniert", title: "MVR(kond.)" },
    { name: "Bruchdehnung_trocken", title: "Bruchdehn.(trocken)" },
    { name: "Bruchdehnung_konditioniert", title: "Bruchdehn.(kond.)" },
    {
      name: "Bruchdehnung_Nominell_trocken",
      title: "Bruchdehnung.nomin.(trocken)",
    },
    {
      name: "Bruchdehnung_Nominell_konditioniert",
      title: "Bruchdehn.nomin.(kond.)",
    },
    { name: "Bruchdehnung_TPE_trocken", title: "Bruchdehn.TPE(trocken)" },
    { name: "Bruchdehnung_TPE_konditioniert", title: "Bruchdehn.TPE(kond.)" },
    { name: "Bruchdehnung_Parallel_trocken", title: "Bruchdehn.par.(trocken)" },
    {
      name: "Bruchdehnung_Parallel_konditioniert",
      title: "Bruchdehn.par.(kond.)",
    },
    { name: "Bruchspannung_MPa_trocken", title: "Bruchsp.MPa(trocken)" },
    { name: "Bruchspannung_MPa_konditioniert", title: "Bruchsp.MPa(kond.)" },
    {
      name: "Bruchspannung_TPE_MPa_trocken",
      title: "Bruchsp.TPE/MPa(trocken)",
    },
    {
      name: "Bruchspannung_TPE_MPa_konditioniert",
      title: "Bruchsp.TPE/MPa(kond.)",
    },
    {
      name: "Bruchspannung_Parallel_MPa_trocken",
      title: "Bruchsp.par.MPa(trocken)",
    },
    {
      name: "Bruchspannung_Parallel_MPa_konditioniert",
      title: "Bruchsp.par.MPa(kond.)",
    },
    {
      name: "Bruchspannung_Senkrecht_MPa_trocken",
      title: "Bruchsp.senk.MPa(trocken)",
    },
    {
      name: "Bruchspannung_Senkrecht_MPa_konditioniert",
      title: "Bruchsp.senk.MPa(kond.)",
    },
    { name: "Zugmodul_MPa_trocken", title: "Zugmod.MPa(trocken)" },
    { name: "Zugmodul_MPa_konditioniert", title: "Zugmod.MPa(kond.)" },
    {
      name: "Zugmodul_Kriech_1h_MPa_trocken",
      title: "Zugmod.Kriech.1h.MPa(trocken)",
    },
    {
      name: "Zugmodul_Kriech_1h_MPa_konditioniert",
      title: "Zugmod.Kriech.1h.MPa(kond.)",
    },
    {
      name: "Zugmodul_Kriech_1000h_MPa_trocken",
      title: "Zugmod.Kriech.1000h.MPa(trocken)",
    },
    {
      name: "Zugmodul_Kriech_1000h_MPa_konditioniert",
      title: "Zugmod.Kriech.1000h.MPa(kond.)",
    },
    { name: "Zugmodul_Parallel_MPa_trocken", title: "Zugmod.par.MPa(trocken)" },
    {
      name: "Zugmodul_Parallel_MPa_konditioniert",
      title: "Zugmod.par.MPa(kond.)",
    },
    {
      name: "Zugmodul_Senkrecht_MPa_trocken",
      title: "Zugmod.senk.MPa(trocken)",
    },
    {
      name: "Zugmodul_Senkrecht_MPa_konditioniert",
      title: "Zugmod.senk.MPa(kond.)",
    },
  ]);

  return (
    <div>
      <Grid container item xs={12}>
        Suchparameter



















        
      </Grid>
      <Grid container item xs={12}>
        <Grid container item xs={12}>
          <Grid item xs={4} justify="center" alignContent="center">
            {" "}
            <Button className={classes.buttons} onClick={resetSearch}>
              <LoopIcon style={{ marginRight: 5 }}></LoopIcon>
              Zurücksetzen
            </Button>{" "}
          </Grid>
          <Grid item xs={4} justify="center" alignContent="center">
            {" "}
            <Button className={classes.buttons} onClick={initiateSearch}>
              <SearchIcon style={{ marginRight: 5 }}></SearchIcon>
              Suche starten
            </Button>{" "}
          </Grid>
          <Grid item xs={4} justify="center" alignContent="center">
            {" "}
            <Button
              className={classes.buttons}
              onClick={() => {
                addPlast();
                handleClickPlastClose();
              }}
            >
              <PolymerIcon style={{ marginRight: 5 }}></PolymerIcon>
              Zuweisen
            </Button>
          </Grid>
        </Grid>
      </Grid>
      <Grid container item xs={12}>
        <Grid container item xs={12}>
          {resultsReturned == false ? (
            <div></div>
          ) : (
            <div style={{ color: "black", marginTop: 25 }}>
              {" "}
              Es wurden {resultCount} Ergebnisse mit Ihren Spezifikationen
              gefunden.
            </div>
          )}
        </Grid>
      </Grid>
      <Grid container item xs={12}>
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
      </Grid>
    </div>
  );
};

export default MaterialSearch;
