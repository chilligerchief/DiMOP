// author: topr
// last updated: 28.04.2021
// currently used: yes
// description: rebuild of Comparison.jsx because I broke it

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

//Devexpress
import {
  SelectionState,
  IntegratedSorting,
  SortingState,
} from "@devexpress/dx-react-grid";
import {
  Grid as GridDevExpress,
  Table,
  TableHeaderRow,
  TableTreeColumn,
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

const CompareMaterials = () => {
  const classes = useStyles();

  const {
    selected_construction_id,
    selected_construction_title,
    comparison_data,
  } = useContext(MainContext);

  const [
    selectedConstructionId,
    setSelectedConstructionId,
  ] = selected_construction_id;

  const [
    selectedConstructionTitle,
    setSelectedConstructionTitle,
  ] = selected_construction_title;

  const [comparisonData, setComparisionData] = comparison_data;

  const [columnsComparison] = useState([
    { name: "id", title: "Mat.Nr." },
    { name: "mat_desc", title: "Mat.Bez." },
    { name: "recycling_cat", title: "Rec.Kat." },
    { name: "mat_rw", title: "Rec.Fäh." },
    { name: "price", title: "Preis" },
    { name: "co2_value", title: "GWP" },
    { name: "resource_use", title: "ADPf" },
  ]);

  const [tableColumnExtensionsComparison] = useState([
    { columnName: "id", width: 150 },
    { columnName: "mat_desc", width: 250 },
    { columnName: "recycling_cat", width: 150 },
    { columnName: "mat_rw", width: 150 },
    { columnName: "price", width: 150 },
    { columnName: "co2_value", width: 150 },
    { columnName: "resource_use", width: 150 },
  ]);

  const [rowSelection, setRowSelection] = useState([]);

  useEffect(() => {
    if (selectedConstructionTitle !== "Bitte auswaehlen") {
      fetch("/mat_eval_get/" + selectedConstructionId)
        .then((res) => {
          return res.json();
        })
        .then((d) => {
          console.log(selectedConstructionId);
          console.log(d);
          setComparisionData(d);
          console.log(comparisonData);
        });
    } else {
    }
  }, []);

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
        <div>
          <GridDevExpress rows={comparisonData} columns={columnsComparison}>
            <SelectionState
              selection={rowSelection}
              onSelectionChange={setRowSelection}
            />
            <TreeDataState />
            <SortingState />
            <IntegratedSorting />
            <Table columnExtensions={tableColumnExtensionsComparison} />
            <TableHeaderRow showSortingControls />
            <TableTreeColumn for="id" showSelectionControls />
            <Toolbar />
          </GridDevExpress>
        </div>
      </Grid>
    </div>
  );
};

export default CompareMaterials;
