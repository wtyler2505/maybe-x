import axios from "axios";

// Backend URL must come from environment, never hardcode
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
if (!BACKEND_URL) {
  // eslint-disable-next-line no-console
  console.warn("REACT_APP_BACKEND_URL is not defined. API calls will fail.");
}

export const api = axios.create({
  baseURL: `${BACKEND_URL}/api`,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function getHello() {
  const { data } = await api.get("/");
  return data;
}

export async function getHealth() {
  const { data } = await api.get("/health");
  return data;
}

export async function createStatus(client_name) {
  const { data } = await api.post("/status", { client_name });
  return data; // { id, client_name, timestamp }
}

export async function listStatus() {
  const { data } = await api.get("/status");
  return data; // StatusCheck[]
}