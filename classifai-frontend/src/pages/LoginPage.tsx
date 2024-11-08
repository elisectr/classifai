import React from "react";
import { Button, TextField, Box, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

const LoginPage: React.FC = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Logique de connexion (à implémenter)
    navigate("/menu");
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" mt={10}>
      <Typography variant="h4">Connexion</Typography>
      <TextField label="Nom d'utilisateur" variant="outlined" margin="normal" />
      <TextField label="Mot de passe" type="password" variant="outlined" margin="normal" />
      <Button variant="contained" onClick={handleLogin}>Se connecter</Button>
      <Button onClick={() => navigate("/register")}>S'inscrire</Button>
    </Box>
  );
};

export default LoginPage;
