import { useEffect } from "react";
import axios from "axios";
import Board from './Board';

function App() {
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/state").then((response) => {
      console.log("API Response:", response.data);
    });
  }, []);

  return (
    <><h1>Connect 4</h1><Board /></>
  );
}

export default App;
