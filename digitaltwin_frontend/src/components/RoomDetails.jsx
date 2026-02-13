
function RoomDetails({ room }) {
    if (!room) {
        return <div className="room-details">Select a room to see details</div>;
    }
    return (
        <div className="room-details">
            <h3>{room.name} live Monitoring</h3>
            <p>Temperature: {room.temperature}°C</p>
            <p>Humidity: {room.humidity}%</p>
            <p>Power: {room.power}W</p>
        </div>

    )
}
export default RoomDetails;