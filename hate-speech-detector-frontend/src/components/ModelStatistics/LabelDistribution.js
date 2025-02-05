import React from "react";
import { Pie } from "@ant-design/plots";

const LabelDistribution = ({ directoryData }) => {
  if (!directoryData || Object.keys(directoryData).length === 0) {
    return <div>No data available for Label Distribution</div>;
  }

  // Transform directory data (e.g., {0: count, 1: count}) into pie chart data
  const chartData = Object.entries(directoryData).map(([label, count]) => ({
    type: `Label: ${label}`,
    value: count,
  }));

  // Pie chart configuration
  const config = {
    appendPadding: 10,
    data: chartData,
    angleField: "value",
    colorField: "type",
    radius: 0.8,
    label: {
      type: "inner",
      offset: "-30%",
      content: ({ percent }) => `${(percent * 100).toFixed(1)}%`,
      style: {
        fontSize: 14,
        textAlign: "center",
      },
    },
    interactions: [{ type: "element-active" }],
  };

  return (
    <div>
      <h3>Label Distribution</h3>
      <Pie {...config} />
    </div>
  );
};

export default LabelDistribution;
