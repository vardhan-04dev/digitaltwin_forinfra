import { useEffect, useState } from "react";
import RoomGrid from "./components/RoomGrid";
import RoomDetails from "./components/RoomDetails";
import "./App.css";


function App() {
  const [rooms, setRooms] = useState([]);
  const [selectedRoom, setSelectedRoom] = useState(null);
  useEffect(() => {
    const fetchdata = async () => {
      try{
        const res = await fetch("http://localhost:5000/api/rooms");
        const data = await res.json();
        setRooms(data);
      } catch (error) {
        console.error("Error fetching rooms:", error);
      }
    };
    fetchdata();
    const interval = setInterval(fetchdata, 5000);
    return () => clearInterval(interval);
  }, []);
    
  return (
    <div className="App-container">
      <div className="title">
        <h1>Digital Twin for Infrastructure</h1>
      </div>
      <div className="main-container">
        <div className="left-panel">
          <RoomGrid rooms={rooms} onSelectRoom={setSelectedRoom} />
        </div>
        <div className="right-panel">
            <RoomDetails room={selectedRoom} />              
        </div>
      </div>
    </div>
  );
}

export default App;
