import LiveGraphs from "./LiveGraphs";
function RoomDetails({ room }) {
    if (!room) {
        return <div className="room-details">Select a room to see details</div>;
    }
    return (
        <>
        <h2>{room.name}</h2>
        <div className="room-details">
            <h3>live Monitoring</h3>
            <div className="live-values">
                <p>Temperature: {room.live.temp}°C</p>
                <p>Humidity: {room.live.humidity}%</p>
                <p>Power: {room.live.power}W</p>
            </div>
            <div className="expected-values"></div>
            <LiveGraph history={room.history} />
        </div>
        </>
        
    )
}
export default RoomDetails;