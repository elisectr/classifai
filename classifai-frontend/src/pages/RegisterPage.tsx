import React from "react";
import { Button, TextField, Box, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

const RegisterPage: React.FC = () => {
  const navigate = useNavigate();

  const handleRegister = () => {
    // Logique d'inscription (à implémenter)
    navigate("/");
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" mt={10}>
      <Typography variant="h4">Inscription</Typography>
      <TextField label="Nom d'utilisateur" variant="outlined" margin="normal" />
      <TextField label="Mot de passe" type="password" variant="outlined" margin="normal" />
      <Button variant="contained" onClick={handleRegister}>S'inscrire</Button>
      <Button onClick={() => navigate("/")}>Retour</Button>
    </Box>
  );
};

export default RegisterPage;
