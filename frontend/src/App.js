import React from 'react';
import { AppBar, Toolbar, Typography, Container, Grid, Paper } from '@material-ui/core';

function App() {
  return (
    <div className="App">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Interview Catalyst</Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg" style={{ marginTop: '2rem' }}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Paper style={{ padding: '1rem' }}>
              <Typography variant="h5">Welcome to Interview Catalyst</Typography>
              <Typography variant="body1">Your automated job application assistant</Typography>
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </div>
  );
}

export default App;