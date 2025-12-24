import { api } from "./api";
import { useState } from "react";

function App() {
  const [name, setName] = useState("");

  const createUser = async () => {
    await api.post("/users", { name });
    alert("User created");
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Expense Sharing App</h2>
      <input
        placeholder="User Name"
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={createUser}>Create User</button>
    </div>
  );
}

export default App;
