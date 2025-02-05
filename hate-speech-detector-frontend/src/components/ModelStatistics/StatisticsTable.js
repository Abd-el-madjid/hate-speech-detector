// src/components/ModelStatistics/StatisticsTable.js
import React from "react";
import { Table, Card } from "antd";

const columns = [
  { title: "Data", dataIndex: "data", key: "data" },
  { title: "Input", dataIndex: "input", key: "input" },
  { title: "Output", dataIndex: "output", key: "output" },
];

const data = [
  { key: "1", data: "bessie.com", input: "#3003", output: "$8,500" },
  { key: "2", data: "naomie.info", input: "Details", output: "$700.00" },
  // Add more data rows as needed
];

const StatisticsTable = () => (
  <Card title="Model Statistics" style={{ marginTop: "20px" }}>
    <Table columns={columns} dataSource={data} pagination={{ pageSize: 4 }} />
  </Card>
);

export default StatisticsTable;
