// author: topr
// last updated: 11.11.2020
// currently used: yes
// description: includes topsis method

import React from "react";
import { useEffect, useContext, useState } from "react";

//Components
import { MainContext } from "./MainContext.jsx";

//Material UI
import { makeStyles, withStyles } from "@material-ui/core/styles";
import Rating from "@material-ui/lab/Rating";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import FiberManualRecordIcon from "@material-ui/icons/FiberManualRecord";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Checkbox from "@material-ui/core/Checkbox";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import ListItemText from "@material-ui/core/ListItemText";
import Select from "@material-ui/core/Select";

//Devexpress
import {
  SelectionState,
  IntegratedSorting,
  SortingState,
} from "@devexpress/dx-react-grid";
import {
  Grid as GridDevExpress,
  Table,
  TableSelection,
  TableColumnVisibility,
  TableHeaderRow,
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
  textfield: { margin: 0, padding: 0, background: "white" },
  title: {
    fontSize: 13,
  },
  card_div: {
    marginBottom: 15,
  },
  formControl: {
    minWidth: 325,
  },
  root_card: {
    marginLeft: 50,
    marginRight: 50,
    marginTop: 20,
    marginBottom: 20,
    height: 100,
    width: 200,
  },
}));

const StyledRating = withStyles({
  iconFilled: {
    color: "#005000",
  },
  iconHover: {
    color: "#005000",
  },
})(Rating);

const Comparison = () => {
  const classes = useStyles();

  const { selected_construction_id, selected_construction_title } = useContext(
    MainContext
  );

  const [
    selectedConstructionId,
    setSelectedConstructionId,
  ] = selected_construction_id;
  const [
    selectedConstructionTitle,
    setSelectedConstructionTitle,
  ] = selected_construction_title;

  const [weightsSet, setWeightsSet] = useState(false);
  const [comparisionDone, setComparisonDone] = useState(false);
  const [alternatives, setAlternatives] = useState([]);
  const [selection, setSelection] = useState([]);
  const [resultData, setResultData] = useState([]);
  const [comparisonData, setComparisionData] = useState([]);

  const [columns] = useState([
    { name: "mat_id", title: "Mat.Nr."},
    { name: "mat_desc", title: "Mat.Bez."},
    { name: "recycling_cat", title: "Rec.Kat."},
    { name: "mat_rw", title: "Rec.Fäh."},
    { name: "price", title: "Preis"},
    { name: "co2_value", title: "GWP"},
    { name: "resource_use", title: "ADPf"},
  ]);

  const [tableColumnExtensions] = useState([
    { columnName: "mat_id", width: 75 },
    { columnName: "mat_desc", width: 250 },
    { columnName: "recycling_cat", width: 75 },
    { columnName: "mat_rw", width: 75 },
    { columnName: "price", width: 75 },
    { columnName: "co2_value", width: 75 },
    { columnName: "resource_use", width: 75 },
  ]);

  const [rowSelection, setRowSelection] = useState([]);

  const [evaluationRatings, setEvaluationRatings] = useState({
    recycling: 2,
    co2: 2,
    price: 2,
  });

  const [weights, setWeights] = useState({
    price: 0.33,
    co2: 0.33,
    recycling: 0.33,
  });

  const calcWeights = () => {
    setWeights({
      ...weights,
      ["recycling"]:
        evaluationRatings.recycling /
        (evaluationRatings.price +
          evaluationRatings.co2 +
          evaluationRatings.recycling),
      ["co2"]:
        evaluationRatings.co2 /
        (evaluationRatings.price +
          evaluationRatings.co2 +
          evaluationRatings.recycling),
      ["price"]:
        evaluationRatings.price /
        (evaluationRatings.price +
          evaluationRatings.co2 +
          evaluationRatings.recycling),
    });
  };

  const [topsisData, setTopsisData] = useState([
    {
      id: 1,
      mat_desc: "Elektrische Zahnbuerste A",
      price: 1.9,
      co2: 0.75,
      recycling: 0.75,
    },
    {
      id: 2,
      mat_desc: "Elektrische Zahnbuerste B",
      price: 2.0,
      co2: 0.8,
      recycling: 0.9,
    },
    {
      id: 3,
      mat_desc: "Elektrische Zahnbuerste C",
      price: 1.6,
      co2: 0.7,
      recycling: 0.55,
    },
    {
      id: 4,
      mat_desc: "Elektrische Zahnbuerste D",
      price: 1.2,
      co2: 0.8,
      recycling: 0.3,
    },
  ]);

  const [topsisColumns] = useState([
    { name: "id", title: "Mat.Nr." },
    { name: "mat_desc", title: "Mat.Bez." },
    { name: "price", title: "Preis" },
    { name: "co2", title: "C02-Wert" },
    { name: "recycling", title: "Recyclingwert" },
  ]);

  const [tableColumnExtensions] = useState([
    { columnName: "id", width: 100 },
    { columnName: "mat_desc", width: 350 },
    { columnName: "price", width: 150 },
    { columnName: "co2", width: 150 },
    { columnName: "recycling", width: 150 },
  ]);

  const compareAlternatives = () => {
    calcWeights();
    setWeightsSet(true);
  };

  useEffect(() => {
      fetch("/mat_eval/" + selectedConstructionId)
        .then((res) => {
          return res.json();
        })
        .then((d) => {
          setComparisionData(d);;
        });
  });

  return (
    <div>
      <Grid
        container
        item
        xs={12}
        style={{
          marginTop: 25,
          textAlign: "center",
        }}
      >
        <GridDevExpress rows={comparisonData} columns={columns}>
          <SelectionState
            selection={rowSelection}
            onSelectionChange={setRowSelection}
          />
          <IntegratedSorting />
          <Table columnExtensions={tableColumnExtensions} />
          <TableHeaderRow showSortingControls />
          <TableTreeColumn for="mat_id" showSelectionControls />
          <Toolbar />
        </GridDevExpress>
      </Grid>









      <Grid
        container
        item
        xs={12}
        style={{
          marginTop: 25,
          textAlign: "center",
        }}
      >
        <Grid item xs={4} style={{ marginTop: 30 }}>
          <Box component="fieldset" mb={3} borderColor="transparent">
            <Typography component="legend">Recyclingwert</Typography>
            <StyledRating
              name="recycling"
              value={evaluationRatings.recycling}
              max={10}
              onChange={(event, newValue) => {
                setEvaluationRatings({
                  ...evaluationRatings,
                  ["recycling"]: newValue,
                });
              }}
              icon={<FiberManualRecordIcon fontSize="inherit" />}
            />
          </Box>
          <Box component="fieldset" mb={3} borderColor="transparent">
            <Typography component="legend">Preis</Typography>
            <StyledRating
              name="price"
              value={evaluationRatings.price}
              max={10}
              onChange={(event, newValue) => {
                setEvaluationRatings({
                  ...evaluationRatings,
                  ["price"]: newValue,
                });
              }}
              icon={<FiberManualRecordIcon fontSize="inherit" />}
            />
          </Box>
          <Box component="fieldset" mb={3} borderColor="transparent">
            <Typography component="legend">CO2-Wert</Typography>
            <StyledRating
              name="co2"
              value={evaluationRatings.co2}
              max={10}
              onChange={(event, newValue) => {
                setEvaluationRatings({
                  ...evaluationRatings,
                  ["co2"]: newValue,
                });
              }}
              icon={<FiberManualRecordIcon fontSize="inherit" />}
            />
          </Box>
        </Grid>
        <Grid item xs={8}>
          <Grid
            container
            item
            xs={12}
            style={{
              marginTop: 25,
              textAlign: "center",
            }}
          >
            <Grid item xs={4}>
              <Card className={classes.root_card} variant="outlined">
                <CardContent>
                  <Typography
                    className={classes.title}
                    color="textSecondary"
                    gutterBottom
                    align="center"
                  >
                    Gewichtung Recyclingwert
                  </Typography>
                  <Typography variant="h5" component="h2" align="center">
                    {Number(
                      (evaluationRatings.recycling * 100) /
                        (evaluationRatings.price +
                          evaluationRatings.co2 +
                          evaluationRatings.recycling)
                    ).toFixed(2)}{" "}
                    %
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={4}>
              {" "}
              <Card className={classes.root_card} variant="outlined">
                <CardContent>
                  <Typography
                    className={classes.title}
                    color="textSecondary"
                    gutterBottom
                    align="center"
                  >
                    Gewichtung Preis
                  </Typography>
                  <Typography variant="h5" component="h2" align="center">
                    {Number(
                      (evaluationRatings.price * 100) /
                        (evaluationRatings.price +
                          evaluationRatings.co2 +
                          evaluationRatings.recycling)
                    ).toFixed(2)}{" "}
                    %
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={4}>
              <Card className={classes.root_card} variant="outlined">
                <CardContent>
                  <Typography
                    className={classes.title}
                    color="textSecondary"
                    gutterBottom
                    align="center"
                  >
                    Gewichtung C02-Wert
                  </Typography>
                  <Typography variant="h5" component="h2" align="center">
                    {Number(
                      (evaluationRatings.co2 * 100) /
                        (evaluationRatings.price +
                          evaluationRatings.co2 +
                          evaluationRatings.recycling)
                    ).toFixed(2)}{" "}
                    %
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid
              container
              item
              xs={12}
              style={{
                marginTop: 25,
                marginLeft: 50,
                textAlign: "left",
              }}
            >
              <Grid xd={6}>
                <Typography>
                  Bitte wählen Sie zwei oder mehr Stücklisten aus.
                </Typography>
                <FormControl className={classes.formControl}>
                  <InputLabel id="demo-mutiple-checkbox-label">
                    Stücklisten
                  </InputLabel>
                  <Select
                    labelId="demo-mutiple-checkbox-label"
                    id="demo-mutiple-checkbox"
                    multiple
                    value={alternatives}
                    onChange={handleDropdownChange}
                    input={<Input />}
                    renderValue={(selected) => selected.join(", ")}
                  >
                    {listDropdownData.map((name) => (
                      <MenuItem key={name} value={name}>
                        <Checkbox checked={alternatives.indexOf(name) > -1} />
                        <ListItemText primary={name} />
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>
              <Grid
                xd={3}
                style={{
                  textAlign: "right",
                }}
              >
                <Button
                  className={classes.buttons}
                  onClick={() => {
                    compareAlternatives();
                    console.log(weights);
                  }}
                >
                  Vergleich durchführen
                </Button>
                <Grid
                  xd={3}
                  style={{
                    textAlign: "right",
                  }}
                >
                  <Button
                    className={classes.buttons}
                    variant="outlined"
                    onClick={() => {
                      console.log(resultData);
                    }}
                  >
                    Print Ergebnis
                  </Button>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
      <Grid
        container
        item
        xs={12}
        style={{
          marginLeft: 25,
          textAlign: "center",
        }}
      >
        <GridDevExpress rows={topsisData} columns={topsisColumns}>
          <SelectionState
            selection={selection}
            onSelectionChange={setSelection}
          />
          <SortingState />
          <IntegratedSorting />
          <Table columnExtensions={tableColumnExtensions} />
          <TableSelection />
          <TableColumnVisibility />
          <Toolbar />
          <TableHeaderRow showSortingControls />
        </GridDevExpress>
      </Grid>
    </div>
  );
};

export default Comparison;
