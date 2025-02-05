import React from "react";
import { Table } from "antd";

const ConfusionMatrix = ({ matrix }) => {
  if (!matrix || matrix.length === 0) {
    return <div>No data available for Confusion Matrix</div>;
  }

  const columns = [
    { title: "", dataIndex: "actual", key: "actual", width: 150 },
    {
      title: "Predicted: Positive",
      dataIndex: "predPositive",
      key: "predPositive",
    },
    {
      title: "Predicted: Negative",
      dataIndex: "predNegative",
      key: "predNegative",
    },
  ];

  const data = [
    {
      key: "1",
      actual: "Actual: Positive",
      predPositive: matrix[0][0],
      predNegative: matrix[0][1],
    },
    {
      key: "2",
      actual: "Actual: Negative",
      predPositive: matrix[1][0],
      predNegative: matrix[1][1],
    },
  ];

  return (
    <Table columns={columns} dataSource={data} pagination={false} bordered />
  );
};

export default ConfusionMatrix;
