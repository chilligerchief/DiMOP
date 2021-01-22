import React from "react";
import { useEffect, useContext, useState } from "react";

//Components
import { MainContext } from "./MainContext.jsx";

//Material UI
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import { Typography } from "@material-ui/core";
import CheckCircleIcon from "@material-ui/icons/CheckCircle";
import WarningIcon from "@material-ui/icons/Warning";

//Devexpress
import {
  SelectionState,
  FilteringState,
  IntegratedFiltering,
  IntegratedSorting,
  SortingState,
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
    margin: 10,
    height: 30,
    width: 140,
  },
}));

const MatFertTable = () => {
  const classes = useStyles();

  const {
    selected_material,
    new_material,
    add_component_open,
    orga_id,
    bom_updated,
    parent_material,
    child_updated,
    add_component_mode,
    active_step,
  } = useContext(MainContext);

  const [activeStep, setActiveStep] = active_step;
  const [selectedMaterial, setSelectedMaterial] = selected_material;
  const [addComponentOpen, setAddComponentOpen] = add_component_open;
  const [orgaId, setOrgaId] = orga_id;
  const [childUpdated, setChildUpdated] = child_updated;
  const [loading, setLoading] = useState(true);
  const [materialData, setMaterialData] = useState([]);
  const [parentMaterial, setParentMaterial] = parent_material;
  const [materialValid, setMaterialValid] = useState(true);
  const [addComponentMode, setAddComponentMode] = add_component_mode;

  useEffect(() => {
    fetch("/mat?orga_id=" + orgaId)
      .then((res) => {
        return res.json();
      })
      .then((d) => {
        console.log(d);
        setMaterialData(d.filter((d) => d.id !== parentMaterial));
        console.log(materialData);
        setChildUpdated(false);
      });
  }, []);

  const [materialColumns] = useState([
    { name: "id", title: "Mat.Nr." },
    { name: "mat_desc", title: "Mat.Bez." },
    { name: "mat_id_int", title: "ERP Mat.Nr." },
    { name: "mat_desc_int", title: "ERP Bez." },
    { name: "cad_id", title: "CAD Nr." },
    { name: "mara_plast_id", title: "Kunststoff" },
    { name: "mat_rw", title: "Recycl." },
    { name: "height", title: "Höhe" },
    { name: "width", title: "Breite" },
    { name: "depth", title: "Tiefe" },
    { name: "unit", title: "Einheit" },
    { name: "weight", title: "Gewicht" },
    { name: "weight_unit", title: "G. Einheit" },
    { name: "volume", title: "Volumen" },
    { name: "volume_unit", title: "Vol. Einheit" },
    { name: "is_atomic", title: "Atomar?" },
  ]);

  const [defaultHiddenColumnNames] = useState([
    "mat_id_int",
    "mat_desc_int",
    "cad_id",
    "mara_plast_id",
    "mat_rw",
    "height",
    "width",
    "depth",
    "unit",
    "weight",
    "weight_unit",
    "volume",
    "volume_unit",
    "is_atomic",
  ]);

  const [tableColumnExtensions] = useState([{ columnName: "id", width: 100 }]);

  const [selection, setSelection] = useState([]);

  const onClickSelect = () => {
    if (selection.length == 1) {
      setSelectedMaterial(materialData[selection].id);
      setAddComponentMode("existing");
      setActiveStep(2);
    } else {
      setMaterialValid(false);
    }
  };

  return (
    <div>
      <GridDevExpress rows={materialData} columns={materialColumns}>
        <SelectionState
          selection={selection}
          onSelectionChange={setSelection}
        />
        <SortingState />
        <FilteringState defaultFilters={[]} />
        <IntegratedFiltering />
        <IntegratedSorting />
        <Table columnExtensions={tableColumnExtensions} />
        <TableSelection />
        <TableColumnVisibility
          defaultHiddenColumnNames={defaultHiddenColumnNames}
        />
        <Toolbar />
        <ColumnChooser />
        <TableFilterRow />
        <TableHeaderRow showSortingControls />
      </GridDevExpress>
      <Grid container item xs={12} justify="center">
        <Grid item xs={2}></Grid>
        <Grid item xs={8}>
          <Button className={classes.buttons} onClick={onClickSelect}>
            Material auswählen
          </Button>
          {materialValid ? (
            <div />
          ) : (
            <div style={{ color: "red" }}>
              <WarningIcon
                style={{
                  fontSize: "small",
                  marginRight: 10,
                }}
              ></WarningIcon>{" "}
              Bitte ein Material wählen
            </div>
          )}
        </Grid>
        <Grid item xs={2}></Grid>
      </Grid>
    </div>
  );
};

export default MatFertTable;
