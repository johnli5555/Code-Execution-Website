import axios from "axios";

// sets up an Axios instance configured to communicate with an FastAPI running on http://localhost:8000
const api = axios.create({
  baseURL: "http://localhost:8000",
});

export default api;
