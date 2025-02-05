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
    <><Board /></>
  );
}

export default App;
