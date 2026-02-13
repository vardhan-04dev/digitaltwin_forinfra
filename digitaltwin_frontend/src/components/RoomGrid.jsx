function RoomGrid({ rooms, onSelectRoom }) {
    return (
        <div className="room-grid">
            {rooms.map((room) => (
                <div key={room.id} className="room-card" onClick={() => onSelectRoom(room)}>
                    <h3>{room.name}</h3>
                </div>
            ))}
        </div>
    )
}
export default RoomGrid;