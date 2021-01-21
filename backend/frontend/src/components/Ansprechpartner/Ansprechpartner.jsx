import React from "react";

import norman from "../../assets/img/norman_pytel.jpg";
import {
    Typography,
    makeStyles,
    Card,
    CardActionArea,
    CardMedia,
    CardContent,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    card: {
        maxWidth: 345,
    },
    media: {
        height: 320,
    },
}));

export const Ansprechpartner = () => {
    const classes = useStyles();
    return (
        <Card className={classes.card}>
            <CardActionArea>
                <CardMedia
                    className={classes.media}
                    image={norman}
                    title="Ansprechpartner"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        Norman Pytel
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                    >
                        Lehrstuhl für BWL und Wirtschaftsinformatik Prof. Dr.
                        Axel Winkelmann
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                    >
                        Julius-Maximilians-Universität Würzburg
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                    >
                        Sanderring 2
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                    >
                        97070 Würzburg
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                    >
                        E-Mail: Norman.Pytel@uni-wuerzburg.de
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                    >
                        Telefon: 0931 31-86348
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>
    );
};
