function RoomGrid({ rooms, onSelectRoom }) {
    if (rooms.length === 0) {
        return <p>Loading rooms...</p>;
    }
    return (
        <div className="room-grid">
            {rooms.map((room) => (
                <div key={room.id} className={`room-block ${room.alert ? "alert" : ""}`} onClick={() => onSelectRoom(room)}>
                    <h3>{room.name}</h3>
                </div>
            ))}
        </div>
    )
}
export default RoomGrid;