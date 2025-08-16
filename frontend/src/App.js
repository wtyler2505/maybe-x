import { useEffect, useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { getHello, getHealth, createStatus, listStatus } from "./api";

const Home = () => {
  const [hello, setHello] = useState("");
  const [health, setHealth] = useState("");
  const [clientName, setClientName] = useState("");
  const [items, setItems] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    (async () => {
      try {
        const h = await getHello();
        setHello(h.message);
        const hc = await getHealth();
        setHealth(hc.status);
        const list = await listStatus();
        setItems(list);
      } catch (e) {
        setError(String(e));
        // eslint-disable-next-line no-console
        console.error(e);
      }
    })();
  }, []);

  const onSubmit = async (e) => {
    e.preventDefault();
    try {
      await createStatus(clientName || "anonymous");
      setClientName("");
      const list = await listStatus();
      setItems(list);
    } catch (e1) {
      setError(String(e1));
    }
  };

  return (
    <div>
      <header className="App-header">
        <a className="App-link" href="https://emergent.sh" target="_blank" rel="noopener noreferrer">
          <img alt="emergent" src="https://avatars.githubusercontent.com/in/1201222?s=120&u=2686cf91179bbafbc7a71bfbc43004cf9ae1acea&v=4" />
        </a>
        <p className="mt-5">Building something incredible ~!</p>
        <div className="mt-4 text-sm opacity-80">Hello: {hello} • Health: {health || "unknown"}</div>
        <form onSubmit={onSubmit} className="mt-6 flex gap-2">
          <input
            value={clientName}
            onChange={(e) => setClientName(e.target.value)}
            placeholder="Client name"
            className="px-3 py-2 rounded-md text-black"
          />
          <button type="submit" className="px-3 py-2 rounded-md bg-blue-600">
            Create Status
          </button>
        </form>
        {error && <div className="mt-3 text-red-400">{error}</div>}
        <ul className="mt-6 text-left max-w-xl">
          {items.map((it) => (
            <li key={it.id} className="mb-2 border border-gray-700 rounded p-2">
              <div className="text-xs opacity-70">{it.id}</div>
              <div>{it.client_name}</div>
              <div className="text-xs opacity-70">{new Date(it.timestamp).toLocaleString()}</div>
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />}>
            <Route index element={<Home />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;