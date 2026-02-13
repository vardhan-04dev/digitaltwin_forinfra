import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

function SingleGraph({ data, dataKey, title, stroke }) {
  return (
    <div className="graph-card">
      <h3>{title}</h3>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey={dataKey}
            stroke={stroke}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

function LiveGraphs({ history }) {
  if (!history) return null;

  return (
    <div className="graphs-container">
      <SingleGraph
        data={history}
        dataKey="temp"
        title="Temperature Trend"
        stroke="#ff4d4f"
      />

      <SingleGraph
        data={history}
        dataKey="humidity"
        title="Humidity Trend"
        stroke="#1890ff"
      />

      <SingleGraph
        data={history}
        dataKey="power"
        title="Power Consumption"
        stroke="#52c41a"
      />

      <SingleGraph
        data={history}
        dataKey="crowd"
        title="Crowd Frequency"
        stroke="#722ed1"
      />
    </div>
  );
}

export default LiveGraphs;
